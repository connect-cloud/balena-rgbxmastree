from time import sleep
from tree import RGBXmasTree
from colorzero import Color
import random
import os
import signal


BRIGHTNESS = os.environ["BRIGHTNESS"] if "BRIGHTNESS" in os.environ else 0.08
DELAY = os.environ["DELAY"] if "DELAY" in os.environ else 0.5

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


if __name__ == "__main__":
    killer = GracefulKiller()
    while not killer.kill_now:
        sleep(DELAY)
        pixel = random.choice(tree)
        pixel.color = random_color()

    print("KB interrupt received")
    tree.off()
    tree.close()


