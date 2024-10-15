import os
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
# from langchain.output_parsers import JsonOutputParser
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the Gemini Pro model
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the JSON parser
parser = JsonOutputParser()

# Create the prompt template
template = """
Your task is to craft a compelling short story based on the dream described below. Follow these guidelines:

1. The story should be engaging and imaginative, capturing the essence and emotions of the dream.
2. Use clear and simple English, ensuring that the narrative is easily understood by school students.
3. The story should be rich enough to spark students' imagination.
4. Divide the story into exactly 5 paragraphs, each focusing on a different aspect or scene from the dream.


Dream description: {dream_description}

Return the story as a JSON object with keys 'paragraph1', 'paragraph2', 'paragraph3', 'paragraph4', and 'paragraph5'.

{format_instructions}

Story:
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["dream_description"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

def generate_story(dream_description: str) -> dict:
    # Generate the story
    _input = prompt.format_prompt(dream_description=dream_description)
    output = llm.invoke(_input.to_string())
    
    # Parse the output
    story = parser.parse(output)
    
    return story

# Example usage
if __name__ == "__main__":
    dream_description = "I was flying through a colorful marketplace filled with magical items."
    story = generate_story(dream_description)
    print(story)