# 📸 Face Recognition Attendance System

## Overview
A real-time AI system that uses face recognition to mark attendance automatically using webcam input.

---

## Features
- Real-time face detection
- Automatic attendance marking
- Timestamp recording
- Confidence-based recognition
- Simple Streamlit dashboard
- Add users via image dataset

---

## Project Structure
- app.py → Streamlit dashboard
- face_attendance.py → Recognition engine
- photo/ → Known face images
- attendance.csv → Attendance records

---

## How to Run

## Install dependencies
``bash
      pip install streamlit opencv-python face-recognition numpy pandas

### Add dataset

Place images in photo/ folder:


alice.jpg → Alice
bob.jpg → Bob

``` id="dataset_clean"
##Run system
python face_attendance.py
streamlit run app.py
