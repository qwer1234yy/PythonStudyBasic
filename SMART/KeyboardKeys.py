#encoding=utf-8
import win32api
import win32con

class KeyboardKeys(object):
    #模拟键盘按键类
    VK_CODE={
        'enter':0x0D,
        'ctrl':0x11,
        'v':0x56,
    'shift':0x10}

    @staticmethod
    def keyDown(keyName):
        #按下按键
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName],0,0,0)

    @staticmethod
    def keyUp(keyName):
        #释放按键
        win32api.keybd_event(KeyboardKeys.VK_CODE[keyName],0,win32con.KEYEVENTF_KEYUP,0)

    @staticmethod
    def oneKey(key):#对前两个方法的调用
        #模拟单个按键
        KeyboardKeys.keyDown(key)
        KeyboardKeys.keyUp(key)


    @staticmethod
    def twoKeys(key1,key2):#对前面函数的调用
        #模拟两个组合键
        KeyboardKeys.keyDown(key1)
        KeyboardKeys.keyDown(key2)
        KeyboardKeys.keyUp(key2)
        KeyboardKeys.keyUp(key1)