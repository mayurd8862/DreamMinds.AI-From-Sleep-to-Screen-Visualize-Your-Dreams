import streamlit as st
from PIL import Image, UnidentifiedImageError
import os
import io
from src.paragraph_gen import paragraph_gen
from src.prompt_gen import prompt_gen
from src.image_gen import img_gen
import time
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


st.title("👻🔮 DreamMinds.AI")
st.subheader("", divider='rainbow')


def title_gen(story):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
    )
    prompt = f"""
    Your task is to craft a compelling title for the story provided below. The title should capture the core theme and emotion of the story, which is based on a user's dream description. The title must be creative, evocative, and concise, consisting of just 3-4 impactful words. Output should contain only one title with emoji.

    Story:
    {story}
    """
    result = llm.invoke(prompt)
    return result.content

def generate_image_with_retry(content, max_retries=3):
    """Attempt to generate an image with retries on failure."""
    retries = 0
    while retries < max_retries:
        pmt = prompt_gen(content)
        decoded_img = img_gen(pmt)
        try:
            image = Image.open(io.BytesIO(decoded_img))
            return image
            
        except UnidentifiedImageError:
            retries += 1
            st.warning(f"Attempt {retries} failed. Retrying with a new prompt...")
    st.error("Failed to generate a valid image after multiple attempts.")
    return None

dream = st.text_area("Enter your Dream description in short:", 
                     placeholder="We were at a theme park, enjoying the rides, when suddenly my friends started disappearing one by one. The park became empty and eerie. I had to solve the mystery and bring them back before I was left all alone.")

if st.button("🧵 Weave the Dream"):
    start_time = time.time()
    json_otpt = paragraph_gen(dream)
    st.write(json_otpt)
    
    title = title_gen(json_otpt)
    st.subheader(title)

    for key, content in json_otpt.items():

        image = generate_image_with_retry(content)

        col1, col2, col3 = st.columns([0.5, 3.5, 0.5])  # Adjust the width ratio as needed
        with col2:
            if image:
                st.image(image, use_container_width=True)
        
        st.write(content)
        st.write("-------------------------")
        time.sleep(21)

    end_time = time.time()  # End timing
    execution_time = end_time - start_time
    st.write(f"Execution time: {execution_time:.2f} seconds")



