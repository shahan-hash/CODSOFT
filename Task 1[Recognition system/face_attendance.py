import cv2
import face_recognition
import os
import pandas as pd
from datetime import datetime

# Store known faces
known_encodings = []
known_names = []

photo_folder = "photo"

# Attendance file
attendance_file = "attendance.csv"

# Create attendance file if it doesn't exist
if not os.path.exists(attendance_file):
    df = pd.DataFrame(columns=["Name", "Time", "Date"])
    df.to_csv(attendance_file, index=False)

# Prevent duplicate attendance
marked_attendance = set()

# Load all images from photo folder
for file in os.listdir(photo_folder):

    if file.endswith((".jpg", ".jpeg", ".png")):

        image_path = os.path.join(photo_folder, file)

        image = face_recognition.load_image_file(image_path)

        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:

            known_encodings.append(encodings[0])

            name = os.path.splitext(file)[0]

            known_names.append(name)

print("\nLoaded Faces:")
for name in known_names:
    print(name)

# Start webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    face_locations = face_recognition.face_locations(
        rgb_frame
    )

    face_encodings = face_recognition.face_encodings(
        rgb_frame,
        face_locations
    )

    for (top, right, bottom, left), face_encoding in zip(
        face_locations,
        face_encodings
    ):

        matches = face_recognition.compare_faces(
            known_encodings,
            face_encoding
        )

        face_distances = face_recognition.face_distance(
            known_encodings,
            face_encoding
        )

        name = "Unknown"
        actual_name = "Unknown"

        if len(face_distances) > 0:

            best_match_index = face_distances.argmin()

            if matches[best_match_index]:

                confidence = round(
                    (1 - face_distances[best_match_index]) * 100,
                    2
                )

                actual_name = known_names[
                    best_match_index
                ]

                name = (
                    f"{actual_name} "
                    f"({confidence}%)"
                )

                # Mark attendance only once
                if actual_name not in marked_attendance:

                    now = datetime.now()

                    current_time = now.strftime(
                        "%H:%M:%S"
                    )

                    current_date = now.strftime(
                        "%d-%m-%Y"
                    )

                    attendance = pd.DataFrame(
                        [[
                            actual_name,
                            current_time,
                            current_date
                        ]],
                        columns=[
                            "Name",
                            "Time",
                            "Date"
                        ]
                    )

                    attendance.to_csv(
                        attendance_file,
                        mode="a",
                        header=False,
                        index=False
                    )

                    marked_attendance.add(
                        actual_name
                    )

                    print(
                        f"Attendance Marked: "
                        f"{actual_name}"
                    )

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.imshow(
        "Face Attendance System",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()