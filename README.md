# Smart Lighting Embedded System

Smart lighting system with automatic light regulation using Raspberry Pi, Raspberry Pi Pico, light sensors, PWM and Wi-Fi communication.

## Overview

This project implements a smart lighting system designed to automatically regulate light intensity based on ambient light conditions.

The system combines a Raspberry Pi, Raspberry Pi Pico, light sensors and PWM-based dimming. It also provides manual control through a mobile application.

## System Architecture

The Raspberry Pi acts as a central part of the system and communicates with sensors, the microcontroller and the mobile application.

![Smart Lighting System Architecture](images/system-architecture.webp)

## Features

- Automatic light intensity regulation
- PWM-based light dimming
- Ambient light measurement
- Raspberry Pi and Raspberry Pi Pico integration
- Wi-Fi communication
- Mobile application control
- UART communication
- I²C communication
- Sensor-based lighting control

## Hardware

The system uses several hardware components for sensing, communication and lighting control:

- Raspberry Pi
- Raspberry Pi Pico
- Microcontroller
- Light sensors
- Photodiode
- Operational amplifier
- Lighting driver
- Light source

## Software & Technologies

The project combines embedded hardware with software and communication technologies:

- Python
- Raspberry Pi
- Raspberry Pi Pico
- PWM
- UART
- I²C
- Wi-Fi
- Embedded systems
- Sensor interfacing

## Mobile Application

A mobile application provides manual control of the lighting system. The interface allows the user to turn the light on or off and change the light intensity.

### Main Control Interface

![Mobile App Control Interface](images/mobile-app-control-interface.png)

### Light Intensity Control

![Mobile App Dimming Control](images/mobile-app-dimming-control.png)

## Raspberry Pi Software

Python is used on the Raspberry Pi for communication and control of different parts of the system.

The software includes functionality for:

- PWM control
- UART communication
- Communication with sensors
- Light dimming
- Server functionality
- System testing

![Raspberry Pi Server Code](images/raspberry-pi-server-code.webp)

## Source Code

The source code is available in the `src/` directory.

```text
src/
├── PWM.py
├── dimming.py
├── UARTtr.py
├── timerTest.py
├── server.py
└── server2.py
```

The different Python scripts handle communication, PWM control, dimming, server functionality and testing.

## Project Structure

```text
smart-lighting-embedded-system/
├── images/
│   ├── mobile-app-control-interface.png
│   ├── mobile-app-dimming-control.png
│   ├── raspberry-pi-server-code.webp
│   └── system-architecture.webp
│
├── src/
│   ├── PWM.py
│   ├── dimming.py
│   ├── UARTtr.py
│   ├── timerTest.py
│   ├── server.py
│   └── server2.py
│
├── .gitignore
└── README.md
```

## Key Concepts

This project demonstrates practical experience with:

- Embedded systems
- Microcontrollers
- Raspberry Pi development
- Sensor integration
- PWM-based control
- UART and I²C communication
- Wi-Fi communication
- Python programming
- Hardware-software integration
