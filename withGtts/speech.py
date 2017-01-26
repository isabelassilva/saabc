from gtts import gTTS

tts = gTTS(text='Hello', lang='en')

tts.save("hello.mp3")

#from Tkinter import *
#root = Tk()

"""
from pygame import mixer
mixer.init()
mixer.music.load('hello.mp3')
mixer.music.play()

import vlc
p = vlc.MediaPlayer("hello.mp3")
p.play()

import webbrowser
webbrowser.open("hello.mp3")
"""
from subprocess import call
call(["cvlc", "hello.mp3"])     #"vlc" uses default interface / "cvlc" uses dummy interface module ("without interface")

#root.mainloop()
