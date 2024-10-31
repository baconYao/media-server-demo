import os


def resource_generator():
    pass


class MediaServerAdapter:
    """
    MediaServerAdapter class handles anything on Media Server side. A Media
    Server can be a laptop with Ubuntu Desktop environment 24.04 or later.

    (Whatever?) No matter what type of Media Server is, the golden sample
    (big_buck_bunny) must be placed on it properly.
    """

    MEDIA_SERVER_IP = "HDMI_INPUT_MEDIA_SERVER_IP"

    def __init__(self) -> None:
        self._media_server_ip = os.getenv(self.MEDIA_SERVER_IP)
        self._golden_sample = os.path.join(
            "$HOME",
            "media_server",
            "sample_2_big_bug_bunny",
            "big_bug_bunny_1920x1080_60fps_h264.mp4",
        )

    def _change_to_mirror_mode(self):
        # TODO: change Media Server to Mirror mode / 關閉 internal output，
        # 只有一個 external video output
        # Resolution 我記得都是固定在 1920x1080，Media Server 看到的狀況)
        pass

    def _set_audio_output(self):
        # TODO: 調整 audio 的輸出
        pass

    def has_media_server_detected_the_output(self) -> bool:
        """
        需要一個方式確認 Media Server 有偵測到 DUT 作為他的 video output
        目前假設是一台 24.04 的 laptop / Zapper server image
        - 24.04 lapto
            - 我想自動轉成 mirror mode，已確保 playe 可以正確的 video 輸出
            - audio volume 自動音量調整為最大聲
        """

        pass

    def _get_media_server_image_type(self) -> str:
        """
        Get the imagae type of Media Server

        :returns:
            "desktop" or "server"
        """
        # TODO: 檢查 desktop / server
        pass

    def _check_file_exist(self, file_path: str) -> bool:
        """
        Make sure the a specifc file exists at Media Server. This file will be
        played on Media Server side via some kind of player like vlc.

        :param file_path:
            A file name or full path be sent to Media Sever and get feedback
            to see if it existsed or not.

        :returns:
            True if the file exists at Media Server, False otherwise
        """
        # TODO: Call api to check file
        pass

    def adjust_media_server_environment(self) -> None:
        """
        Trigger the Mideo Server plays a specific video.
        """
        if not self._check_file_exist(file_path=self._golden_sample):
            raise SystemExit()

    def play_video(self) -> None:
        """
        Trigger the Mideo Server plays a video.
        """
        # TODO: call api to play sprcific video
        pass


def record():
    """
    A context manager to handle recording in background
    """
    pass


def preview():
    pass


def video_record():
    pass


def audio_record():
    pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
