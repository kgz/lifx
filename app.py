import sys
from time import sleep

from lifxlan import RED, ORANGE, YELLOW,GREEN, CYAN, BLUE, PURPLE, PINK, LifxLAN
import random
c = [RED, ORANGE, YELLOW,GREEN, CYAN, BLUE, PURPLE, PINK]

LEN = 3

lan = LifxLAN(LEN)
original_powers = lan.get_power_all_lights()

for light in original_powers:
    light.set_power(original_powers[light])

while 1:
    for x in range(LEN):
        lan.get_lights()[x].set_color(random.choice(c), rapid=0)
        # sleep(0.5)

    sleep(0.2)
  