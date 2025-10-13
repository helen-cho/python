import streamlit as st
import cv2
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt 

def predict(file):
    image = np.array(Image.open(file))

    resnet50=tf.keras.applications.resnet.ResNet50(
        weights='imagenet', input_shape=(224, 224, 3)
    )

    image_resize = cv2.resize(image, (224,224))
    image_reshape = image_resize.reshape([1, 224, 224, 3])

    pred=resnet50.predict(image_reshape)
    decoded_pred = tf.keras.applications.imagenet_utils.decode_predictions(pred)
    return decoded_pred[0]

st.title('이미지 분류 인공지능 페이지')
file = st.file_uploader('이미지를 올려주세요.', type=['jpg', 'png'])
if file:
    with st.spinner('기다려주세요...'):
        st.image(file)
        preds = predict(file)
        for idx, pred in enumerate(preds):
            st.success(f'{idx+1}위 {pred[1]}({pred[2] * 100:.2f})')