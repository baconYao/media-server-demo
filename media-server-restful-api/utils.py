import shlex
import shutil
import os
import subprocess

SAMPLES = "./samples"

def _save_file_to_server(uploaded_file, path: str = SAMPLES):
    temp_file = os.path.join(path, uploaded_file.filename)

    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    return temp_file

def _playback_via_vlc(filename: str, path: str = SAMPLES):
    candidate = os.path.join(path, filename)
    cmd = f"vlc -f --no-video-title-show {candidate} vlc://quit"
    ret = subprocess.run(
        shlex.split(cmd),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        timeout=300,
    )
