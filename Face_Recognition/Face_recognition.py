import cv2
import dlib
import numpy as np
import os
import requests
import bz2
import time
import json

# URLs for the necessary models
SHAPE_PREDICTOR_URL = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"
FACE_RECOGNITION_MODEL_URL = "http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2"

# Filenames for the models
SHAPE_PREDICTOR_FILENAME = "shape_predictor_68_face_landmarks.dat"
FACE_RECOGNITION_MODEL_FILENAME = "dlib_face_recognition_resnet_model_v1.dat"
KNOWN_FACES_FILE = "known_faces.json"

# Function to download and extract the models if they don't exist
def download_and_extract_model(url, filename, retries=5):
    if not os.path.exists(filename):
        for attempt in range(retries):
            try:
                print(f"Downloading {filename} (Attempt {attempt + 1})...")
                response = requests.get(url, stream=True)
                response.raise_for_status()
                with open(filename + ".bz2", 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                print(f"Extracting {filename}...")
                with bz2.BZ2File(filename + ".bz2") as fr, open(filename, 'wb') as fw:
                    fw.write(fr.read())
                os.remove(filename + ".bz2")
                print(f"{filename} downloaded and extracted successfully.")
                return
            except requests.RequestException as e:
                print(f"Failed to download {filename}: {e}")
                if attempt < retries - 1:
                    print("Retrying...")
                    time.sleep(2)  # Wait before retrying
                else:
                    print("Max retries reached. Exiting.")
                    raise

# Download required models
download_and_extract_model(SHAPE_PREDICTOR_URL, SHAPE_PREDICTOR_FILENAME)
download_and_extract_model(FACE_RECOGNITION_MODEL_URL, FACE_RECOGNITION_MODEL_FILENAME)

# Load the face detector and shape predictor from dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(SHAPE_PREDICTOR_FILENAME)

# Load the face recognition model
face_rec_model = dlib.face_recognition_model_v1(FACE_RECOGNITION_MODEL_FILENAME)

# Load known faces and their names
known_faces = []
known_names = []

def load_known_faces():
    global known_faces, known_names
    if os.path.exists(KNOWN_FACES_FILE):
        with open(KNOWN_FACES_FILE, 'r') as f:
            data = json.load(f)
            known_faces = [np.array(face) for face in data['faces']]
            known_names = data['names']
    else:
        known_faces = []
        known_names = []

def save_known_faces():
    with open(KNOWN_FACES_FILE, 'w') as f:
        json.dump({
            'faces': [face.tolist() for face in known_faces],
            'names': known_names
        }, f)

def get_face_encoding(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    if len(faces) == 0:
        return None
    
    shape = predictor(gray, faces[0])
    face_descriptor = face_rec_model.compute_face_descriptor(image, shape)
    return np.array(face_descriptor)

def recognize_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    
    for face in faces:
        shape = predictor(gray, face)
        face_descriptor = face_rec_model.compute_face_descriptor(image, shape)
        face_descriptor = np.array(face_descriptor)
        
        # Compare with known faces only if known_faces is not empty
        if known_faces:
            distances = np.linalg.norm(known_faces - face_descriptor, axis=1)
            min_distance_index = np.argmin(distances)
        
            if distances[min_distance_index] < 0.6:
                name = known_names[min_distance_index]
            else:
                name = "Unknown"
        else:
            name = "Unknown"
        
        # Draw a rectangle around the face and label it
        (x, y, w, h) = (face.left(), face.top(), face.width(), face.height())
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        # If the face is unknown, prompt the user to add it
        if name == "Unknown":
            return face_descriptor, face

    return None, None

def main():
    # Load known faces
    load_known_faces()
    
    # Initialize video capture
    cap = cv2.VideoCapture(0)  # Change to video file path if using a video file
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Recognize faces in the frame
        face_descriptor, face = recognize_faces(frame)
        
        # If an unknown face is detected
        if face_descriptor is not None:
            cv2.imshow('Unknown Face', frame)
            print("Unknown face detected. Press 'a' to add, 'c' to continue without adding.")
            key = cv2.waitKey(0)
            if key == ord('a'):
                new_name = input("Enter name for the new face: ")
                known_faces.append(face_descriptor)
                known_names.append(new_name)
                save_known_faces()
                print(f"Added new face: {new_name}")
            elif key == ord('c'):
                print("Continuing without adding the face.")
            if cv2.getWindowProperty('Unknown Face', cv2.WND_PROP_VISIBLE) >= 1:
                cv2.destroyWindow('Unknown Face')  # Destroy the window only if it exists
        
        # Display the frame
        cv2.imshow('Face Recognition', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
