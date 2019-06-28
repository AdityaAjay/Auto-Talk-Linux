#!/usr/bin/python
import time, audioop, alsaaudio, pyautogui as pg

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK)

inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

inp.setperiodsize(160)



def press(keys, presses=1):
    if type(keys) == str:
        keys = [keys]
    else:
        lowerKeys = []
        for s in keys:
            if len(s) > 1:
                lowerKeys.append(s.lower())
            else:
                lowerKeys.append(s)
    for i in range(presses):
        for k in keys:
            pg._failSafeCheck()
            pg.platformModule._keyDown(k)
            pg.platformModule._keyUp(k)


while True:
    l, data = inp.read()
    if l:
        #print(audioop.max(data, 2))
        val = audioop.max(data, 2)
        if val > 17000:
            for j in range(50):
                press('k')
    time.sleep(.001)
