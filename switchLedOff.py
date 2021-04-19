import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

action = sys.argv[1]
pin = int(sys.argv[1])

GPIO.setup(pin, GPIO.OUT)
if action == "on":
    GPIO.output(pin, GPIO.HIGH)
else:
    GPIO.output(pin, GPIO.LOW)