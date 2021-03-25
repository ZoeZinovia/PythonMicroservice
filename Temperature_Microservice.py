import time
import board
import adafruit_dht
import paho.mqtt.publish as publish
import json

MQTT_SERVER = "192.168.1.210"
MQTT_PATH = "Temperature"

#Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)

count = 0
while count<20:
    try:
         # Print the values to the serial port
         temperature = dhtDevice.temperature
         humidity = dhtDevice.humidity
         message = str('{Temp: {:.2f}}'
               .format(temperature))
         publish.single(MQTT_PATH, message, hostname=MQTT_SERVER)

    except RuntimeError as error:     # Errors happen fairly often, DHT's are hard to read, just keep going
         print(error.args[0])
    count += 1
    time.sleep(5)