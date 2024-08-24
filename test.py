import streamlit as st
import google.generativeai as genai
from PIL import Image, UnidentifiedImageError
import os
import io
from paragraph_gen import paragraph_gen
from prompt_gen import prompt_gen
from image_gen import img_gen
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("👻🔮 DreamMinds.AI")
st.subheader("", divider='rainbow')

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = st.text_input("Enter your Google API Key", type="password")

def title_gen(story):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
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
    json_otpt = paragraph_gen(dream)
    # st.write(json_otpt)
    
    title = title_gen(json_otpt)
    st.subheader(title)

    for key, content in json_otpt.items():

        image = generate_image_with_retry(content)
        if image:
            st.image(image)
        
        st.write(content)
        st.write("-------------------------")






# The Infinite School Hallway: My friends and I were stuck in a school where the hallways never ended. Every time we turned a corner, we found ourselves back at the same spot. The school bell kept ringing, but no one was around. We had to figure out how to escape before we were trapped there forever.

# The Disappearing Friends: We were at a theme park, enjoying the rides, when suddenly my friends started disappearing one by one. The park became empty and eerie. I had to solve the mystery and bring them back before I was left all alone.

# The Haunted Locker: I found an old, dusty locker at the back of the school that no one else seemed to notice. When I opened it, strange things started happening—books floating, lights flickering, and whispers in the dark. My friends and I had to uncover the locker’s secret before it took control of the school.

# The Mirror Maze: My friends and I entered a mirror maze at the carnival, but it turned out to be much more than just a game. The reflections started moving on their own, trapping us inside. We had to find the real exit before the mirrors trapped us forever.

# The Vanishing Neighborhood: One night, my friends and I noticed that houses in our neighborhood were disappearing, leaving behind only empty lots. We had to figure out what was causing the disappearances before our own homes vanished too.

# The Talking Animals: In my dream, all the animals in the zoo started talking and asking for our help. They were trapped and needed us to find the key to set them free. But time was running out, and we had to work together to save them before the zookeeper returned.

# The Mysterious Library: My friends and I discovered a hidden library in the school basement. Every book we opened transported us to a different world, but each one was more dangerous than the last. We had to find the right book to get back home.

# The Disappearing Text Messages: My friends and I were texting each other when our messages started disappearing, and we couldn't communicate anymore. We had to figure out what was happening and how to reconnect before something strange happened to us.

# The Hidden Door: While exploring an old house, my friends and I found a hidden door that led to a mysterious underground world. We had to navigate through the strange tunnels and creatures to find our way back to the surface.

# The Game That Became Real: My friends and I were playing a video game when suddenly, we were pulled into the game itself. The only way to escape was to complete the game’s challenges, but the game kept changing the rules, making it harder and harder to win.


# The Floating School: My friends and I were in a school that floated in the sky. Every time we tried to leave, the stairs turned into slides, sending us back to our classrooms. We had to solve a puzzle to make the school land safely.

# The Talking Animals: We found ourselves in a forest where all the animals could talk. They needed our help to find a missing treasure that could save their home from an evil wizard.

# The Magic Library: We discovered a hidden library where the books came to life. Each book took us to a different world, but we had to finish the story to return home.

# The Endless Maze: My friends and I were trapped in a giant maze that kept changing every time we took a wrong turn. We needed to work together to find the way out.

# The Haunted Playground: We were playing in a playground at night, but all the equipment started moving on its own. We had to find out what was causing the strange behavior before we could leave.

# The Lost Toy Store: We entered a toy store where the toys came alive after closing time. They needed our help to defeat a giant robot that was trying to take over.

# The Time-Traveling Classroom: Our classroom turned into a time machine, and we had to complete tasks in different historical periods to return to the present.

# The Hidden Cave: We discovered a cave filled with glowing crystals that could grant wishes, but we had to choose our wishes wisely to avoid getting trapped forever.

# The Mystery of the Vanishing School: One day, our school started disappearing piece by piece. We had to solve the mystery and find the missing parts before everything was gone.

# The Magical Paintings: We found a gallery where the paintings could pull us inside. Each painting was a different adventure, but we had to find the right one to get back to the real world.



