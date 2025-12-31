# 📊 Flask Server Monitor Dashboard

A lightweight, real‑time server monitoring dashboard built with **Flask**, **psutil**, and **Chart.js**. It displays live CPU, memory, disk usage, system uptime, and a rolling CPU usage history chart. The project is fully containerized with **Docker**, making it portable and easy to deploy on any machine.

This project demonstrates backend development, API design, frontend integration, and DevOps workflows (Docker + systemd).

---

## 🚀 Features

- Real‑time CPU, memory, and disk usage  
- Rolling CPU usage history chart (updates every second)  
- System uptime display  
- Clean, responsive dashboard UI  
- REST API endpoints for system metrics  
- Dockerized for consistent deployment  
- Can run as a systemd service on Linux  
- Zero external dependencies beyond Python + psutil  

---

## 🖥️ Dashboard Preview



---

## 🧩 Tech Stack

- **Backend:** Flask  
- **System Metrics:** psutil  
- **Frontend:** HTML, CSS, Chart.js  
- **Containerization:** Docker  
- **Deployment:** systemd (optional)  

---

## 📦 Installation (Local)

### 1. Clone the repo

```bash
git clone https://github.com/ConzShift/flask-server-monitor.git
cd flask-server-monitor
```
### 3. Install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
```
### 4. Run the app
```bash
python app.py
```
### Visit:
```bash
http://localhost:5000
```
# 🐳 Run with Docker (Recommended)

### 1. Build the image

