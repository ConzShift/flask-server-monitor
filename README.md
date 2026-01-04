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
![Dashboard Screenshot](screenshot.png)

![Server Monitor Dashboard](server-monitor-dashboard.gif)

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
```bash
docker build -t server-monitor .
```
### 2. Run the container
```bash
docker run -p 5000:5000 server-monitor
```
### open:
```bash
http://localhost:5000
```

# 🔧 Run as a systemd Service (Optional)
### Create a service file:
```bash
sudo nano /etc/systemd/system/server-monitor.service
```
### Example:
```bash
[Unit]
Description=Flask Server Monitor
After=network.target

[Service]
User=dev
WorkingDirectory=/home/dev/server-monitor
ExecStart=/usr/bin/python3 app.py
Restart=always

[Install]
WantedBy=multi-user.target
```
### Enable + start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable server-monitor
sudo systemctl start server-monitor
```
# 📁 Project Structure
```bash
flask-server-monitor/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   └── dashboard.html
└── .gitignore
```

# 🧠 Skills Demonstrated
- Backend API development
- Real‑time data handling
- Frontend charting with Chart.js
- Docker image creation & container deployment
- Linux service management (systemd)
- Clean project structure & documentation
- Git/GitHub workflow mastery

# 🌱 Future Improvements
- Add network upload/download monitoring
- Add disk I/O and temperature sensors
- Add GPU usage (if available)
- Add dark/light theme toggle
- Export dashboard as PNG/PDF
- Add authentication for remote access

---








