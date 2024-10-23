import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    print(volume)
    # all on loud volume 
    if (volume >= 27000) :
        for i in range(11):
             leds[i].value = 1
             sleep(0.1)

    # volume medium max
    if (volume > 22000 and volume <27000):
            for i in range(10,7,-1):
                leds[i].value = 0
                sleep(0.01)
            for i in range(9):
             leds[i].value = 1
             sleep(0.01)

    # volume medium
    if (volume > 19000 and volume <22000):
            for i in range(10,5,-1):
                leds[i].value = 0
                sleep(0.01)
            for i in range(6):
             leds[i].value = 1
             sleep(0.01)

    # volume high low
    if (volume > 10000 and volume <19000):
            for i in range(10,3,-1):
                leds[i].value = 0
                sleep(0.01)
            for i in range(4):
             leds[i].value = 1
             sleep(0.01)

    # volume low
    if (volume <10000):
            for i in range(10,2,-1):
                leds[i].value = 0
                sleep(0.01)
            for i in range(1):
             leds[i].value = 1
             sleep(0.01)


        




    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?