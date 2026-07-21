"""
Sensor driver wrappers for the Rural IoT Medical Dispatcher.
Target: Raspberry Pi Pico W, MicroPython.

Replace pin numbers with your actual wiring before use.
"""

from machine import Pin, ADC, I2C
import time

# ---------------- Pulse Sensor (Heart Rate) ----------------
PULSE_PIN = 26  # ADC0

def read_pulse_raw():
    """Return a raw ADC reading (0-65535) from the pulse sensor."""
    adc = ADC(Pin(PULSE_PIN))
    return adc.read_u16()


def estimate_bpm(sample_seconds=10):
    """
    Very basic peak-counting BPM estimate.
    For production use, replace with a proper PPG peak-detection algorithm.
    """
    adc = ADC(Pin(PULSE_PIN))
    threshold = 40000  # calibrate for your sensor/hardware
    peaks = 0
    above = False
    start = time.ticks_ms()

    while time.ticks_diff(time.ticks_ms(), start) < sample_seconds * 1000:
        val = adc.read_u16()
        if val > threshold and not above:
            peaks += 1
            above = True
        elif val <= threshold:
            above = False
        time.sleep_ms(5)

    return int(peaks * (60 / sample_seconds))


# ---------------- Temperature Sensor (MLX90614, I2C) ----------------
MLX90614_ADDR = 0x5A
MLX90614_TOBJ1 = 0x07

def read_object_temperature(i2c):
    """Read object temperature in Celsius from an MLX90614 over I2C."""
    data = i2c.readfrom_mem(MLX90614_ADDR, MLX90614_TOBJ1, 3)
    raw = data[0] | (data[1] << 8)
    temp_c = raw * 0.02 - 273.15
    return round(temp_c, 1)


# ---------------- Ultrasonic Sensor (HC-SR04) ----------------
TRIG_PIN = 15
ECHO_PIN = 14

def read_distance_cm():
    trig = Pin(TRIG_PIN, Pin.OUT)
    echo = Pin(ECHO_PIN, Pin.IN)

    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()

    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()

    duration = time.ticks_diff(pulse_end, pulse_start)
    distance = (duration * 0.0343) / 2  # speed of sound in cm/us
    return round(distance, 1)
