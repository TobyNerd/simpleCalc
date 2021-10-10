import winsound


def play_music():
    winsound.PlaySound("music/8-bit Detective.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
