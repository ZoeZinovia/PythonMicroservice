import time
import board
import adafruit_dht
import paho.mqtt.publish as publish
import json
import sys

MQTT_SERVER = sys.argv[1]
MQTT_PATH = "Humidity"

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D12)
humidity = 0
temperature = 0;
count = 0
while count < 20:
    try:
        # Print the values to the serial port
        newHumidity = dhtDevice.humidity
        newTemperature = dhtDevice.temperature
        if newHumidity != humidity:
            humidity = newHumidity
            hum_json = {"Humidity": humidity, "Unit": "%"}
            publish.single("Humidity", json.dumps(hum_json), hostname=MQTT_SERVER)
            print("Humidity reading sent")

        if newTemperature != temperature:
            temperature = newTemperature
            temp_json = {"Temp": temperature, "Unit": "C"}
            publish.single("Temperature", json.dumps(temp_json), hostname=MQTT_SERVER)
            print("Temperature reading sent")

    except RuntimeError as error:  # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
    count += 1
    time.sleep(5)
