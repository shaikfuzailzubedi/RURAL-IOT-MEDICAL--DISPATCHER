# Rural IoT: Automatic Medical Dispatcher with Dynamic Tele-Monitoring System

> Published in *International Journal of Advanced Research and Review (IJARR)*, 10(5), 2025; 22–33.

An IoT-based Anytime Medical Machine (AMM) designed to bring basic diagnosis, vitals monitoring, and medicine dispatch to rural and underserved areas with limited access to doctors.

## Authors
MD. Khaja Pasha, Mohammed Waseem, Syed Mustafa Ali, Shaik Fuzail Zubedi, Satish Chandra Goud
Department of Electronics and Communication Engineering, Lords Institute of Engineering and Technology, Hyderabad, Telangana, India.

## Abstract
Rural healthcare access remains a major challenge in India, where over 70% of the population lives in areas with limited medical infrastructure. This project proposes an Anytime Medical Machine (AMM) that continuously monitors a patient's vital parameters — heart rate, body temperature, and other readings — using IoT sensors, and connects the patient with a remote doctor over a live audio/video link. The doctor examines the patient, prescribes medication, and the AMM automatically dispatches the correct tablets. Patients can also query the system for their medicine intake timings.

## Features
- Real-time vitals monitoring: heart rate (pulse sensor), body temperature (contactless IR sensor)
- Ultrasonic sensor for object/patient presence detection
- Camera + headphone for live voice/video consultation with a remote doctor
- Automatic medicine dispatch via load cell + motor/relay driven dispenser
- OLED display for on-device status and readings
- Emergency alerting to nearest healthcare facility with live location
- Server-based query system for medicine intake schedule

## System Architecture
```
Power Supply → Microcontroller (Raspberry Pi Pico W)
                     │
   ┌─────────────────┼───────────────────────┐
   │                 │                       │
Temperature      Pulse Sensor          Ultrasonic Sensor
Sensor (MLX90614)                      (HC-SR04)
   │                 │                       │
   └─────────────────┴───────────┬───────────┘
                                  │
                         Microcontroller
                          │           │
                        OLED     Driver Circuit → Load Cell
                        Display    (ULN2003/Relay)  (Medicine Dispenser)
                          │
                        Camera (video consult)
```

## Hardware Components
| Component | Purpose |
|---|---|
| Raspberry Pi Pico W (RP2040 + CYW43439 Wi-Fi/BT) | Main microcontroller with wireless connectivity |
| Pulse Sensor | Heart rate monitoring |
| MLX90614 | Contactless IR body temperature sensor |
| HC-SR04 Ultrasonic Sensor | Distance/presence detection |
| Camera module | Live video consultation |
| OLED Display (0.96", 128x64) | Local readout of vitals/status |
| Buzzer | Audio alerts |
| Relay + ULN2003 Darlington driver | Driving the medicine dispenser motor |
| Load Cell | Dispensing/weight verification |
| LM7805 + transformer + rectifier + filter | +5V regulated power supply |

## Repository Structure
```
rural-iot-medical-dispatcher/
├── README.md
├── LICENSE
├── docs/
│   └── hardware.md        # detailed component notes from the paper
├── src/
│   ├── main.py             # main control loop (MicroPython, Pico W)
│   ├── sensors.py          # sensor driver wrappers
│   └── dispenser.py        # medicine dispatch control
└── .github/
    └── ISO_ISSUE_TEMPLATE (optional)
```

## Getting Started
1. Flash MicroPython firmware onto the Raspberry Pi Pico W.
2. Wire up sensors as per `docs/hardware.md`.
3. Copy the contents of `src/` onto the Pico W (e.g. using Thonny).
4. Update Wi-Fi credentials and server endpoint in `main.py`.
5. Run `main.py`.

> Note: The `src/` code here is a starting scaffold reconstructed from the published paper's design — replace pin numbers and calibration values with your actual build's wiring.

## Future Scope
- Machine learning for predictive healthcare and chronic condition detection
- Multi-language voice alerts / AI virtual assistant for non-literate users
- Integration with government health databases and insurance schemes
- Solar-powered nodes and satellite IoT connectivity for fully off-grid deployment

## Citation
If you reference this work, please cite:
```
MD. Khaja Pasha, Mohammed Waseem, Syed Mustafa Ali, Shaik Fuzail Zubedi, Satish Chandra Goud,
"Rural IoT: Automatic Medical Dispatcher with Dynamic Tele Monitoring System Using IoT in Rural Zones",
International Journal of Advanced Research and Review, 10(5), 2025, pp. 22-33.
```

## License
MIT License — see [LICENSE](LICENSE).
