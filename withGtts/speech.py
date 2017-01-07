from gtts import gTTS

tts = gTTS(text='Hello', lang='en')

tts.save("hello.mp3")

from Tkinter import *
root = Tk()

from pygame import mixer
mixer.init()
mixer.music.load('hello.mp3')
mixer.music.play()

root.mainloop()
