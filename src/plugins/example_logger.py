import time

from boatd import BasePlugin

class ExamplePlugin(BasePlugin):
    def main(self):
        while self.running:
            position = self.boatd.boat.position()
            print('ExamplePlugin: logging some stuff ', position)
            time.sleep(5)

plugin = ExamplePlugin