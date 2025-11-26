import busio, digitalio, board, time    # importeer modules
import adafruit_mcp3xxx.mcp3008 as MCP  # importeer module
from adafruit_mcp3xxx.analog_in import AnalogIn # importeer een module
from gpiozero import RGBLED # importeer een module
spi = busio.SPI(clock=board.SCK,MISO=board.MISO,MOSI=board.MOSI)    # laat zien waar de clock, miso en mosi op het bord zitten in variabele spi
cs = digitalio.DigitalInOut(board.D5)   # sluit het aan op digitale pin 5
mcp = MCP.MCP3008(spi, cs)  # zet alle aansluitingen in variabele mcp
channel1 = AnalogIn(mcp, MCP.P0)    # zet de waarde van channel0 in variabele channel1
channel2 = AnalogIn(mcp, MCP.P1)    # zet de waarde van channel1 in variabele channel2
channel3 = AnalogIn(mcp, MCP.P2)    # zet de waarde van channel2 in variabele channel3
led = RGBLED(red = 17, green = 27, blue = 22)   # sluit de rgb led aan op pinnen 17, 27, 22

while True: # blijf altijd doen
    channelValue1 = channel1.value / 65535  # zet de waarde van de eerste potmeter tussen 0 en 1 en zet het in variabele channelValue1
    channelValue2 = channel2.value / 65535  # zet de waarde van de tweede potmeter tussen 0 en 1 en zet het in variabele channelValue2
    channelValue3 = channel3.value / 65535  # zet de waarde van de derde potmeter tussen 0 en 1 en zet het in variabele channelValue3
    led.color = (channelValue1, channelValue2, channelValue3)   # zet de 3 waardes van de potmeters in de rgb led
    time.sleep(0.5) # wacht een halve seconde