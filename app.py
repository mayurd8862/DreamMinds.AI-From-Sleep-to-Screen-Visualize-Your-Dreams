import streamlit as st
import google.generativeai as genai
from PIL import Image
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import io
from src.paragraph_gen import paragraph_gen
from src.prompt_gen import prompt_gen
from src.image_gen import img_gen


st.title("👻🔮 DreamMinds.AI")
st.subheader("", divider = 'rainbow')

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = st.text_input("Enter your Google API Key", type="password")

# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def title_gen(story):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    prompt = f"""
    Your task is to craft a compelling title for the story provided below. The title should capture the core theme and emotion of the story, which is based on a user's dream description. The title must be creative, evocative, and concise, consisting of just 3-4 impactful words. output should contain only one title.

    Story:
    {story}
    """

    result = llm.invoke(prompt)
    return result.content


dream = st.text_area("Enter your Dream description in short: ")

if st.button("Analyze Dream"):

    json_otpt = paragraph_gen(dream)
    st.write(json_otpt)
    
    title = title_gen(json_otpt)
    st.subheader(title)

    for key, content in json_otpt.items():
        print(f"{key}:\n{content}\n")

        pmt = prompt_gen(content)

        decoded_img = img_gen(pmt)

        image = Image.open(io.BytesIO(decoded_img))
        st.image(image)
        st.write(content)
        st.write("-------------------------")

        # save_path = f"{key}.png"
        # image.save(save_path)

