import sys
from song import powerpuff_song, posca_song

def jukebox(track):
    if track == 1:
        powerpuff_song()
    elif track == 2:
        posca_song()
    else:
        print('We only have two songs for now !')


if __name__ == '__main__':
    args = sys.argv

    if len(args) != 2:
        print('Usage: python3 new_jukebox.py <track>')
        exit(1)

    track = args[1]
    if not track.isdigit():
        print('Error: track must be an int, not', track)
        exit(2)

    print('Running jukebox!')
    jukebox(int(track))
