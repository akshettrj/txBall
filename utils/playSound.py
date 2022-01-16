import subprocess


def play_sound(music_file):
    subprocess.Popen(
        ["mpg123", music_file],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
