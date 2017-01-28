import os.path
from subprocess import call
import pyttsx

def msg_definer(character):
    character = character.upper()
    if (character == 'A'):
        if os.path.isfile("A.mp3"):
            call(["cvlc", "A.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter A, dot 1.")
            engine.runAndWait()
        return "Letter A, dot 1."
    if (character == 'B'):
        if os.path.isfile("B.mp3"):
            call(["cvlc", "B.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter B, dots 1 and 2.")
            engine.runAndWait()
        return "Letter B, dots 1 and 2."
    if (character == 'C'):
        if os.path.isfile("C.mp3"):
            call(["cvlc", "C.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter C, dots 1 and 4.")
            engine.runAndWait()
        return "Letter C, dots 1 and 4."
    if (character == 'D'):
        if os.path.isfile("D.mp3"):
            call(["cvlc", "D.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter D, dots 1, 4 and 5.")
            engine.runAndWait()
        return "Letter D, dots 1, 4 and 5."
    if (character == 'E'):
        if os.path.isfile("E.mp3"):
            call(["cvlc", "E.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter E, dots 1 and 5.")
            engine.runAndWait()
        return "Letter E, dots 1 and 5."
    if (character == 'F'):
        if os.path.isfile("F.mp3"):
            call(["cvlc", "F.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter F, dots 1, 2 and 4.")
            engine.runAndWait()
        return "Letter F, dots 1, 2 and 4."

    if (character == 'G'):
        if os.path.isfile("G.mp3"):
            call(["cvlc", "G.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter G, dots 1, 2, 4 and 5.")
            engine.runAndWait()
        return "Letter G, dots 1, 2, 4 and 5."
    if (character == 'H'):
        if os.path.isfile("H.mp3"):
            call(["cvlc", "H.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter H, dots 1, 2 and 5.")
            engine.runAndWait()
        return "Letter H, dots 1, 2 and 5."
    if (character == 'I'):
        if os.path.isfile("I.mp3"):
            call(["cvlc", "I.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter I, dots 2 and 4.")
            engine.runAndWait()
        return "Letter I, dots 2 and 4."
    if (character == 'J'):
        if os.path.isfile("J.mp3"):
            call(["cvlc", "J.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter J, dots 2, 4 and 5.")
            engine.runAndWait()
        return "Letter J, dots 2, 4 and 5."
    if (character == 'K'):
        if os.path.isfile("K.mp3"):
            call(["cvlc", "K.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter K, dots 1 and 3.")
            engine.runAndWait()
        return "Letter K, dots 1 and 3."
    if (character == 'L'):
        if os.path.isfile("L.mp3"):
            call(["cvlc", "L.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter L, dots 1, 2 and 3.")
            engine.runAndWait()
        return "Letter L, dots 1, 2 and 3."
    if (character == 'M'):
        if os.path.isfile("M.mp3"):
            call(["cvlc", "M.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter M, dots 1, 3 and 4.")
            engine.runAndWait()
        return "Letter M, dots 1, 3 and 4."

    if (character == 'N'):
        if os.path.isfile("N.mp3"):
            call(["cvlc", "N.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter N, dots 1, 3, 4 and 5.")
            engine.runAndWait()
        return "Letter N, dots 1, 3, 4 and 5."
    if (character == 'O'):
        if os.path.isfile("O.mp3"):
            call(["cvlc", "O.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter O, dots 1, 3 and 5.")
            engine.runAndWait()
        return "Letter O, dots 1, 3 and 5."
    if (character == 'P'):
        if os.path.isfile("P.mp3"):
            call(["cvlc", "P.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter P, dots 1, 2, 3 and 4.")
            engine.runAndWait()
        return "Letter P, dots 1, 2, 3 and 4."
    if (character == 'Q'):
        if os.path.isfile("Q.mp3"):
            call(["cvlc", "Q.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter Q, dots 1, 2, 3, 4 and 5.")
            engine.runAndWait()
        return "Letter Q, dots 1, 2, 3, 4 and 5."
    if (character == 'R'):
        if os.path.isfile("R.mp3"):
            call(["cvlc", "R.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter R, dots 1, 2, 3 and 5.")
            engine.runAndWait()
        return "Letter R, dots 1, 2, 3 and 5."
    if (character == 'S'):
        if os.path.isfile("S.mp3"):
            call(["cvlc", "S.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter S, dots 2, 3 and 4.")
            engine.runAndWait()
        return "Letter S, dots 2, 3 and 4."

    if (character == 'T'):
        if os.path.isfile("T.mp3"):
            call(["cvlc", "T.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter T, dots 2, 3, 4 and 5.")
            engine.runAndWait()
        return "Letter T, dots 2, 3, 4 and 5."
    if (character == 'U'):
        if os.path.isfile("U.mp3"):
            call(["cvlc", "U.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter U, dots 1, 3 and 6.")
            engine.runAndWait()
        return "Letter U, dots 1, 3 and 6."
    if (character == 'V'):
        if os.path.isfile("V.mp3"):
            call(["cvlc", "V.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter V, dots 1, 2, 3 and 6.")
            engine.runAndWait()
        return "Letter V, dots 1, 2, 3 and 6."
    if (character == 'W'):
        if os.path.isfile("W.mp3"):
            call(["cvlc", "W.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter W, dots 2, 4, 5 and 6.")
            engine.runAndWait()
        return "Letter W, dots 2, 4, 5 and 6."
    if (character == 'X'):
        if os.path.isfile("X.mp3"):
            call(["cvlc", "X.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter X, dots dots 1, 3, 4 and 6.")
            engine.runAndWait()
        return "Letter X, dots dots 1, 3, 4 and 6."
    if (character == 'Y'):
        if os.path.isfile("Y.mp3"):
            call(["cvlc", "Y.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter Y, dots 1, 3, 4, 5 and 6.")
            engine.runAndWait()
        return "Letter Y, dots 1, 3, 4, 5 and 6."
    if (character == 'Z'):
        if os.path.isfile("Z.mp3"):
            call(["cvlc", "Z.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Letter Z, dots 1, 3, 5 and 6.")
            engine.runAndWait()
        return "Letter Z, dots 1, 3, 5 and 6."

    if (character == '1'):
        if os.path.isfile("1.mp3"):
            call(["cvlc", "1.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Number 1, dot 1.")
            engine.runAndWait()
        return "Number 1, dot 1."
    if (character == '2'):
        if os.path.isfile("2.mp3"):
            call(["cvlc", "2.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Number 2, dots 1 and 2.")
            engine.runAndWait()
        return "Number 2, dots 1 and 2."
    if (character == '3'):
        if os.path.isfile("3.mp3"):
            call(["cvlc", "3.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Number 3, dots 1 and 4.")
            engine.runAndWait()
        return "Number 3, dots 1 and 4."
    if (character == '4'):
        if os.path.isfile("4.mp3"):
            call(["cvlc", "4.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Number 4, dots 1, 4 and 5.")
            engine.runAndWait()
        return "Number 4, dots 1, 4 and 5."
    if (character == '5'):
        if os.path.isfile("5.mp3"):
            call(["cvlc", "5.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Number 5, dots 1 and 5.")
            engine.runAndWait()
        return "Number 5, dots 1 and 5."
    if (character == '6'):
        if os.path.isfile("6.mp3"):
            call(["cvlc", "6.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Number 6, dots 1, 2, and 4.")
            engine.runAndWait()
        return "Number 6, dots 1, 2, and 4."
    if (character == '7'):
        if os.path.isfile("7.mp3"):
            call(["cvlc", "7.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Number 7, dots 1, 2, 4 and 5.")
            engine.runAndWait()
        return "Number 7, dots 1, 2, 4 and 5."
    if (character == '8'):
        if os.path.isfile("8.mp3"):
            call(["cvlc", "8.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Number 8, dots 1, 2 and 5.")
            engine.runAndWait()
        return "Number 8, dots 1, 2 and 5."
    if (character == '9'):
        if os.path.isfile("9.mp3"):
            call(["cvlc", "9.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Number 9, dots 2 and 4.")
            engine.runAndWait()
        return "Number 9, dots 2 and 4."
    if (character == '0'):
        if os.path.isfile("0.mp3"):
            call(["cvlc", "0.mp3"])
        else:
            engine = pyttsx.init()
            engine.say("Number 0, dots 2, 4 and 5.")
            engine.runAndWait()
        return "Number 0, dots 2, 4 and 5."
