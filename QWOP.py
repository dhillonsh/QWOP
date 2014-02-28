import win32com.client, win32api, win32con
from threading import Thread
from time import sleep
from random import uniform
moveList = {
    'o':0x4F,
    'p':0x50,
    'q':0x51,
    'w':0x57,
}

def clickKey(key):
    while(True):
        sleepTime = uniform(0,1)
        print("Pressing " + key + " for " + str(sleepTime) + " seconds")
        win32api.keybd_event(moveList[key], 0, 0,0)
        sleep(sleepTime)
        win32api.keybd_event(moveList[key],0 ,win32con.KEYEVENTF_KEYUP,0)

def restart():
    while(True):
        win32api.keybd_event(0x20, 0, 0,0)
        win32api.keybd_event(0x20,0 ,win32con.KEYEVENTF_KEYUP,0)
        sleep(5)

for (key,val) in moveList.items():
    key = Thread(target=clickKey, args=[key])
    key.start()

restart = Thread(target=restart, args=[])
restart.start()
