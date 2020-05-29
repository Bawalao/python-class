from song import powerpuff_song, posca_song

def jukebox(track):
    if track == 1:
        powerpuff_song()
    elif track == 2:
        posca_song()
    else:
        print('We only have two songs for now !')

print('Running the jukebox!')
jukebox(1)
