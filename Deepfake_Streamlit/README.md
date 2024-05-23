# Deepfake Detection with Streamlit

This repository contains a project for detecting deepfakes using machine learning models and Streamlit for an interactive web interface. The project is divided into three main components:

1. **Frame Extraction** (`extract_frames_streamlit.py`)
2. **Model Training** (`train_model_streamlit.py`)
3. **Deepfake Detection** (`detect_deepfake_streamlit.py`)

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
  - [Frame Extraction](#frame-extraction)
  - [Model Training](#model-training)
  - [Deepfake Detection](#deepfake-detection)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Deepfake technology has made it increasingly difficult to distinguish between real and fake media. This project provides a technical solution to detect and mitigate the spread of deepfakes by using Convolutional Neural Networks (CNNs) and an interactive Streamlit interface.

## Setup

To set up the project on your local machine, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/SyedAejazAhmed/Python_Mini_Project.git
    cd Deepfake_Streamlit
    ```

2. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Install additional dependencies for Streamlit:**

    ```bash
    pip install streamlit opencv-python-headless tensorflow
    ```

## Dependencies
1. Python 3.6+
2. TensorFlow
3. OpenCV
4. Streamlit

## Usage
## Running the Streamlit App

### You need to run each script separately using Streamlit. Open a terminal in your project directory and run:
```bash
streamlit run extract_frames_streamlit.py
```

### Then in another terminal:
```bash
streamlit run train_model_streamlit.py
```

### And finally:
```bash
streamlit run detect_deepfake_streamlit.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
