import streamlit as st
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def prompt_gen(paragraph_content):
    llm = ChatGroq(model="mixtral-8x7b-32768")
    prompt = f"""Generate a straightforward and simple image description based on the content provided below. Use basic words and keep the description clear and easy to understand so it can be effectively used by a text-to-image model. It should strictly generate cartoon like characters. 

    Content:
    {paragraph_content}
    """

    result = llm.invoke(prompt)
    return result.content



# paragraph = "The air hung heavy, thick with the smell of damp earth and decaying leaves. Sunlight struggled to pierce the dense canopy, casting long, eerie shadows that danced across the jungle floor. We, a group of friends, huddled together, our hearts pounding in our chests. Fear had taken root, twisting our laughter into nervous whispers. We had ventured into this ancient jungle, lured by whispers of hidden treasures and forgotten secrets, but the whispers had turned into screams."


# print(prompt_gen(paragraph))

