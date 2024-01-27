import streamlit as st
from PIL import Image, ImageEnhance

def enhance_image(image, enhancement_factor):
    enhanced_image = ImageEnhance.Contrast(image).enhance(enhancement_factor)
    return enhanced_image

def main():
    st.title('Enhance Your Images')
    st.write('Upload an image and enhance it!')

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption='Original Image', use_column_width=True)

        enhancement_factor = st.slider('Enhancement Factor', 0.0, 2.0, 1.0)

        if st.button('Enhance'):
            # Load the image
            image = Image.open(uploaded_image)

            # Enhance the image
            enhanced_image = enhance_image(image, enhancement_factor)

            # Display the enhanced image
            st.image(enhanced_image, caption='Enhanced Image', use_column_width=True)

if __name__ == "__main__":
    main()
