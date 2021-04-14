import paho.mqtt.client as mqtt
import json
import RPi.GPIO as GPIO
import time

MQTT_SERVER = "192.168.1.210"
MQTT_PATH = "LED"
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
start = time.time()

def on_connect(client, userdata, flags, rc):
    print("Connected. Result code: "+ str(rc))
    client.subscribe(MQTT_PATH)


#the on_message function runs once a message is received from the broker
def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    print("message received: " + msg.payload)
    received_json = json.loads(msg.payload) #convert the string to json object
    if "Done" in received_json:
        client.disconnect()
        end = time.time()
        print("led subscriber connection closing. Total time running: " + end)
    else:
        led_1_status = received_json["LED_1"]
        led_1_gpio = received_json["GPIO"]
        GPIO.setup(led_1_gpio, GPIO.OUT)
        if led_1_status:
            GPIO.output(led_1_gpio, GPIO.HIGH)
        else:
            GPIO.output(led_1_gpio, GPIO.LOW)
        print("Pi LED updated")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect(MQTT_SERVER, 1883, 60)
client.loop_forever()