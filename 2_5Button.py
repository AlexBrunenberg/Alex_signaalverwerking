from gpiozero import Button
from time import sleep
     
button = Button(2)
while True:
    button.wait_for_press()
    print("Button was pressed")
    sleep(1)