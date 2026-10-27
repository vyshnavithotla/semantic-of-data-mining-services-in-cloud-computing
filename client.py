"""
client.py — test client for the Cloud Server feature.

What this does:
Sends MULTIPLE patients' data to your running server, one after another,
and prints each prediction as it comes back. This proves the server can
handle repeated requests, not just a single one-off test.

HOW TO USE:
1. Run your main app first: python main.py
2. In the app window, click buttons in order:
   Upload Diabetes Dataset -> Preprocess Dataset -> Train Random Forest Algorithm
   -> Start Cloud Server & Publish CCDM Service
3. Open a SECOND terminal window (keep the app running in the first one)
4. In that second terminal, run: python client.py
5. Watch BOTH windows: this terminal prints each patient + prediction,
   and the app's text box shows "from connected user" + prediction for each one.
"""

import socket
import time

# Each row: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
# Comment (label) shows the real recorded outcome from the dataset, for comparison.
patients = [
    ("6,148,72,35,0,33.6,0.627,50",   "known diabetic case (expect 1)"),
    ("1,85,66,29,0,26.6,0.351,31",    "known healthy case (expect 0)"),
    ("8,183,64,0,0,23.3,0.672,32",    "known diabetic case (expect 1)"),
    ("1,89,66,23,94,28.1,0.167,21",   "known healthy case (expect 0)"),
    ("0,137,40,35,168,43.1,2.288,33", "known diabetic case (expect 1)"),
]

host = socket.gethostname()   # same machine as the server, so this matches
port = 5000

print(f"Sending {len(patients)} patients to the server one by one...\n")

for i, (data, label) in enumerate(patients, start=1):
    client_socket = socket.socket()
    client_socket.connect((host, port))

    client_socket.send(data.encode())
    response = client_socket.recv(1024).decode().strip()

    result_text = "Diabetes predicted (1)" if response == "1" else "No diabetes predicted (0)"
    print(f"Patient {i}: {label}")
    print(f"   Sent:      {data}")
    print(f"   Predicted: {result_text}\n")

    client_socket.close()
    time.sleep(0.5)   # small pause so the server has time to loop back and accept the next connection

print("Done. Check the app's text box — it should show one line per patient too.")