import time
import paho.mqtt.publish as publish
import json
from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import sys

MQTT_SERVER = sys.argv[1]
MQTT_PATH = "PIR"

#Initial the pir device, with data pin connected to 17:
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
#pir = MotionSensor(17)
presence = False

count = 0
while count<20:
    try:
         # Print the values to the serial port
         newPresence = GPIO.input(17)
         if newPresence != presence:
             presence = newPresence
             temp_json = {"PIR": presence}
             publish.single(MQTT_PATH, json.dumps(temp_json), port=1883, hostname=MQTT_SERVER)
             print("PIR reading sent")

    except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
         print(error.args[0])
    count += 1
    time.sleep(5)

    #test