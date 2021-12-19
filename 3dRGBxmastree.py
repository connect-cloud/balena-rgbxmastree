from time import sleep
from datetime import datetime
from tree import RGBXmasTree
from colorzero import Color
import random
import os
import signal
import requests
import urllib3

urllib3.disable_warnings() # Disable SSL warnings becaus the Hue bridge uses self signed certs



BRIGHTNESS = (int(os.environ["BRIGHTNESS"])/100) if "BRIGHTNESS" in os.environ else 0.08
DELAY = float(os.environ["DELAY"]) if "DELAY" in os.environ else 1
STARTTIME = os.environ["STARTTIME"] if "STARTTIME" in os.environ else "0000"
STOPTIME = os.environ["STOPTIME"] if "STOPTIME" in os.environ else "2359"

if "USE_HUE_LIGHT_STATUS" in os.environ:
    if os.environ["USE_HUE_LIGHT_STATUS"] == 'True':
        use_hue_light_status = True
        hue_ip = os.environ["HUE_IP"] if "HUE_IP" in os.environ else "0.0.0.0"
        hue_username = os.environ["HUE_USERNAME"] if "HUE_USERNAME" in os.environ else ""
        hue_light_name = os.environ["HUE_LIGHT_NAME"] if "HUE_LIGHT_NAME" in os.environ else ""
        if os.environ["HUE_USE_SSL"] == 'True':
            hue_base_url = f'https://{hue_ip}/api/{hue_username}'
        else:
            hue_base_url = f'http://{hue_ip}/api/{hue_username}'
    else:
        use_hue_light_status = False
else:
    use_hue_light_status = False


# Initialize the Tree
tree = RGBXmasTree(brightness=BRIGHTNESS)


def random_color():
    colors = [Color('red'), Color('green'), Color('blue'), Color('yellow'), Color('purple')]
    color = random.choice(colors)
    return color


def get_hue_lights(hue_base_url):
    hue_url = f'{hue_base_url}/lights'
    response = requests.get(hue_url, verify=False)
    return response.json()


def get_hue_light_by_name(name, hue_base_url):
    lights = get_hue_lights(hue_base_url)
    for light_id in lights:
        light_id = str(light_id) #  convert to string because in the dict the light id is a string
        if lights[light_id]['name'] == name:
            return lights[light_id]
        else:
            return False


def get_hue_light_status_by_name(name, hue_base_url):
    light = get_hue_light_by_name(name, hue_base_url)
    if light:
        if light['state']['on'] and light['state']['reachable']:
            return True
    else:
        return False


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

def color_tree(initialize_tree):
    if initialize_tree:
        for pixel in tree:
            pixel.color = random_color()
        initialize_tree = False
    pixel = random.choice(tree)
    pixel.color = random_color()
    return initialize_tree


if __name__ == "__main__":
    initialize_tree = True
    killer = GracefulKiller()
    while not killer.kill_now:
        now = datetime.now().strftime("%H%M")
        if use_hue_light_status:
            if get_hue_light_status_by_name(hue_light_name, hue_base_url):
                initialize_tree = color_tree(initialize_tree)
                sleep(DELAY)
            else:
                tree.off()
                initialize_tree = True
                sleep(5)
        elif now >= STARTTIME and now < STOPTIME:
            initialize_tree = color_tree(initialize_tree)
            sleep(DELAY)
        else:
            tree.off()
            initialize_tree = True
            sleep(60)
