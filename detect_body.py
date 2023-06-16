import cv2
import numpy as np
import dlib

# Load the face detector and predictor
face_detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Read the image or video
image = cv2.imread("image.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_detector(gray)

# For each face, find the 68 facial landmarks
for face in faces:
    landmarks = predictor(gray, face)

    # Calculate the body dimensions
    height = landmarks[62][1] - landmarks[51][1]
    weight = landmarks[30][0] - landmarks[16][0]
    waist = landmarks[23][1] - landmarks[27][1]
    hip = landmarks[29][1] - landmarks[31][1]

    # Find the chest landmarks
    chest_landmarks = []
    for i in range(68):
        if landmarks[i][0] > landmarks[30][0] and landmarks[i][0] < landmarks[31][0]:
            chest_landmarks.append(landmarks[i])

    # Calculate the chest circumference
    chest_circumference = 0
    for i in range(len(chest_landmarks) - 1):
        chest_circumference += np.sqrt((chest_landmarks[i][0] - chest_landmarks[i + 1][0])**2 + (chest_landmarks[i][1] - chest_landmarks[i + 1][1])**2)

    # Find the shoulders landmarks
    shoulders_landmarks = []
    for i in range(68):
        if landmarks[i][1] > landmarks[27][1] and landmarks[i][1] < landmarks[29][1]:
            shoulders_landmarks.append(landmarks[i])

    # Calculate the shoulders width
    shoulders_width = 0
    for i in range(len(shoulders_landmarks) - 1):
        shoulders_width += np.sqrt((shoulders_landmarks[i][0] - shoulders_landmarks[i + 1][0])**2 + (shoulders_landmarks[i][1] - shoulders_landmarks[i + 1][1])**2)

    # Print the body dimensions
    print("Height:", height)
    print("Weight:", weight)
    print("Waist:", waist)
    print("Hip:", hip)
    print("Chest circumference:", chest_circumference)
    print("Shoulders width:", shoulders_width)
