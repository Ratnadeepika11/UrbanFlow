
# 🏙️ UrbanFlow Dashboard - Urban Infrastructure Audit

An intelligent water management command center providing real-time monitoring, leak detection, and AI-driven audit support for city administrators and utility engineers.

## Overview

**SmartWater Dashboard** is designed to balance resource conservation and infrastructure integrity through an integrated dashboard with visual analytics and automated alerts. Built as a specialized Django application, this project emphasizes data-driven decision making, visual impact, and clean architecture for urban utility management.

## Features

* **Real-Time Sector Audit** - Live monitoring of water inflow vs. consumption across city zones.
* **Infrastructure Leak Detection** - Automated alerts for physical pipe damage based on NRW (Non-Revenue Water) logic.
* **Consumer Wastage Analytics** - Visual tracking of household/sector usage against established thresholds.
* **Water Quality & Pressure Monitoring** - Integrated pH level and Bar pressure sensor visualization.
* **Automated Action Logging** - Intelligent recommendations (e.g., "Deploy Engineers", "Flush System") based on sensor data.
* **Data Visualization** - Color-coded bar charts (Red: Waste, Orange: Leak, Blue: Optimal) for rapid status assessment.

## Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python 3.11+** | Core programming language |
| **Django 4.2+** | Web framework for backend and routing |
| **Pandas** | Data analytics and calculation of city-wide metrics |
| **Matplotlib** | Generation of dynamic infrastructure consumption charts |
| **SQLite3** | Relational database for sector and sensor data |
| **Bootstrap 5** | Responsive UI styling and dashboard components |

## 🔧 Installation

### Prerequisites
* Python 3.11+
* pip (Python package manager)

### Quick Start
1. **Clone the repository**
   ```bash
   git clone [https://github.com/mehetab-01/Smart-City-Water-Monitor.git](https://github.com/mehetab-01/Smart-City-Water-Monitor.git)
   cd Smart-City-Water-Monitor
   pip install django pandas matplotlib
   python manage.py migrate
   python manage.py runserver
   
## Project Structure

```text
smart_city_water_monitor/
├── smart_city/               # Project configuration
│   ├── settings.py           # Core Django settings
│   └── urls.py               # Main routing configuration
├── water_monitor/            # Primary application code
│   ├── models.py             # WaterSector & Sensor database schemas
│   ├── views.py              # Logic for audits, alerts, and graphs
│   └── admin.py              # Sector management interface
├── templates/                # Dashboard UI
│   └── dashboard.html        # Real-time sector audit interface
├── db.sqlite3                # Database containing simulated sensor data
├── manage.py                 # Django application entry point
└── README.md                 # Project documentation

```

## 👤AUTHOR
**RATNADEEPIKA MOSA** <br>
**Project: UrbanFlow Dashboard**
<div align="center">
This project is developed strictly for academic and educational purposes
</div>


