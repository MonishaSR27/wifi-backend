from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for communication from React

@app.route('/change-password', methods=['POST'])
def change_password():
    data = request.get_json()
    ssid = data.get('ssid')
    password = data.get('password')

    # Simulate router password change (for now just print it)
    print(f"Received new SSID: {ssid}, Password: {password}")

    # In future: send to router script here
    return jsonify({"message": "Wi-Fi password change request received."})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
