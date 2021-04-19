import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

action = sys.argv[1]
if action == "on":
    GPIO.output(4, GPIO.HIGH)
else:
    GPIO.output(4, GPIO.LOW)