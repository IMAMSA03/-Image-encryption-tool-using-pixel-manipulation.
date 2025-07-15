import streamlit as st
from PIL import Image
import numpy as np

def encrypt_image(image, key):
    image_array = np.array(image).astype(np.uint16)
    encrypted_array = (image_array + key) % 256
    return encrypted_array.astype(np.uint8)

def decrypt_image(image, key):
    image_array = np.array(image)
    temp_array = image_array.astype(np.int16)
    decrypted_array = (temp_array - key + 256) % 256
    decrypted_array = decrypted_array.astype(np.uint8)
    return Image.fromarray(decrypted_array)

st.set_page_config(page_title="Image Encryptor", layout="centered")
st.title("Image Encryption & Decryption Tool")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
key = st.number_input("Enter Secret Key (1 to 255)", min_value=1, max_value=255, value=5)

if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Original Image", use_column_width=True)

    if st.button("Encrypt"):
        encrypted_img = encrypt_image(image, key)
        st.image(encrypted_img, caption="Encrypted Image", use_column_width=True)

    if st.button("Decrypt"):
        decrypted_img = decrypt_image(image, key)
        st.image(decrypted_img, caption="Decrypted Image", use_column_width=True)
