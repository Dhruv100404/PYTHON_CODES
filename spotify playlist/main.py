import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller

keyboard = Controller()
msg = []
for i in range(0, 10):
    msg.append("Hi")


def send_whatsapp_message(msg: list):


    try:

            pywhatkit.sendwhatmsg_instantly(
                phone_no="+919426544658",
                message=msg,
                tab_close=True
            )
            time.sleep(10)
            pyautogui.click()
            time.sleep(2)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            print("Message sent!")
    except Exception as e:
        print(str(e))



if __name__ == "__main__":

    send_whatsapp_message(msg)
