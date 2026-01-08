import board, time,adafruit_dht # importeer modules
from gpiozero import RGBLED, PWMLED # importeer modules

led = RGBLED(red = PWMLED(9), green = PWMLED(10), blue = PWMLED(11)) # definieer de LED
dhtDevice = adafruit_dht.DHT11(board.D18)   #verbind de dht11 op pin 18 en noem het dhtDevice
lijst = [[255,0,0],[205,38,38],[205,55,0],[250,128,114],[238,149,114],[255,127,0],[205,133,0]]
lijst = [255,0,0 

205,38,38 

205,55,0 

250,128,114 

238,149,114 

255,127,0 

205,133,0 

238,173,14 

238,221,130 

205,205,0 

255,246,143 

124,252,0 

0,255,0 

78,238,148 

0,245,255 

151,255,255 

0,255,255 

135,206,250 

0,191,255 

30,144,255 

0,0,255 ]

while True:
    temperatuur = dhtDevice.temperature
    lijstNummer = map(temperatuur, 0, 40, 0, 20)
    print(f"Temp: {temperatuur}°C")
    led.color = (rood, 0, blauw)   # zet de 3 waardes van de potmeters in de rgb led
    time.sleep(2)
