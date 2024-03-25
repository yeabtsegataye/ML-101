import cv2
from deepface import DeepFace

# Initialize webcam
cap = cv2.VideoCapture(0)

# Error handling for webcam access
if not cap.isOpened():
    print("Error opening webcam. Please check your device.")
    exit()

while True:
    # Capture video frame
    ret, frame = cap.read()

    # Check if frame is read successfully
    if not ret:
        print("Error reading frame from webcam. Exiting...")
        break

    # Use the recommended `extract_faces` function
    results = DeepFace.extract_faces(frame, detector_backend='opencv', enforce_detection=False)

    # Handle potential lack of detected faces gracefully
    if len(results) == 0:
        print("No faces detected in the frame.")
        cv2.imshow('Emotion Detection', frame)
        cv2.waitKey(1)
        continue

    face_img = results[0]['face']  # Assuming single face for simplicity

    # Emotion analysis (assuming successful face detection)
    try:
        emotion = DeepFace.analyze(face_img, actions=['emotion'])['emotion']
        # Display emotion label on the frame
        x, y, w, h = results[0]['roi']  # Extract region of interest
        cv2.putText(frame, f"Emotion: {emotion}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    except (KeyError, ValueError):  # Handle potential errors during analysis
        print("Error analyzing face. Skipping to next frame.")

    # Display the frame
    cv2.imshow('Emotion Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close window
cap.release()
cv2.destroyAllWindows()
