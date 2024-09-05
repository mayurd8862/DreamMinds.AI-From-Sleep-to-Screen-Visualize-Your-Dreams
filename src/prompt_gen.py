import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = st.text_input("Enter your Google API Key", type="password")

# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def prompt_gen(paragraph_content):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    # prompt = f"""Generate a clear and concise image description based on the following content. The description should be direct and to the point.

    # Content:
    # {paragraph_content}
    # """

    prompt = f"""Generate a straightforward and simple image description based on the content provided below. Use basic words and keep the description clear and easy to understand so it can be effectively used by a text-to-image model. The characters should look lifelike but maintain a cartoon style.

    Content:
    {paragraph_content}
    """

    result = llm.invoke(prompt)
    return result.content



# paragraph = "The air hung heavy, thick with the smell of damp earth and decaying leaves. Sunlight struggled to pierce the dense canopy, casting long, eerie shadows that danced across the jungle floor. We, a group of friends, huddled together, our hearts pounding in our chests. Fear had taken root, twisting our laughter into nervous whispers. We had ventured into this ancient jungle, lured by whispers of hidden treasures and forgotten secrets, but the whispers had turned into screams."


# print(prompt_gen(paragraph))

