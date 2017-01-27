import pyttsx

from Tkinter import *

def key(event):
    engine = pyttsx.init()
    if event.char == event.keysym:
        from table import msg_definer
        msg = msg_definer(event.char)
    elif len(event.char) == 1:
        msg = 'Punctuation Key %r (%r)' % (event.keysym, event.char)
    else:
        msg = 'Special Key %r' % event.keysym
    label1.config(text=msg)
    engine.say(msg)
    engine.runAndWait()

root = Tk()
prompt = '      Press any key      '
label1 = Label(root, text=prompt, width=len(prompt), bg='yellow')
label1.pack()

root.bind_all('<Key>', key)

root.mainloop()