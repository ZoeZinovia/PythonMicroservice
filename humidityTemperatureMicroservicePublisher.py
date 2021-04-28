import time
import board
import adafruit_dht
import paho.mqtt.publish as publish
import json
import sys

start = time.time()

MQTT_SERVER = sys.argv[1]

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D4)
humidity = 0
temperature = 0;
count = 0
while count < 100:
        # Print the values to the serial port
        newHumidity = dhtDevice.humidity
        newTemperature = dhtDevice.temperature
        # if newHumidity != humidity:
        humidity = newHumidity
        hum_json = {"Humidity": humidity, "Unit": "%"}
        publish.single("Humidity", json.dumps(hum_json), hostname=MQTT_SERVER)
        time.sleep(0.2)
        # if newTemperature != temperature:
        temperature = newTemperature
        temp_json = {"Temp": temperature, "Unit": "C"}
        publish.single("Temperature", json.dumps(temp_json), hostname=MQTT_SERVER)
        count += 1
    # time.sleep(0.2)

publish.single("Humidity", json.dumps({"Done": True}), port=1883, hostname=MQTT_SERVER)
publish.single("Temperature", json.dumps({"Done": True}), port=1883, hostname=MQTT_SERVER)
end = time.time()
print("Humidity and temperature runtime = " + str(end-start))
with open("piResultsPython.txt", "a") as myfile:
    myfile.write("Humidity and temperature publisher runtime = " + str(end-start) + "\n")
