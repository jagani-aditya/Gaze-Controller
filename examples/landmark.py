import numpy as np
import cv2
import face_recognition

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx=1, fy=1)

    # Find all facial features in all the faces in the video
    face_landmarks_list = face_recognition.face_landmarks(frame)

    for face_landmarks in face_landmarks_list:
        # Loop over each facial feature (eye, nose, mouth, lips, etc)
        for name, list_of_points in face_landmarks.items():

            hull = np.array(face_landmarks[name])
            hull_landmark = cv2.convexHull(hull)
            cv2.drawContours(frame, hull_landmark, -1, (0, 255, 0), 3)


    cv2.imshow("Frame", frame)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
