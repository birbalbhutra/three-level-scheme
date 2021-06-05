import os
import sys
sys.path.insert(0, './src')

import streamlit as st

from PIL import Image
from src.lsb_stegno import lsb_encode, lsb_decode


menu = st.sidebar.radio('Visual Cryptography', ['Home', 'Encryption', 'Decryption'])

if menu == 'Home':
    st.title('Visual Cryptography')
    with open('README.md', 'r') as f:
        docs = f.read()
    st.markdown(docs, unsafe_allow_html=True)


elif menu == 'Encryption':
    st.title('Encryption')

    # Image
    img = st.file_uploader('Upload an image to be used for encryption', type=['jpg', 'png', 'jpeg'])
    if img is not None:
        img = Image.open(img)
        try:
            img.save('images/img.jpg')
        except:
            img.save('images/img.png')
        st.image(img, caption='Selected image to use for data encoding',
                use_column_width=True)

    # Data
    txt = st.text_input('Give your Message')

    # Encode message
    if st.button('Encrypt Message'):

        # Checks
        if len(txt) == 0:
            st.warning('No data to hide')
        elif img is None:
            st.warning('No image file selected')

        # Generate splits
        else:
            lsb_encode(txt)
            st.success('Data encoded, Shares generated in folder [images]')

elif menu == 'Decryption':
    st.title('Decryption')

    # Share 
    img1 = st.file_uploader('Upload First Encrypted Image', type=['png'])
    if img1 is not None:
        img1 = Image.open(img1)
        img1.save('images/share1.png')
        st.image(img1, caption='Image 1', use_column_width=True)

    # Decode message
    if st.button('Decrypt Image'):

        # Check
        if img1 is None:
        # if img1 is None or img2 is None:
            st.warning('Upload both images')

        # Compress shares
        else:
            st.success('Decoded message: ' + lsb_decode('images/share1.png'))

