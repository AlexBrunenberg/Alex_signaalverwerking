from gpiozero import LEDBoard
import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP)
dhtDevice = adafruit_dht.DHT11(board.D18)
sensor = W1ThermSensor()
leds = LEDBoard(13,17,27,22,10,9,5,6)


temperature_c = dhtDevice.temperature
humidity = dhtDevice.humidity
temperature_in_celcius = sensor.get_temperature()

temperatuur = (temperature_in_celcius + temperature_c) /2


while True:
    try:
        temperature_c = dhtDevice.temperature
        temperature_in_celcius = sensor.get_temperature()
        temperatuur = (temperature_in_celcius + temperature_c) /2
        print(f"temp DS18B20: {temperature_in_celcius}°C")
        print(f"Temp DHT11: {temperature_c:.1f}°C")
        print("temperatuur:",temperatuur )
        teller = 0
        for temp in range(0, 35, 5):
            if int(temperatuur) >= temp:
                leds[teller].on()
            else:
                leds[teller].off()
            teller += 1
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)