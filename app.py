from flask import Flask, jsonify, render_template, redirect
import psutil
import time
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
cpu_history = []

# -----------------------------
# ROUTES
# -----------------------------

@app.route("/")
def home():
    # Redirect root → dashboard for better UX
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/metrics")
def metrics():
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = time.time() - psutil.boot_time()

    return jsonify({
        "cpu": cpu,
        "memory": memory,
        "disk": disk,
        "uptime_seconds": int(uptime)
    })

@app.route("/cpu-history")
def get_cpu_history():
    usage = psutil.cpu_percent(interval=None)
    timestamp = time.strftime("%H:%M:%S")

    # Keep last 20 entries
    if len(cpu_history) >= 20:
        cpu_history.pop(0)

    cpu_history.append({
        "time": timestamp,
        "usage": usage
    })

    return jsonify(cpu_history)

# -----------------------------
# MAIN ENTRY
# -----------------------------

if __name__ == "__main__":
    port = int(os.getenv("FLASK_PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "False") == "True"

    print(f"🚀 Server Monitor running at: http://localhost:{port}/dashboard")
    app.run(host="0.0.0.0", port=port, debug=debug)