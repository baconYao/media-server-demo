# client.py
import rpyc

if __name__ == "__main__":
    # conn = rpyc.connect("localhost", 18819, config={"allow_all_attrs": True})
    conn = rpyc.connect(
        "10.102.182.83", 18819, config={"allow_all_attrs": True}
    )

    video_path = "/home/ubuntu/sample/video1.mp4"
    result = conn.root.play_video(video_path)

    print(result)

    conn.close()
