## Face Recognition Project

## Overview
This project implements a face recognition system using Python, OpenCV, and Dlib. It detects faces in images or video streams and recognizes known faces based on pre-trained models. Unknown faces can be added to the system for future recognition.

## Installation
To run the face recognition system, follow these installation steps:

Clone the Repository:
```bash
  git clone https://github.com/SyedAejazAhmed/Python_Mini_Project/tree/main/Face_Recognition
  ```
  
## Install Dependencies:
Navigate to the project directory and install the required Python dependencies using pip:
```bash
cd face-recognition-project
pip install -r requirements.txt
```

## Download Models:
The script automatically downloads the required face detection and recognition models. However, if you encounter any issues, manually download the following models:
- shape_predictor_68_face_landmarks.dat
- dlib_face_recognition_resnet_model_v1.dat

## Prepare Known Faces:
Add images of known faces to the `known_faces` directory. Ensure the images are named appropriately and contain only the face of the person to be recognized.

## Usage
After completing the installation steps, you can run the face recognition system using the following command:
```bash
python face_recognition.py
```

Follow the on-screen instructions to add new faces to the system when unknown faces are detected. Press 'a' to add a face or 'c' to continue without adding. Press 'q' to quit the application.

## Contributors
- Your Name: [Your GitHub Profile](https://github.com/SyedAejazAhmed)
- Contributor Name: [Contributor GitHub Profile](https://github.com/sujan58)

## License
This project is licensed under the MIT License. See the LICENSE file for details.
