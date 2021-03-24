import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11 # might need to be changed depending on the pi setup
DHT_PIN = 4 # might need to be changed depending on the pi setup
# print("trying..")
# humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)  # Not doing anything...
# print(humidity)
# print(temperature)

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(3);

# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
#
# while True: # Run forever
#  GPIO.output(8, GPIO.HIGH) # Turn on
#  sleep(1) # Sleep for 1 second
#  GPIO.output(8, GPIO.LOW) # Turn off
#  sleep(1) # Sleep for 1 second