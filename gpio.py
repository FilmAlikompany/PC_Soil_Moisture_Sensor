from time import sleep
import RPi.GPIO as GPIO
import spidev
import time
import sys
from gpiozero import LED
import requests
import os

GPIO.setmode(GPIO.BCM)

api_key = 'CRIL0P4LSC9Y6B58'
url = 'https://api.thingspeak.com/update'

relay_pin = 16
GPIO.setup(relay_pin, GPIO.OUT)

signal_pin = LED(relay_pin, active_high=False)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def send_data(humidity):
    response = requests.get(url,
    params={
        'api_key': api_key,
        'field1': humidity
    })
    print(response.json)

def main_loop():
    print("PROGRAM START")
    while True:
        resp = spi.xfer2([0x68, 0x00])
        volume = ((resp[0] << 8) + resp[1]) & 0x3FF

        if volume >= 650:
            print("above 650")
            GPIO.output(relay_pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(relay_pin, GPIO.LOW)
        else:
            print("under 650")
            GPIO.output(relay_pin, GPIO.LOW)

        send_data(volume)
        time.sleep(5)

    GPIO.cleanup(relay_pin)
