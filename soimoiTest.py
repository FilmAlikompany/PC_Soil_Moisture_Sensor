# 応用演習(PC)第１２回授業内に作成
# 2020/12/10

from time import sleep
from gpiozero import LED
import RPi.GPIO as GPIO
import time

relay_pin = 17
LED(relay_pin, active_high=False)

def main_loop():
    while True:
        sleep(2)
        GPIO.setup(relay_pin, GPIO.OUT)


if __name__ == "__main__":
    main_loop()
