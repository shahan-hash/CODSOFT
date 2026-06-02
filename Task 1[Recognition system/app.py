import streamlit as st
import pandas as pd
import os
import subprocess
import sys

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="Face Attendance System",
    page_icon="📸",
    layout="wide"
)

st.title("📸 AI Face Recognition Attendance System")
st.markdown("---")

# ---------------- SESSION STATE ----------------
if "process_started" not in st.session_state:
    st.session_state.process_started = False

# ---------------- ADD PERSON FEATURE ----------------
st.sidebar.header("👤 Add New Person")

name = st.sidebar.text_input("Enter Name")
img_file = st.sidebar.file_uploader("Upload Face Image", type=["jpg", "png", "jpeg"])

if st.sidebar.button("Add Person"):

    if name and img_file:

        folder = "photo"

        if not os.path.exists(folder):
            os.makedirs(folder)

        file_path = os.path.join(folder, f"{name}.jpg")

        with open(file_path, "wb") as f:
            f.write(img_file.read())

        st.sidebar.success(f"{name} added successfully ✔")

    else:
        st.sidebar.warning("Please enter name and upload image")

# ---------------- CONTROL PANEL ----------------
st.subheader("🎥 Control Panel")

col1, col2 = st.columns(2)

with col1:
    if st.button("▶ Start Face Recognition"):

        if not st.session_state.process_started:

            subprocess.Popen(
                [sys.executable, "face_attendance.py"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0
            )

            st.session_state.process_started = True
            st.success("Face Recognition Started 🚀")

        else:
            st.warning("Already running ⚠️")

with col2:
    if st.button("🛑 Stop System (manual)"):

        st.session_state.process_started = False
        st.warning("Stop the face_attendance.py window manually")

st.markdown("---")

# ---------------- DASHBOARD ----------------
st.subheader("📋 Attendance Dashboard")

if os.path.exists("attendance.csv"):

    try:
        df = pd.read_csv("attendance.csv")

        # safety check
        if "Name" in df.columns:

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Total Records", len(df))

            with col2:
                st.metric("Unique People", df["Name"].nunique())

            st.dataframe(df, use_container_width=True)

            st.download_button(
                "📥 Download CSV",
                df.to_csv(index=False),
                file_name="attendance.csv",
                mime="text/csv"
            )

        else:
            st.error("CSV format incorrect. Delete attendance.csv and restart.")

    except Exception as e:
        st.error(f"Error reading CSV: {e}")

else:
    st.info("No attendance found yet. Start face recognition.")

st.markdown("---")
st.caption("Built with Python 🐍 | OpenCV 👁️ | Face Recognition 🤖 | Streamlit ⚡")