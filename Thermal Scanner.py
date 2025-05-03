
import cv2
import numpy as np

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Simulate temperature map (normalize gray to 20-40°C)
    temp_map = cv2.normalize(gray, None, 20, 40, cv2.NORM_MINMAX)

    # Apply thermal colormap for visualization
    thermal_frame = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Get region of interest (ROI) in temp_map
        face_temp_roi = temp_map[y:y + h, x:x + w]
        avg_temp = np.mean(face_temp_roi)
        temp_text = f"{avg_temp:.1f}°C"

        # Draw rectangle and overlay temperature
        cv2.rectangle(thermal_frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        cv2.putText(thermal_frame, temp_text, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    # Display the result
    cv2.imshow('Thermal Scanner with Person Detection', thermal_frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()





