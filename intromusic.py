# coding=utf-8

import pygame
import bluetooth
import time
import datetime

# Bluetooth ID : [song path, playedToday]
songID = {
        '84:38:35:AB:FA:F9' : ['/home/pi/IntroMusic/nicksong.mp3',False], # Nick
        '70:05:14:B7:56:EB' : ['/home/pi/IntroMusic/song.mp3',False], # Tristan
        '64:A7:69:63:41:C0' : ['/home/pi/IntroMusic/song.mp3',False], # kevin
        '40:B3:95:IF:04:F0' : ['/home/pi/IntroMusic/alexfsong.mp3',False], # Alex F
        '68:A8:60:9E:3E:2C' : ['/home/pi/IntroMusic/alexssong.mp3',False], # Alex S
        '00:F4:B0:00:B7:71' : ['/home/pi/IntroMusic/davesong.mp3',False], # Dave 
        'CC:78:5F:A1:FZ:67' : ['/home/pi/IntroMusic/jinsong.mp3',False], # Jinyoung 
        '8C:58:77:9E:15:CB' : ['/home/pi/IntroMusic/jennasong.mp3',False], # Jenna 
        '04:F7:E4:90:FD:89' : ['/home/pi/IntroMusic/richardsong.mp3',False], # Richard 
        'B8:17:C2:08:8A:ID' : ['/home/pi/IntroMusic/andrewsong.mp3',False], # Andrew
        '68:A8:6D:AF:42:C1' : ['/home/pi/IntroMusic/stevesong.mp3',False], # Steve 
        '24:AB:81:E0:7F:7E' : ['/home/pi/IntroMusic/timsong.mp3',False], # Tim 
        '7C:FA:DF:99:DF:05' : ['/home/pi/IntroMusic/marksong.mp3',False], # Mark 
         }

firstAtWork = True

def reset():
    for ID in songID:
        songID[ID][1] = False
    firstAtWork = True


while 1:

    nearby_devices = bluetooth.discover_devices(duration=1,lookup_names=False)
    print nearby_devices

    songPlayed = False

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute

    if (hour == 6 or hour == 18) and minute == 0:
        reset()
        time.sleep(61)

    if firstAtWork == False:
        for bdaddr in nearby_devices:
            for ID in songID:
                if ID == bdaddr and songPlayed == False and songID[ID][1] == False:
                    pygame.mixer.init(frequency=22050, size = -16, channels = 2, buffer = 4096)
                    pygame.mixer.music.load(songID[ID][0])
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        pygame.time.Clock().tick(10)
                    songPlayed = True
                    songID[ID][1] = True
                    time.sleep(10)
    else: 
        firstAtWork = False
        time.sleep(30)
    
    
    
    
    
    