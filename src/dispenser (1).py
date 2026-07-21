"""
Rural IoT: Automatic Medical Dispatcher — main control loop
Target: Raspberry Pi Pico W, MicroPython

This is a scaffold reconstructed from the published paper's design.
Fill in your Wi-Fi credentials, server endpoint, and OLED driver of choice
(e.g. ssd1306) before deploying.
"""

import network
import time
from machine import I2C, Pin
import sensors
import dispenser

# ---- Configuration ----
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
SERVER_URL = "http://your-server.example.com/api/vitals"

I2C_SDA = 0
I2C_SCL = 1


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    timeout = 15
    while not wlan.isconnected() and timeout > 0:
        time.sleep(1)
        timeout -= 1

    if wlan.isconnected():
        print("Connected:", wlan.ifconfig())
    else:
        print("Wi-Fi connection failed")

    return wlan.isconnected()


def read_all_vitals(i2c):
    return {
        "heart_rate_bpm": sensors.estimate_bpm(sample_seconds=5),
        "temperature_c": sensors.read_object_temperature(i2c),
        "distance_cm": sensors.read_distance_cm(),
    }


def main():
    connect_wifi()
    i2c = I2C(0, sda=Pin(I2C_SDA), scl=Pin(I2C_SCL), freq=100000)

    while True:
        vitals = read_all_vitals(i2c)
        print("Vitals:", vitals)

        # TODO: send `vitals` to SERVER_URL for the remote doctor to review
        # TODO: update OLED display with current readings

        # Example emergency check (tune thresholds to real clinical guidance)
        if vitals["heart_rate_bpm"] > 120 or vitals["heart_rate_bpm"] < 40:
            dispenser.sound_alert(beeps=3)
            # TODO: trigger emergency alert to nearest facility with location

        time.sleep(5)


if __name__ == "__main__":
    main()
