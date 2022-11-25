from picographics import PicoGraphics, DISPLAY_INKY_PACK
from network_manager import NetworkManager
import WIFI_CONFIG
import uasyncio
import gc


BUTTON_UP = 15
BUTTON_DOWN = 11
BUTTON_A = 12
BUTTON_B = 13
BUTTON_C = 14


class Badger2040W():
    def __init__(self):
        self.display = PicoGraphics(DISPLAY_INKY_PACK)

    def __getattr__(self, item):
        # Glue to redirect calls to PicoGraphics
        if item in dir(self.display):
            return getattr(self.display, item)
        else:
            return getattr(self, item)

    def status_handler(self, mode, status, ip):
        print(mode, status, ip)
        self.display.set_pen(15)
        self.display.clear()
        self.display.set_pen(0)
        if status:
            self.display.text("Connected!", 10, 10, 300, 0.5)
            self.display.text(ip, 10, 30, 300, 0.5)
        else:
            self.display.text("Connecting...", 10, 10, 300, 0.5)
        self.display.update()

    def connect(self):
        self.display.set_update_speed(2)
        network_manager = NetworkManager(WIFI_CONFIG.COUNTRY, status_handler=self.status_handler)
        uasyncio.get_event_loop().run_until_complete(network_manager.client(WIFI_CONFIG.SSID, WIFI_CONFIG.PSK))
        gc.collect()
