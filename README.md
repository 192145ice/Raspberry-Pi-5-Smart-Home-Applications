# Raspberry Pi 5 Smart Home Applications
本專題以 Raspberry Pi 為核心，整合光敏電阻、DHT11 溫溼度感測器、LED 與 PWM 風扇，實作一套智慧環境控制系統。系統在自動模式下可依環境亮度控制照明，並依溫度自動調整風扇轉速；同時也透過 LINE Bot 提供遠端監控與手動控制功能，使用者可即時查詢環境狀態或介入控制設備。

## 📁 專案架構說明

```bash
Raspberry-Pi-5-Smart-Home-Applications/
├── .env                     # LINE Bot 金鑰與環境變數設定
├── .gitattributes           
├── all.py                   # 主程式（整合 LED、風扇、感測器與 LINE Bot）
├── fan.py                   # 風扇 PWM 控制模組測試
├── light.py                 # 光敏電阻與 LED 控制模組測試
├── temp.py                  # DHT11 溫溼度讀取模組測試
├── README.md                
├── LICENSE                  
└── venv/                    # Python 虛擬環境（不建議提交至 Git）
```

## ⚙️ python套件需求
```bash
flask
python-dotenv
line-bot-sdk
gpiozero
adafruit-circuitpython-dht
```

## 📱 LINE 指令列表

> 指令 **不分大小寫**

| 指令 | 功能說明 |
|------|----------|
| `LED ON` | 手動開啟 LED |
| `LED OFF` | 手動關閉 LED |
| `FAN ON` | 手動開啟風扇（全速） |
| `FAN OFF` | 手動關閉風扇 |
| `AUTO ON` | 啟用自動控制模式 |
| `AUTO OFF` | 關閉自動控制模式 |
| `TEMP` | 查詢目前溫度與濕度 |

### 📌 補充說明
- **自動模式（AUTO ON）**：  
  - 光敏電阻自動控制 LED  
  - 溫度自動調整風扇轉速  
- 發送 **LED / FAN 手動指令** 時，系統會自動切換為手動模式，避免自動控制覆蓋使用者設定。
