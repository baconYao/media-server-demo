# server.py
import rpyc
import shlex
import subprocess


class MediaServerService(rpyc.Service):

    def exposed_play_video(self, file_path):
        try:
            cmd = f"vlc -f --no-video-title-show {file_path} vlc://quit"
            subprocess.run(
                shlex.split(cmd),
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding="utf-8",
            )
            return "Video playback started successfully."
        except Exception as e:
            return f"Error playing video: {str(e)}"


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    # port = 60000    # zapper service listens port 6000 as well
    port = 18819    # zapper service listens port 6000 as well
    server = ThreadedServer(MediaServerService, port=port)
    print(f"MediaServerService started, listening on port {port}...")
    server.start()
