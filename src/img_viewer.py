import streamlit as st
import base64
import plotly.express as px

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()



st.title("👻🔮 DreamMinds.AI")
st.subheader("", divider='rainbow')



dream = st.text_area("Enter your Dream description in short:", 
                     placeholder="We were at a theme park, enjoying the rides, when suddenly my friends started disappearing one by one. The park became empty and eerie. I had to solve the mystery and bring them back before I was left all alone.")

if st.button("🧵 Weave the Dream"):
    pass





# st.image("generated_image.png")


import streamlit as st
from PIL import Image

# Open the image using PIL
image = Image.open("generated_image.png")

# Resize the image
# new_image = image.resize((400, 400))
# Use Streamlit columns to center the image
col1, col2, col3 = st.columns([0.5, 3.5, 0.5])  # Adjust the width ratio as needed
with col2:
    st.image(image, use_column_width=True)









st.write("The Infinite School Hallway: My friends and I were stuck in a school where the hallways never ended. Every time we turned a corner, we found ourselves back at the same spot. The school bell kept ringing, but no one was around. We had to figure out how to escape before we were trapped there forever.were at a theme park, enjoying the rides, when suddenly my friends started disappearing one by one. The park became empty and eerie.")



