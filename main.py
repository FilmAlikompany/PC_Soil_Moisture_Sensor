from time import sleep
import RPi.GPIO as GPIO
import spidev
import time
import sys
from gpiozero import LED
GPIO.setmode(GPIO.BCM)

relay_pin = 16
GPIO.setup(relay_pin, GPIO.OUT)

signal_pin = LED(relay_pin, active_high=False)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def main_loop():
    print("PROGRAM START")
    while True:
        resp = spi.xfer2([0x68, 0x00])
        volume = ((resp[0] << 8) + resp[1]) & 0x3FF
        
        if volume >= 650:
            print("650     ^j")
            GPIO.output(relay_pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(relay_pin, GPIO.LOW)
        else:
            print("650 ^|   ^`")
            GPIO.output(relay_pin, GPIO.LOW)
        time.sleep(5)

    GPIO.cleanup(relay_pin)

if __name__ == "__main__":
    main_loop()
