#to put music you need to copy the relative path putting the songs into the songs folder
from pygame import mixer

mixer.init()
song=str(input('Select a song: '))
mixer.music.load(song)
mixer.music.set_volume(1)
mixer.music.play()

while True:
    print(' Press k to stop the music')
    print('Press r to resume')
    print('Press c to change song')
    print('Press q to exit')

    opcion = input('-')
    if opcion == 'k':
        mixer.music.pause(song)
    elif opcion == 'r':
        mixer.music.unpause()
    elif opcion == 'c':
        mixer.music.stop()
        cancion=str(input('Select a song: '))  
        mixer.music.load(song)
        mixer.music.set_volume(1)
        mixer.music.play()           
    elif opcion=='q':
        mixer.music.stop
        break
    