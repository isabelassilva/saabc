#coding:utf-8
import urllib2
def internet_on():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err:
        return False

__LANGUAGE__ = 'pt-br'

if __LANGUAGE__ == 'en':
    __LETTER__ = 'Letter'
    __NUMBER__ = 'Number'
    __DOT__ = 'dot'
    __AND__ = 'and'

if __LANGUAGE__ == 'pt-br':
    __LETTER__ = 'Letra'
    __NUMBER__ = 'Numero'
    __DOT__ = 'ponto'
    __AND__ = 'e'


if internet_on():

    from gtts import gTTS
    import os.path

# Letters #
    if not os.path.isfile("A_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' A, ' + __DOT__ + ' 1.', lang=__LANGUAGE__)
        tts.save("A_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("B_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' B, ' + __DOT__ + 's 1 ' + __AND__ + ' 2.', lang=__LANGUAGE__)
        tts.save("B_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("C_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' C, ' + __DOT__ + 's 1 ' + __AND__ + ' 4.', lang=__LANGUAGE__)
        tts.save("C_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("D_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' D, ' + __DOT__ + 's 1, 4 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("D_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("E_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' E, ' + __DOT__ + 's 1 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("E_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("F_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' F, ' + __DOT__ + 's 1, 2 ' + __AND__ + ' 4.', lang=__LANGUAGE__)
        tts.save("F_" + __LANGUAGE__ + ".mp3")

    if not os.path.isfile("G_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' G, ' + __DOT__ + 's 1, 2, 4 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("G_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("H_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' H, ' + __DOT__ + 's 1, 2 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("H_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("I_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' I, ' + __DOT__ + 's 2 ' + __AND__ + ' 4.', lang=__LANGUAGE__)
        tts.save("I_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("J_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' J, ' + __DOT__ + 's 2, 4 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("J_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("K_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' K, ' + __DOT__ + 's 1 ' + __AND__ + ' 3.', lang=__LANGUAGE__)
        tts.save("K_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("L_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' L, ' + __DOT__ + 's 1, 2 ' + __AND__ + ' 3.', lang=__LANGUAGE__)
        tts.save("L_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("M_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' M, ' + __DOT__ + 's 1, 3 ' + __AND__ + ' 4.', lang=__LANGUAGE__)
        tts.save("M_" + __LANGUAGE__ + ".mp3")

    if not os.path.isfile("N_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' N, ' + __DOT__ + 's 1, 3, 4 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("N_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("O_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' O, ' + __DOT__ + 's 1, 3 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("O_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("P_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' P, ' + __DOT__ + 's 1, 2, 3 ' + __AND__ + ' 4.', lang=__LANGUAGE__)
        tts.save("P_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("Q_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' Q, ' + __DOT__ + 's 1, 2, 3, 4 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("Q_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("R_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' R, ' + __DOT__ + 's 1, 2, 3 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("R_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("S_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' S, ' + __DOT__ + 's 2, 3 ' + __AND__ + ' 4.', lang=__LANGUAGE__)
        tts.save("S_" + __LANGUAGE__ + ".mp3")

    if not os.path.isfile("T_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' T, ' + __DOT__ + 's 2, 3, 4 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("T_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("U_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' U, ' + __DOT__ + 's 1, 3 ' + __AND__ + ' 6.', lang=__LANGUAGE__)
        tts.save("U_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("V_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' V, ' + __DOT__ + 's 1, 2, 3 ' + __AND__ + ' 6.', lang=__LANGUAGE__)
        tts.save("V_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("W_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' W, ' + __DOT__ + 's 2, 4, 5 ' + __AND__ + ' 6.', lang=__LANGUAGE__)
        tts.save("W_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("X_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' X, ' + __DOT__ + 's' + __DOT__ + 's 1, 3, 4 ' + __AND__ + ' 6.', lang=__LANGUAGE__)
        tts.save("X_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("Y_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' Y, ' + __DOT__ + 's 1, 3, 4, 5 ' + __AND__ + ' 6.', lang=__LANGUAGE__)
        tts.save("Y_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("Z_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__LETTER__ + ' Z, ' + __DOT__ + 's 1, 3, 5 ' + __AND__ + ' 6.', lang=__LANGUAGE__)
        tts.save("Z_" + __LANGUAGE__ + ".mp3")

# Numbers #
    if not os.path.isfile("1_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__NUMBER__ + ' 1,' + __DOT__ + ' 1.', lang=__LANGUAGE__)
        tts.save("1_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("2_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__NUMBER__ + ' 2,' + __DOT__ + 's 1 ' + __AND__ + ' 2.', lang=__LANGUAGE__)
        tts.save("2_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("3_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__NUMBER__ + ' 3,' + __DOT__ + 's 1 ' + __AND__ + ' 4.', lang=__LANGUAGE__)
        tts.save("3_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("4_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__NUMBER__ + ' 4,' + __DOT__ + 's 1, 4 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("4_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("5_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__NUMBER__ + ' 5,' + __DOT__ + 's 1 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("5_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("6_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__NUMBER__ + ' 6,' + __DOT__ + 's 1, 2 ' + __AND__ + ' 4.', lang=__LANGUAGE__)
        tts.save("6_" + __LANGUAGE__ + ".mp3")

    if not os.path.isfile("7_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__NUMBER__ + ' 7,' + __DOT__ + 's 1, 2, 4 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("7_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("8_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__NUMBER__ + ' 8,' + __DOT__ + 's 1, 2 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("8_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("9_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__NUMBER__ + ' 9,' + __DOT__ + 's 2 ' + __AND__ + ' 4.', lang=__LANGUAGE__)
        tts.save("9_" + __LANGUAGE__ + ".mp3")
    if not os.path.isfile("0_" + __LANGUAGE__ + ".mp3"):
        tts = gTTS(text=__NUMBER__ + ' 0,' + __DOT__ + 's 2, 4 ' + __AND__ + ' 5.', lang=__LANGUAGE__)
        tts.save("0_" + __LANGUAGE__ + ".mp3")

else:
    print("This procedure requires a internet conneciont.")
