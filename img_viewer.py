import streamlit as st
import base64
import plotly.express as px

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()



img = get_img_as_base64("image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)





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
new_image = image.resize((400, 400))
# Use Streamlit columns to center the image
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the width ratio as needed
with col2:
    st.image(new_image, use_column_width=True)









st.write("The Infinite School Hallway: My friends and I were stuck in a school where the hallways never ended. Every time we turned a corner, we found ourselves back at the same spot. The school bell kept ringing, but no one was around. We had to figure out how to escape before we were trapped there forever.were at a theme park, enjoying the rides, when suddenly my friends started disappearing one by one. The park became empty and eerie.")



