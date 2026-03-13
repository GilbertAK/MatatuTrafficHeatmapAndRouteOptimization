# 🚐 Nairobi Matatu Traffic Heatmap (Project 07)

A real-time geospatial data simulation engine designed to monitor Matatu movement across Nairobi's major routes (Thika Road, Ngong Road, Jogoo Road).

## 🚀 Overview
This system simulates high-frequency GPS telemetry to identify traffic density. It uses a **Point-in-Polygon** logic to determine if a vehicle is in a "Hotspot" zone.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Colorama (Terminal UI), Numpy (Telemetry Simulation), Pandas (Data Management).
- **Concepts:** Geospatial mapping, Real-time analytics, Risk scoring.

## 📊 Logic
The engine calculates a `Congestion Index` based on:
1. Average speed of Matatus in a specific sector.
2. Number of active GPS pings within a 500m radius.