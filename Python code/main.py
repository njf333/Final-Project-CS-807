import serial
import pyautogui
import screen_brightness_control as sbc

#Make sure to change com3 to your device's port number
arduinoSerial = serial.Serial("com3", 9600)

while True:
    brightness = sbc.get_brightness(display=0)[0]
    data = str(arduinoSerial.readline())
    print(data)
    if "VOLUME_UP" in data:
        pyautogui.press("volumeup")
    if "VOLUME_DOWN" in data:
        pyautogui.press("volumedown")
    if "BRIGHTNESS_UP" in data:
        if brightness <100:
            brightness += 20
        sbc.set_brightness(brightness, display=0)
    if "BRIGHTNESS_DOWN" in data:
        if brightness > 0:
            brightness -= 20
        sbc.set_brightness(brightness, display=0)