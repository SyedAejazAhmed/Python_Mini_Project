import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import streamlit as st

st.title("Deepfake Detection - Model Training")

if st.button("Train Model"):
    # Data generators for training and validation
    train_datagen = ImageDataGenerator(rescale=1.0/255.0, validation_split=0.2)
    train_generator = train_datagen.flow_from_directory(
        'output_frames_folder',  # Path to the folder with extracted frames
        target_size=(128, 128),
        batch_size=32,
        class_mode='binary',
        subset='training'
    )
    validation_generator = train_datagen.flow_from_directory(
        'output_frames_folder',
        target_size=(128, 128),
        batch_size=32,
        class_mode='binary',
        subset='validation'
    )

    # Model definition
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Model training
    model.fit(train_generator, epochs=10, validation_data=validation_generator)

    # Save the model
    model.save('deepfake_detection_model.h5')
    st.success("Model training completed and saved to deepfake_detection_model.h5")
