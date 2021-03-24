import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
import Adafruit_DHT

sensor = 22 # might need to be changed depending on the pi setup
pin = 12 # might need to be changed depending on the pi setup
print("trying..")
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)  # Not doing anything...
print(humidity)
print(temperature)

# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
#
# while True: # Run forever
#  GPIO.output(8, GPIO.HIGH) # Turn on
#  sleep(1) # Sleep for 1 second
#  GPIO.output(8, GPIO.LOW) # Turn off
#  sleep(1) # Sleep for 1 second