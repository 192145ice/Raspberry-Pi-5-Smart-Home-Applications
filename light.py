from gpiozero import DigitalInputDevice, PWMOutputDevice, LED
from time import sleep

# 光敏模組 DO 腳
ldr = DigitalInputDevice(17)

# # LED 控制
led = LED(27)

while True:
    if not ldr.value:  # 高電位 → 亮
        print("Bright environment 🌞")
        led.off()
    else:  # 低電位 → 暗
        print("Dark environment 🌑")
        led.on()
    sleep(0.5)


