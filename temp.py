import time
import board
import adafruit_dht

dht = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            temperature = dht.temperature
            humidity = dht.humidity

            if temperature is not None and humidity is not None:
                print(f"Temperature: {temperature}°C")
                print(f"Humidity: {humidity}%")
            else:
                print("Failed to retrieve data from DHT11")

        except RuntimeError as error:
            # DHT11 常會短暫讀取失敗，忽略即可
            print(error.args[0])

        time.sleep(2)

except KeyboardInterrupt:
    print("Stopping...")
finally:
    dht.exit()