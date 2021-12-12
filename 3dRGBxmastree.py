from time import sleep
from datetime import datetime
from tree import RGBXmasTree
from colorzero import Color
import random
import os
import signal


BRIGHTNESS = (int(os.environ["BRIGHTNESS"])/100) if "BRIGHTNESS" in os.environ else 0.08
DELAY = float(os.environ["DELAY"]) if "DELAY" in os.environ else 0.5
STARTTIME = os.environ["STARTTIME"] if "STARTTIME" in os.environ else "0000"
STOPTIME = os.environ["STOPTIME"] if "STOPTIME" in os.environ else "2359"

tree = RGBXmasTree(brightness=BRIGHTNESS)


def random_color():
    colors = [Color('red'), Color('green'), Color('blue'), Color('yellow'), Color('purple')]
    color = random.choice(colors)
    return color


class GracefulKiller:
  kill_now = False
  signals = {
    signal.SIGINT: 'SIGINT',
    signal.SIGTERM: 'SIGTERM'
  }

  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self, signum, frame):
    print("\nReceived {} signal".format(self.signals[signum]))
    print("Cleaning up resources. End of the program")
    self.kill_now = True
    tree.off()
    tree.close()
    quit()


if __name__ == "__main__":
    # Initial color the tree
    for pixel in tree:
        pixel.color = random_color()
    
    killer = GracefulKiller()
    while not killer.kill_now:
        now = datetime.now().strftime("%H%M")
        if now >= STARTTIME and now < STOPTIME:
            pixel = random.choice(tree)
            pixel.color = random_color()
            sleep(DELAY)
        else:
            tree.off()
            sleep(60)
