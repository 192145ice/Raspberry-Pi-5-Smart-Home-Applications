from gpiozero import DigitalInputDevice, PWMOutputDevice, LED
from time import sleep
import board
import adafruit_dht

# -----------------------------
# 腳位設定
# -----------------------------
LDR_PIN = 17      # 光敏模組 DO
LED_PIN = 27      # LED
FAN_PIN = 18      # 風扇 PWM (GPIO18)
DHT_PIN = board.D4  # DHT11

# -----------------------------
# 裝置初始化
# -----------------------------
ldr = DigitalInputDevice(LDR_PIN)
led = LED(LED_PIN)
fan = PWMOutputDevice(FAN_PIN, frequency=1000)
dht = adafruit_dht.DHT11(DHT_PIN)

print("System started...")

try:
    while True:
        # =============================
        # 光敏電阻 → LED 控制
        # =============================
        if not ldr.value:  # 亮
            print("Bright environment 🌞 → LED OFF")
            led.off()
        else:  # 暗
            print("Dark environment 🌑 → LED ON")
            led.on()

        # =============================
        # DHT11 → 風扇控制
        # =============================
        try:
            temperature = dht.temperature
            # temperature = 20
            humidity = dht.humidity

            if temperature is not None:
                print(f"Temperature: {temperature}°C")
                print(f"Humidity: {humidity}%")

                # 溫度對應風扇速度
                if temperature < 25:
                    fan.value = 1.0      # 停止
                elif temperature < 27:
                    fan.value = 0.7
                elif temperature < 30:
                    fan.value = 0.4
                else:
                    fan.value = 0.0      # 全速

                real_speed = 1.0 - fan.value
                print(f"Fan speed: {int(real_speed * 100)}%")

            else:
                print("Failed to retrieve DHT11 data")

        except RuntimeError as error:
            print("DHT error:", error.args[0])

        print("-" * 30)
        sleep(2)

except KeyboardInterrupt:
    print("Stopping program...")

finally:
    fan.value = 0
    led.off()
    dht.exit()
