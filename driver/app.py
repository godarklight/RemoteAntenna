import gpiod
import sys
import time
from datetime import datetime

chip = gpiod.chip("/dev/gpiochip1")
antenna = chip.get_line(8)

config = gpiod.line_request()
config.consumer = "Antenna"
config.request_type = gpiod.line_request.DIRECTION_OUTPUT

antenna.request(config)

print(antenna.consumer)

lastValue = ""

while True:
    f = open("../website/antenna.txt")
    selectedAntenna = f.readlines()[0]
    f.close()
    if (selectedAntenna != lastValue):
        lastValue = selectedAntenna
        print("Switch to " + selectedAntenna + " at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if (selectedAntenna == "ocf"):
            antenna.set_value(1)
        if (selectedAntenna == "vertical"):
            antenna.set_value(0)
    time.sleep(0.1)

print("Done!")
