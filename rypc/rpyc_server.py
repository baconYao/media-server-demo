# server.py
import os
import rpyc
import subprocess


class MediaServerService(rpyc.Service):
    DEFAULT_FILE_PATH = os.path.join(
        os.getenv("HOME"), "media_sample", "sample_2_big_bug_bunny", "{}"
    )

    def exposed_check_file_exists(self, file_name):
        """"""
        return os.path.exists(self.DEFAULT_FILE_PATH.format(file_name))

    def exposed_play_video(self, file_name):
        try:
            subprocess.run(["vlc", self.DEFAULT_FILE_PATH.format(file_name)])
            return "Video playback started successfully."
        except Exception as e:
            return f"Error playing video: {str(e)}"

    def exposed_get_image_type(sefl):
        try:
            ret = subprocess.run(
                ["dpkg", "-s", "ubuntu-desktop"],
            )
            if ret.returncode == 0:
                return "desktop"
            else:
                return "server"
        except Exception as e:
            print(e)
            return f"Error getting image type: {str(e)}"


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    # port = 60000    # zapper service listens port 6000 as well
    port = 18812    # zapper service listens port 6000 as well
    server = ThreadedServer(MediaServerService, port=port)
    print(f"MediaServerService started, listening on port {port}...")
    server.start()
