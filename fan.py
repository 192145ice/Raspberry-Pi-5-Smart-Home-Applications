from gpiozero import PWMOutputDevice
from time import sleep

FAN_PIN = 18   # GPIO18 (PWM)

fan = PWMOutputDevice(FAN_PIN, frequency=1000)

# 加速
for speed in [i / 100 for i in range(100, -1, -5)]:
    fan.value = speed
    print(f"Fan speed: {int(speed*100)}%")
    sleep(0.2)

sleep(1)

# 減速
for speed in [i / 100 for i in range(0, 101, 5)]:
    fan.value = speed   # 0.0 ~ 1.0
    print(f"Fan speed: {int(speed*100)}%")
    sleep(0.2)

sleep(1)
