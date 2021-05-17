import time
import board
import adafruit_dht
import paho.mqtt.publish as publish
import json
import sys

start = time.time()
startDht = time.time()
endDht = time.time()
humidity = 0
temperature = 0

MQTT_SERVER = sys.argv[1]

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)
count = 0
while count < 10000:
    try:
        endDht = time.time()
        if(humidity == 0 and temperature == 0) or (endDht-startDht) > 1:
            humidity = dhtDevice.humidity # Get current humidity from dht11
            temperature = dhtDevice.temperature # Get current temperature from dht11
            startDht = time.time()
        hum_json = {"Humidity": humidity, "Unit": "%"}
        publish.single("Humidity", json.dumps(hum_json), hostname=MQTT_SERVER)
        temp_json = {"Temp": temperature, "Unit": "C"}
        publish.single("Temperature", json.dumps(temp_json), hostname=MQTT_SERVER)
        count += 1
    except RuntimeError as error:  # Errors happen fairly often, DHT's are hard to read, just keep going
        error.args[0]

publish.single("Humidity", json.dumps({"Done": True}), port=1883, hostname=MQTT_SERVER)
publish.single("Temperature", json.dumps({"Done": True}), port=1883, hostname=MQTT_SERVER)
end = time.time()
print("Humidity and temperature runtime = " + str(end-start))
with open("piResultsPython.txt", "a") as myfile:
    myfile.write("Humidity and temperature publisher runtime = " + str(end-start) + "\n")
