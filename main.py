import time
import RPi.GPIO as GPIO
import os
import gpio

GPIO.setmode(GPIO.BCM)
#GPIO18pinを入力モードとし、pull up設定とします
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def main_loop():
    while True:
        GPIO.wait_for_edge(18, GPIO.FALLING)
        sw_counter = 0
        gpio.main_loop()

        while True:
            sw_status = GPIO.input(18)
            if sw_status == 0:
                sw_counter = sw_counter + 1
                if sw_counter >= 50:
                    print("長押し検知！")
                    os.system("sudo shutdown -h now")
                    break
            else:
                print("短押し検知")
                break

            time.sleep(0.01)

        print(sw_counter)


if __name__ == "__main__":
    main_loop()
