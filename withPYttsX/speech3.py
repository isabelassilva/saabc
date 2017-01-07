#coding: utf-8

import pyttsx

engine = pyttsx.init()

engine.setProperty('rate', 100)

engine.setProperty('voice', 'brazil')

engine.say('Ola Mundo, 1 2 3')

voice = engine.getProperty('voice')

print (voice)

engine.runAndWait()