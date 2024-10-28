# client.py
import rpyc

if __name__ == "__main__":
    conn = rpyc.connect("localhost", 60000)

    result = conn.root.check_file_exists("hello")

    # video_path = "/home/baconyao/Videos/my-experiment/big_buck_bunny/bbb_sunflower_1080p_30fps_normal.mp4"
    # result = conn.root.play_video(video_path)

    # result = conn.root.get_image_type()


    print(result)

    conn.close()
