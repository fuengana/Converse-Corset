# 💡 Converse Corset Top — Reactive Light-Up Design  

This project transforms a Converse-inspired corset top into an interactive, light-reactive wearable using the **Adafruit Circuit Playground Express (CPX)**.  
The onboard light sensor and NeoPixels make the corset glow dynamically in a rainbow sequence that responds to ambient light levels.  

---

## 🖼️ Design Overview  

### Digital Mockup  
![Converse Corset Digital Mockup](ConverseCorset.gif)

### Final Prototype  
![Converse Corset Prototype](ConverseCorset.png)

---

## ✨ Features
- **Ambient Light Reactivity:** Uses the CPX light sensor to detect brightness and translate it into colorful light patterns.  
- **Dynamic Lighting:** NeoPixels cycle through a rainbow palette, lighting up more LEDs as the environment gets brighter.  
- **Sound Feedback:** Each brightness level triggers a short tone for a synesthetic light–sound experience.  
- **Wearable Art:** Designed to integrate into a **Converse corset top**, merging fashion and tech expression.  

---

## 🎨 Design Background  
The corset reimagines the classic **Converse sneaker** form as a wearable interface — a piece of clothing that lights up and reacts to its surroundings.  
Each LED becomes a “lace eyelet,” turning an iconic streetwear symbol into a living, responsive canvas.  
The project explores how **fashion, interactivity, and embodiment** can converge to create playful, expressive technology.  

---

## 🧵 Hardware Requirements
- [Adafruit Circuit Playground Express (CPX)](https://www.adafruit.com/product/3333)  
- Power source (USB battery pack or LiPo battery)  
- Conductive thread or wires for integration into the corset  
- Optional: diffuser material to soften the LED glow  

---

## 🧠 How It Works
1. The CPX’s **light sensor** reads the ambient brightness.  
2. The sensor value (`cpx.light`) determines how many of the **10 NeoPixels** light up (`light % 10`).  
3. Each active pixel glows in a different color from a **rainbow gradient**.  
4. The CPX also plays a short **tone** whose pitch changes with brightness.  
5. The sequence repeats continuously, creating a real-time reactive lighting effect.  

---

## 🧩 Code Overview

### Main Script
```python
from adafruit_circuitplayground.express import cpx
import time

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
    if n < 0 or n > 9:
        print("Please provide an indexing number between 0~9")
    else:
        for i in range(n):
            cpx.pixels[i] = rainbow[i]
            time.sleep(0.05)
        cpx.pixels.fill(0x000000)

while True:
    light = cpx.light
    light_on(light % 10)
    cpx.play_tone(light * 10, 0.05)
```

---

## ⚙️ Setup Instructions
1. **Install CircuitPython** on your Adafruit CPX.  
   - Follow Adafruit’s setup guide: [Install CircuitPython on CPX](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart).  
2. **Copy this file** to your CPX as `code.py`.  
3. **Connect the CPX** to your corset using conductive thread or secure wiring.  
4. **Power up** your corset with a battery pack and watch it respond to light.  

---

## 🎨 Customization Ideas
- Modify the `rainbow` color list to create your own color schemes.  
- Adjust `time.sleep()` for faster or slower animations.  
- Replace the light sensor with **touch** or **motion** input for new types of interactivity.  
- Use semi-transparent fabric or mesh overlays to diffuse LED light.  

---

## ⚠️ Safety Notes
- Be cautious of **heat** and **power safety** when incorporating electronics into fabric.  
- Ensure all conductive threads or wires are **insulated** from skin contact.  
- Always test your circuit before sewing or attaching permanently.  

---

## 👩🏽‍🎨 Author
**Fuen Gana**  
*Interactive + Wearable Product Designer*  
Exploring the intersection of **fashion, technology, and embodied experience.**
