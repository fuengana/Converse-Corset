from machine import Pin, ADC
import neopixel
import time

# --- Configuration ---
NUM_PIXELS = 10           # Number of LEDs
PIXEL_PIN = 5             # Change to your NeoPixel data pin
LIGHT_SENSOR_PIN = 34     # Change based on your board's analog input pin

# Initialize NeoPixels and light sensor
np = neopixel.NeoPixel(Pin(PIXEL_PIN), NUM_PIXELS)
light_sensor = ADC(Pin(LIGHT_SENSOR_PIN))
light_sensor.atten(ADC.ATTN_11DB)  # Full 0–3.3V range

# Rainbow color palette
rainbow = [
    0xFFF100,
    0xFF8C00,
    0xE81123,
    0xEC008C,
    0x68217A,
    0x00188F,
    0x00BCF2,
    0x00B294,
    0x009E49,
    0xBAD80A,
]

def light_on(n):
    '''Light up n LEDs in rainbow sequence.'''
    if n < 0 or n > NUM_PIXELS:
        print("Please provide an indexing number between 0–9")
        return
    for i in range(n):
        color = rainbow[i % len(rainbow)]
        r = (color >> 16) & 0xFF
        g = (color >> 8) & 0xFF
        b = color & 0xFF
        np[i] = (r, g, b)
        np.write()
        time.sleep(0.05)
    np.fill((0, 0, 0))
    np.write()

while True:
    light_value = light_sensor.read()  # 0–4095
    n = (light_value // 400) % NUM_PIXELS
    light_on(n)
    time.sleep(0.05)
