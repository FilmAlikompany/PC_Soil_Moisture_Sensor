from time import sleep
import RPi.GPIO as GPIO
import spidev
import time
import sys
from gpiozero import Button, LED
import requests
#from flask import Flask, render_template

GPIO.setmode(GPIO.BCM)
#button = Button(26, bounce_time=0.05)

api_key = ''
url = ''

relay_pin = 16
GPIO.setup(relay_pin, GPIO.OUT)

signal_pin = LED(relay_pin, active_high=False)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

#parm = 0
#det = ""

#app = Flask(__name__)

def send_data(humidity):
    response = requests.get(url,
    params={
        'api_key': api_key,
        'field1': humidity
    })
    print(response.json)

@app.route('/')
def main_loop():
    #global parm
    print("PROGRAM START")
    while True:
        resp = spi.xfer2([0x68, 0x00])
        volume = ((resp[0] << 8) + resp[1]) & 0x3FF

        if volume >= 650:
            print("above 650 : " + str(volume))
            #parm = 0
            GPIO.output(relay_pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(relay_pin, GPIO.LOW)
        else:
            print("under 650 : " + str(volume))
            #parm = 1
            GPIO.output(relay_pin, GPIO.LOW)

        """
        if parm == 0:
            det = "鉢の土がが乾いているようです"
        elif parm == 1:
            det = "鉢の土は湿っています"
        """

        send_data(volume)
        time.sleep(5)
    
    GPIO.cleanup(relay_pin)
    #return render_template('index.html', planter = det)


if __name__ == "__main__":
    #app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
    main_loop()
