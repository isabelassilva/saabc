import urllib2
def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

if internet_on():

    from gtts import gTTS
    import os.path

# Letters #
    if not os.path.isfile("A_en.mp3"):
        tts = gTTS(text='Letter A, dot 1.', lang='en')
        tts.save("A_en.mp3")
    if not os.path.isfile("B_en.mp3"):
        tts = gTTS(text='Letter B, dots 1 and 2.', lang='en')
        tts.save("B_en.mp3")
    if not os.path.isfile("C_en.mp3"):
        tts = gTTS(text='Letter C, dots 1 and 4.', lang='en')
        tts.save("C_en.mp3")
    if not os.path.isfile("D_en.mp3"):
        tts = gTTS(text='Letter D, dots 1, 4 and 5.', lang='en')
        tts.save("D_en.mp3")
    if not os.path.isfile("E_en.mp3"):
        tts = gTTS(text='Letter E, dots 1 and 5.', lang='en')
        tts.save("E_en.mp3")
    if not os.path.isfile("F_en.mp3"):
        tts = gTTS(text='Letter F, dots 1, 2 and 4.', lang='en')
        tts.save("F_en.mp3")

    if not os.path.isfile("G_en.mp3"):
        tts = gTTS(text='Letter G, dots 1, 2, 4 and 5.', lang='en')
        tts.save("G_en.mp3")
    if not os.path.isfile("H_en.mp3"):
        tts = gTTS(text='Letter H, dots 1, 2 and 5.', lang='en')
        tts.save("H_en.mp3")
    if not os.path.isfile("I_en.mp3"):
        tts = gTTS(text='Letter I, dots 2 and 4.', lang='en')
        tts.save("I_en.mp3")
    if not os.path.isfile("J_en.mp3"):
        tts = gTTS(text='Letter J, dots 2, 4 and 5.', lang='en')
        tts.save("J_en.mp3")
    if not os.path.isfile("K_en.mp3"):
        tts = gTTS(text='Letter K, dots 1 and 3.', lang='en')
        tts.save("K_en.mp3")
    if not os.path.isfile("L_en.mp3"):
        tts = gTTS(text='Letter L, dots 1, 2 and 3.', lang='en')
        tts.save("L_en.mp3")
    if not os.path.isfile("M_en.mp3"):
        tts = gTTS(text='Letter M, dots 1, 3 and 4.', lang='en')
        tts.save("M_en.mp3")

    if not os.path.isfile("N_en.mp3"):
        tts = gTTS(text='Letter N, dots 1, 3, 4 and 5.', lang='en')
        tts.save("N_en.mp3")
    if not os.path.isfile("O_en.mp3"):
        tts = gTTS(text='Letter O, dots 1, 3 and 5.', lang='en')
        tts.save("O_en.mp3")
    if not os.path.isfile("P_en.mp3"):
        tts = gTTS(text='Letter P, dots 1, 2, 3 and 4.', lang='en')
        tts.save("P_en.mp3")
    if not os.path.isfile("Q_en.mp3"):
        tts = gTTS(text='Letter Q, dots 1, 2, 3, 4 and 5.', lang='en')
        tts.save("Q_en.mp3")
    if not os.path.isfile("R_en.mp3"):
        tts = gTTS(text='Letter R, dots 1, 2, 3 and 5.', lang='en')
        tts.save("R_en.mp3")
    if not os.path.isfile("S_en.mp3"):
        tts = gTTS(text='Letter S, dots 2, 3 and 4.', lang='en')
        tts.save("S_en.mp3")

    if not os.path.isfile("T_en.mp3"):
        tts = gTTS(text='Letter T, dots 2, 3, 4 and 5.', lang='en')
        tts.save("T_en.mp3")
    if not os.path.isfile("U_en.mp3"):
        tts = gTTS(text='Letter U, dots 1, 3 and 6.', lang='en')
        tts.save("U_en.mp3")
    if not os.path.isfile("V_en.mp3"):
        tts = gTTS(text='Letter V, dots 1, 2, 3 and 6.', lang='en')
        tts.save("V_en.mp3")
    if not os.path.isfile("W_en.mp3"):
        tts = gTTS(text='Letter W, dots 2, 4, 5 and 6.', lang='en')
        tts.save("W_en.mp3")
    if not os.path.isfile("X_en.mp3"):
        tts = gTTS(text='Letter X, dots dots 1, 3, 4 and 6.', lang='en')
        tts.save("X_en.mp3")
    if not os.path.isfile("Y_en.mp3"):
        tts = gTTS(text='Letter Y, dots 1, 3, 4, 5 and 6.', lang='en')
        tts.save("Y_en.mp3")
    if not os.path.isfile("Z_en.mp3"):
        tts = gTTS(text='Letter Z, dots 1, 3, 5 and 6.', lang='en')
        tts.save("Z_en.mp3")

# Numbers #
    if not os.path.isfile("1_en.mp3"):
        tts = gTTS(text='Number 1, dot 1.', lang='en')
        tts.save("1_en.mp3")
    if not os.path.isfile("2_en.mp3"):
        tts = gTTS(text='Number 2, dots 1 and 2.', lang='en')
        tts.save("2_en.mp3")
    if not os.path.isfile("3_en.mp3"):
        tts = gTTS(text='Number 3, dots 1 and 4.', lang='en')
        tts.save("3_en.mp3")
    if not os.path.isfile("4_en.mp3"):
        tts = gTTS(text='Number 4, dots 1, 4 and 5.', lang='en')
        tts.save("4_en.mp3")
    if not os.path.isfile("5_en.mp3"):
        tts = gTTS(text='Number 5, dots 1 and 5.', lang='en')
        tts.save("5_en.mp3")
    if not os.path.isfile("6_en.mp3"):
        tts = gTTS(text='Number 6, dots 1, 2 and 4.', lang='en')
        tts.save("6_en.mp3")

    if not os.path.isfile("7_en.mp3"):
        tts = gTTS(text='Number 7, dots 1, 2, 4 and 5.', lang='en')
        tts.save("7_en.mp3")
    if not os.path.isfile("8_en.mp3"):
        tts = gTTS(text='Number 8, dots 1, 2 and 5.', lang='en')
        tts.save("8_en.mp3")
    if not os.path.isfile("9_en.mp3"):
        tts = gTTS(text='Number 9, dots 2 and 4.', lang='en')
        tts.save("9_en.mp3")
    if not os.path.isfile("0_en.mp3"):
        tts = gTTS(text='Number 0, dots 2, 4 and 5.', lang='en')
        tts.save("0_en.mp3")

else:
    print("This procedure requires a internet conneciont.")
