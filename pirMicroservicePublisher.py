import time
import paho.mqtt.publish as publish
import json
from gpiozero import MotionSensor

pir = MotionSensor(17)

MQTT_SERVER = "192.168.1.210"
MQTT_PATH = "PIR"

#Initial the pir device, with data pin connected to 17:
pir = MotionSensor(17)
presence = False

count = 0
while count<20:
    try:
         # Print the values to the serial port
         newPresence = pir.motion_detected()
         if newPresence != presence:
             presence = newPresence
             temp_json = {"PIR": presence}
             publish.single(MQTT_PATH, json.dumps(temp_json), port=1883, hostname=MQTT_SERVER)

    except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
         print(error.args[0])
    count += 1
    time.sleep(5)

    #test