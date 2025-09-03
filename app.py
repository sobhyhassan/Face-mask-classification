import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("mask_model.h5")

# Define preprocessing function
def preprocess_image(image):
    image = image.resize((128, 128))  # نفس حجم التدريب
    image = image.convert("RGB")
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)  # (1, 128, 128, 3)
    return image

st.title("😷 Face Mask Detection App")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Prediction
    img_array = preprocess_image(image)
    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        st.success("✅ With Mask")
    else:
        st.success("🚫 Without Mask")
        
