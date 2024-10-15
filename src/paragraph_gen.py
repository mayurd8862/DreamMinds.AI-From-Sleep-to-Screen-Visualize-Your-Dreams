
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
import streamlit as st
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import os


if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = st.text_input("Enter your Google API Key", type="password")


def paragraph_gen(dream_description):

    pmt = f"""
    Your task is to craft a compelling short story based on the dream described below. This story should be engaging and imaginative, capturing the essence and emotions of the dream. Use clear and simple English, ensuring that the narrative is easily understood by school students, yet rich enough to spark their imagination. 

    Divide the story into exactly 5 paragraphs, each focusing on a different aspect or scene from the dream.
    Return the story as a JSON object with keys 'paragraph1', 'paragraph2', 'paragraph3', 'paragraph4', and 'paragraph5'.

    dream description:
    {dream_description}
    """

        # The story should be divided into multiple paragraphs, each described in detail.Each paragraph should cotain different pair like - paragraph1 : "paragraph content"


    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    parser = JsonOutputParser()

    prompt = PromptTemplate(
        template="Answer the user query.\n{format_instructions}\n{query}\n",
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | model | parser

    para_json = chain.invoke({"query": pmt})

    return para_json



# # The dream description
# dream = "I was in a dangerous jungle with my friends, the air thick with tension. As we ventured deeper, the eerie sounds of zombies grew louder, echoing through the trees. Fear gripped us as we realized we were not alone; shadows moved in the darkness, and every rustle of leaves sent chills down our spines."


# json_otpt = paragraph_gen(dream)
# # print(json_otpt)


# for key, content in json_otpt.items():
#     print(f"{key}:\n{content}\n")







