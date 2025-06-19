from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

# ✅ 1. Connected Devices
@app.route("/connected_devices", methods=["GET"])
def connected_devices():
    # Dummy data to simulate connected devices
    devices = [
        {"device_name": "Phone", "ip": "192.168.1.2"},
        {"device_name": "Laptop", "ip": "192.168.1.3"},
        {"device_name": "Tablet", "ip": "192.168.1.4"}
    ]
    return jsonify(devices), 200

# ✅ 2. Change Wi-Fi Password
@app.route("/change_password", methods=["POST"])
def change_password():
    data = request.get_json()
    new_password = data.get("new_password")

    if not new_password:
        return jsonify({"error": "New password is required."}), 400

    # Simulate changing password (e.g., using router API or SSH commands)
    print(f"Changing Wi-Fi password to: {new_password}")

    return jsonify({"message": "Wi-Fi password changed successfully!"}), 200

# ✅ 3. Reboot Router
@app.route("/reboot", methods=["POST"])
def reboot_router():
    # Simulate rebooting the router
    print("Rebooting router...")

    return jsonify({"message": "Router rebooted successfully!"}), 200

# ✅ Run app with correct host/port for Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
