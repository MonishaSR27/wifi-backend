# Wi-Fi Management Tool - Backend
<br>
This is the backend of the **Remote Wi-Fi Management Tool** built with Flask. It simulates router management actions such as changing Wi-Fi password, rebooting the router and listing connected devices.
<br>
The backend is designed to work with React + TypeScript frontend and is structured as a pluggable framework that can later be integrated with real router APIs or SSH commands.
<br>
<br>
## Features
<br>
- 'POST /change_password' : Simulates changing the router Wi-Fi password
<br>
- 'POST /reboot' : Simulates a router reboot with a delay
<br>
- 'GET /connected_devices' : returns mock connected device data
<br>
- Logs actions triggered via API for frontend display
<br>
<br>
## Tech Stack
<br>
- Python
<br>
- Flask
<br>
- Flask-CORS(for frontend integration)
<br>
- RESTful API design
<br>
- JSON for request/response handling
<br>
<br>
## Getting Started
<br>
1. Clone the repository
<br>
git clone https://github.com/MonishaSR27/wifi-backend.git
<br>
cd backend
<br>
2.Create and activate a virtual environment
<br>
python -m venv venv
<br>
source venv/bin/activate  # On Windows: venv\Scripts\activate
<br>
3.Install dependencies
<br>
pip install -r requirements.txt
<br>
4.Run the Flask app
<br>
python app.py

