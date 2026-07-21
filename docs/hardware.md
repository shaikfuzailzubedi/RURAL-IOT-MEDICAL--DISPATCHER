# Hardware Notes

## Power Supply
Provides a regulated +5V for all components.
`Transformer (220V AC step-down) → Diode Rectifier → Capacitor Filter → LM7805 Regulator → Load`

## Raspberry Pi Pico W
- Built around the RP2040 chip (ARM, dual-core Cortex-M0+)
- Adds Wi-Fi 802.11 b/g/n and Bluetooth 5.2 via the Infineon CYW43439 chip
- Power regulator: RT6154A (Richtek)
- Chosen for wireless connectivity, needed to send vitals data and alerts to a remote server

## Ultrasonic Sensor (HC-SR04)
- Ceramic transducer emits and receives ultrasonic pulses
- Distance = f(echo return time)
- Used here for presence/positioning detection at the AMM kiosk

## Buzzer
- Piezoelectric/electromechanical audio signaling device
- Positive terminal (+): typically driven at ~6V
- Negative terminal (-): connected to GND
- Used for local audio alerts (e.g., dispensing complete, error states)

## Relay / Motor Driver Stage
- DC motor drives the medicine dispenser mechanism
- Converts electrical energy to mechanical motion via magnetic field interaction

## ULN2003 Darlington Driver
- Monolithic IC with 7 NPN Darlington transistor pairs
- Open-collector outputs, 500 mA per pair (can be paralleled for higher current)
- Includes built-in clamp diodes — safe for driving inductive loads (motors, relays)
- Used here to drive the dispenser motor/relay from low-current microcontroller logic pins

## CCTV / Camera Module
- Used for live video feed to the remote doctor during consultation

## Heart Rate — Pulse Sensor
- Low-power, plug-and-play heart-rate sensor
- Clips onto a fingertip or earlobe
- Outputs an analog signal proportional to blood volume changes (PPG)

## Temperature Sensor — MLX90614
- Contactless infrared (IR) digital temperature sensor
- Measurement range: -70°C to 382.2°C
- Communicates via I2C protocol
- Chosen to avoid physical/hygienic contact with each patient

## Load Cell
- Used with the driver circuit to verify medicine dispensing (e.g. weight-based confirmation)
