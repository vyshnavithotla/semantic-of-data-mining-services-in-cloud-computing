# Semantics of Data Mining Services in Cloud Computing

A desktop application (built with Python's Tkinter GUI) that trains a Random Forest machine learning model to predict diabetes, and can serve predictions to other devices over a network — demonstrating a cloud-based data mining service.

## What It Does

1. **Upload Dataset** — Load a diabetes dataset (CSV) through a simple file picker.
2. **Preprocess Dataset** — Splits the data into training (90%) and testing (10%) sets.
3. **Train Random Forest Algorithm** — Trains a Random Forest Classifier (500 trees) and displays model accuracy.
4. **Start Cloud Server & Publish CCDM Service** — Starts a local server (port 5000) so other machines on the network can send patient data and receive a diabetes prediction back.

## Dataset

Uses the **Pima Indians Diabetes Dataset** — 768 patient records with features:

`Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome`

The dataset is included in this repo at `dataset/diabetes.csv`.

## Tech Stack

- Python 3
- Tkinter (GUI)
- Pandas, NumPy (data handling)
- Scikit-learn (Random Forest model)
- Socket programming (client-server communication)

## How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/vyshnavithotla/semantic-of-data-mining-services-in-cloud-computing.git
   cd semantic-of-data-mining-services-in-cloud-computing
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   python main.py
   ```

4. **Using the app:**
   - Click **"Upload Diabetes Dataset"** → select `dataset/diabetes.csv`
   - Click **"Preprocess Dataset"** → view train/test split info
   - Click **"Train Random Forest Algorithm"** → view model accuracy
   - Click **"Start Cloud Server & Publish CCDM Service"** → starts listening for prediction requests on port 5000
5. **Testing the Cloud Server**

   - Run `python main.py` and click the buttons in order: Upload → Preprocess → Train → Start Cloud Server.
   - Open a second terminal in the project folder and run:
   ```bash
   python client.py
   ```
  `client.py` sends 5 sample patients to the server. Each prediction appears in the terminal and in the app's text box (1 = diabetes, 0 = no diabetes).

## Result

Achieves **~82% accuracy** on the Pima Indians Diabetes Dataset using a Random Forest Classifier.

## Project Background

This project was developed as a Minor Project for the Bachelor of Technology degree (CSE - AI & ML) at Malla Reddy College of Engineering, exploring how semantic and cloud-based data mining services can improve the reliability and accessibility of machine learning predictions.
