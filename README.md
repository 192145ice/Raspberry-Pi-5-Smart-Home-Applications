# Raspberry Pi 5 Smart Home Applications

本專案開發一套基於 Raspberry Pi 5 的智慧家庭控制系統，
透過感測器資料與遠端控制介面，
實現環境監測、自動調節與設備管理功能。

系統整合光敏電阻與溫溼度感測器，
可依環境亮度自動控制 LED，
並依據溫度變化透過 PWM 調整風扇轉速，
以達到自動化環境控制效果。

此外，透過 LINE Bot API 建立即時遠端控制介面，
使用者可查詢環境狀態並手動控制設備，
系統同時支援自動模式與手動模式切換，
避免控制衝突並提升系統穩定性。

專案成果包含：

- IoT 環境監測與控制系統實作
- Raspberry Pi GPIO 裝置控制
- PWM 風扇速度調整
- LINE Bot 遠端控制整合
- 自動 / 手動控制邏輯設計

<h3>Demo Video</h3>

<a href="https://youtu.be/rwNc7hAQefU">
  <img src="https://img.youtube.com/vi/rwNc7hAQefU/0.jpg" width="600">
</a>

<h3>Click me!</h3>

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
