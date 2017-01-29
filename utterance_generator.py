import os.path
import pyttsx
import vlc

__PATH__ = "mp3files/"              #path to where the mp3files are recorded

def msg_definer(character):
    character = character.upper()
    if (character == 'A'):
        if os.path.isfile(__PATH__ + "A_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "A_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter A, dot 1.")
            engine.runAndWait()
        return "Letter A, dot 1."
    if (character == 'B'):
        if os.path.isfile(__PATH__ + "B_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "B_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter B, dots 1 and 2.")
            engine.runAndWait()
        return "Letter B, dots 1 and 2."
    if (character == 'C'):
        if os.path.isfile(__PATH__ + "C_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "C_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter C, dots 1 and 4.")
            engine.runAndWait()
        return "Letter C, dots 1 and 4."
    if (character == 'D'):
        if os.path.isfile(__PATH__ + "D_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "D_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter D, dots 1, 4 and 5.")
            engine.runAndWait()
        return "Letter D, dots 1, 4 and 5."
    if (character == 'E'):
        if os.path.isfile(__PATH__ + "E_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "E_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter E, dots 1 and 5.")
            engine.runAndWait()
        return "Letter E, dots 1 and 5."
    if (character == 'F'):
        if os.path.isfile(__PATH__ + "F_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "F_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter F, dots 1, 2 and 4.")
            engine.runAndWait()
        return "Letter F, dots 1, 2 and 4."

    if (character == 'G'):
        if os.path.isfile(__PATH__ + "G_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "G_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter G, dots 1, 2, 4 and 5.")
            engine.runAndWait()
        return "Letter G, dots 1, 2, 4 and 5."
    if (character == 'H'):
        if os.path.isfile(__PATH__ + "H_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "H_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter H, dots 1, 2 and 5.")
            engine.runAndWait()
        return "Letter H, dots 1, 2 and 5."
    if (character == 'I'):
        if os.path.isfile(__PATH__ + "I_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "I_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter I, dots 2 and 4.")
            engine.runAndWait()
        return "Letter I, dots 2 and 4."
    if (character == 'J'):
        if os.path.isfile(__PATH__ + "J_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "J_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter J, dots 2, 4 and 5.")
            engine.runAndWait()
        return "Letter J, dots 2, 4 and 5."
    if (character == 'K'):
        if os.path.isfile(__PATH__ + "K_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "K_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter K, dots 1 and 3.")
            engine.runAndWait()
        return "Letter K, dots 1 and 3."
    if (character == 'L'):
        if os.path.isfile(__PATH__ + "L_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "L_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter L, dots 1, 2 and 3.")
            engine.runAndWait()
        return "Letter L, dots 1, 2 and 3."
    if (character == 'M'):
        if os.path.isfile(__PATH__ + "M_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "M_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter M, dots 1, 3 and 4.")
            engine.runAndWait()
        return "Letter M, dots 1, 3 and 4."

    if (character == 'N'):
        if os.path.isfile(__PATH__ + "N_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "N_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter N, dots 1, 3, 4 and 5.")
            engine.runAndWait()
        return "Letter N, dots 1, 3, 4 and 5."
    if (character == 'O'):
        if os.path.isfile(__PATH__ + "O_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "O_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter O, dots 1, 3 and 5.")
            engine.runAndWait()
        return "Letter O, dots 1, 3 and 5."
    if (character == 'P'):
        if os.path.isfile(__PATH__ + "P_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "P_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter P, dots 1, 2, 3 and 4.")
            engine.runAndWait()
        return "Letter P, dots 1, 2, 3 and 4."
    if (character == 'Q'):
        if os.path.isfile(__PATH__ + "Q_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "Q_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter Q, dots 1, 2, 3, 4 and 5.")
            engine.runAndWait()
        return "Letter Q, dots 1, 2, 3, 4 and 5."
    if (character == 'R'):
        if os.path.isfile(__PATH__ + "R_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "R_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter R, dots 1, 2, 3 and 5.")
            engine.runAndWait()
        return "Letter R, dots 1, 2, 3 and 5."
    if (character == 'S'):
        if os.path.isfile(__PATH__ + "S_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "S_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter S, dots 2, 3 and 4.")
            engine.runAndWait()
        return "Letter S, dots 2, 3 and 4."

    if (character == 'T'):
        if os.path.isfile(__PATH__ + "T_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "T_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter T, dots 2, 3, 4 and 5.")
            engine.runAndWait()
        return "Letter T, dots 2, 3, 4 and 5."
    if (character == 'U'):
        if os.path.isfile(__PATH__ + "U_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "U_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter U, dots 1, 3 and 6.")
            engine.runAndWait()
        return "Letter U, dots 1, 3 and 6."
    if (character == 'V'):
        if os.path.isfile(__PATH__ + "V_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "V_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter V, dots 1, 2, 3 and 6.")
            engine.runAndWait()
        return "Letter V, dots 1, 2, 3 and 6."
    if (character == 'W'):
        if os.path.isfile(__PATH__ + "W_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "W_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter W, dots 2, 4, 5 and 6.")
            engine.runAndWait()
        return "Letter W, dots 2, 4, 5 and 6."
    if (character == 'X'):
        if os.path.isfile(__PATH__ + "X_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "X_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter X, dots dots 1, 3, 4 and 6.")
            engine.runAndWait()
        return "Letter X, dots dots 1, 3, 4 and 6."
    if (character == 'Y'):
        if os.path.isfile(__PATH__ + "Y_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "Y_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter Y, dots 1, 3, 4, 5 and 6.")
            engine.runAndWait()
        return "Letter Y, dots 1, 3, 4, 5 and 6."
    if (character == 'Z'):
        if os.path.isfile(__PATH__ + "Z_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "Z_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Letter Z, dots 1, 3, 5 and 6.")
            engine.runAndWait()
        return "Letter Z, dots 1, 3, 5 and 6."

    if (character == '1'):
        if os.path.isfile(__PATH__ + "1_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "1_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Number 1, dot 1.")
            engine.runAndWait()
        return "Number 1, dot 1."
    if (character == '2'):
        if os.path.isfile(__PATH__ + "2_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "2_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Number 2, dots 1 and 2.")
            engine.runAndWait()
        return "Number 2, dots 1 and 2."
    if (character == '3'):
        if os.path.isfile(__PATH__ + "3_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "3_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Number 3, dots 1 and 4.")
            engine.runAndWait()
        return "Number 3, dots 1 and 4."
    if (character == '4'):
        if os.path.isfile(__PATH__ + "4_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "4_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Number 4, dots 1, 4 and 5.")
            engine.runAndWait()
        return "Number 4, dots 1, 4 and 5."
    if (character == '5'):
        if os.path.isfile(__PATH__ + "5_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "5_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Number 5, dots 1 and 5.")
            engine.runAndWait()
        return "Number 5, dots 1 and 5."
    if (character == '6'):
        if os.path.isfile(__PATH__ + "6_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "6_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Number 6, dots 1, 2, and 4.")
            engine.runAndWait()
        return "Number 6, dots 1, 2, and 4."
    if (character == '7'):
        if os.path.isfile(__PATH__ + "7_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "7_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Number 7, dots 1, 2, 4 and 5.")
            engine.runAndWait()
        return "Number 7, dots 1, 2, 4 and 5."
    if (character == '8'):
        if os.path.isfile(__PATH__ + "8_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "8_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Number 8, dots 1, 2 and 5.")
            engine.runAndWait()
        return "Number 8, dots 1, 2 and 5."
    if (character == '9'):
        if os.path.isfile(__PATH__ + "9_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "9_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Number 9, dots 2 and 4.")
            engine.runAndWait()
        return "Number 9, dots 2 and 4."
    if (character == '0'):
        if os.path.isfile(__PATH__ + "0_en.mp3"):
            vlc.MediaPlayer(__PATH__ + "0_en.mp3").play()
        else:
            engine = pyttsx.init()
            engine.say("Number 0, dots 2, 4 and 5.")
            engine.runAndWait()
        return "Number 0, dots 2, 4 and 5."
