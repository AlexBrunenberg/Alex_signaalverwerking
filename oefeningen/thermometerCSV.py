import time,board,adafruit_dht
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP)
dhtDevice = adafruit_dht.DHT11(board.D18)
sensor = W1ThermSensor()


temperature_c = dhtDevice.temperature
temperature_in_celcius = sensor.get_temperature()
temperatuur = (temperature_in_celcius + temperature_c) /2

f=open("thermometerCSV.csv","w")
f.write("datum,tijd,DHT11,DS18B20,gemiddeldeTemp \n")
f.close()

while True:
    if (int(time.strftime("%S"))%5) == 0:
        try:
            datum = time.strftime("%Y-%m-%d")
            tijd = time.strftime("%H:%M:%S")
            temperature_c = dhtDevice.temperature
            temperature_in_celcius = sensor.get_temperature()
            temperatuur = (temperature_in_celcius + temperature_c) /2
            print(f"Temp DHT11: {temperature_c:.1f}°C")
            print(f"temp DS18B20: {temperature_in_celcius}°C")
            print("temperatuur:",temperatuur )
            f=open("thermometerCSV.csv","a")
            f.write(f"{datum},{tijd},{temperature_c},{temperature_in_celcius},{temperatuur}\n")
            f.close()
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(2.0)