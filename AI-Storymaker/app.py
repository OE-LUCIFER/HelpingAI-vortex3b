import streamlit as st
import requests
import time
import os
# Create a session for reusing connections
session = requests.Session()

# Function to interact with the AI
def chat_with_ai(message):
    api_url = os.getenv("CHAT_API_URL")
    payload = {"message": message}

    try:
        with session.post(api_url, json=payload) as response:
            if response.status_code == 200:
                return response.json().get('response')  # Access 'response' key
            else:
                return {"error": "Failed to get a response from the AI API."}
    except requests.RequestException as e:
        return {"error": f"Error: {e}"}

# Streamlit app
def main():
    st.title("AI Storymaker 🍿")
    st.sidebar.markdown("## Story Selection")
    st.sidebar.markdown("Please select your story genre, enter the story title, choose the main character, select the story length, choose the language, choose the setting, choose the theme, optionally provide a starting point for the story, choose the number of characters, add the names of the cast and their roles, and choose the type of ending.")

    # User inputs for genre, title, character, length, language, setting, theme, starting point, number of characters, cast, and ending
    story_genre = st.sidebar.selectbox('Select your story genre:', ['Adventure', 'Fantasy', 'Sci-Fi', 'Mystery', 'Romance', 'Horror'])
    story_title = st.sidebar.text_input(f'Enter your story title for {story_genre}:', placeholder='e.g., The Lost Treasure')
    main_character = st.sidebar.text_input('Enter the main character:', placeholder='e.g., Ravi')
    story_length = st.sidebar.selectbox('Select your story length:', ['Short', 'Medium', 'Long'])
    story_language = st.sidebar.selectbox('Select your story language:', ['English', 'Spanish', 'French', 'German', 'Italian', 'Portuguese','Hindi'])
    story_setting = st.sidebar.text_input('Enter the setting for your story:', placeholder='e.g., A haunted mansion')
    story_theme = st.sidebar.text_input('Enter the theme for your story:', placeholder='e.g., Friendship')
    story_start = st.sidebar.text_area('Optionally, enter a starting point for your story:', placeholder='e.g., Once upon a time...')
    num_characters = st.sidebar.slider('Choose the number of characters in your story:', 1, 10, 3)
    cast_names = st.sidebar.text_input('Enter the names of the cast (separated by commas):', placeholder='e.g., Ravi, Sita, Raj')
    cast_roles = st.sidebar.text_input('Enter the roles of the cast (separated by commas):', placeholder='e.g., Detective, Villain, Sidekick')
    story_ending = st.sidebar.selectbox('Choose the type of ending for your story:', ['Happy', 'Sad', 'Cliffhanger'])

    # Generate story when prompted
    if st.sidebar.button('Generate Story'):
        if story_title.lower() in ['quit', 'exit', 'bye']:
            st.success("Goodbye! Have a great day!")
        else:
            with st.spinner("Requesting HelpingAI..."):
                time.sleep(2)  # Wait for 2 seconds
            with st.spinner("Generating story. Please wait..."):
                # Detailed and descriptive prompt
                prompt = f"{story_start} Using advanced AI capabilities, continue a {story_length.lower()}, {story_genre.lower()} story titled '{story_title}' with '{main_character}' as the main character and {num_characters} characters in total. The cast includes {cast_names} with roles {cast_roles}. The story should be set in '{story_setting}' and convey the theme of '{story_theme}'. The story should have a {story_ending.lower()} ending. The story should be engaging, creative, and tailored to the genre of {story_genre}. The story should be written in {story_language}. The goal is to provide a captivating narrative that can entertain readers."
                response = chat_with_ai(prompt)

                # Display generated story
                st.subheader(f"{story_genre} Story - {story_title}")
                st.markdown(response)

    # Feedback system
    st.sidebar.markdown("## Feedback")
    st.sidebar.markdown("Did you enjoy the story? Your feedback helps us improve!")
    feedback = st.sidebar.radio('Select a rating:', ['1 - Poor', '2 - Fair', '3 - Good', '4 - Very Good', '5 - Excellent'])
    if st.sidebar.button('Submit Feedback'):
        st.sidebar.success("Thank you for your feedback!")

    # About section
    st.sidebar.markdown("## About")
    st.sidebar.markdown("This application uses AI to generate stories based on the genre, title, main character, length, language, setting, theme, a starting point, number of characters, the names and roles of the cast, and the type of ending you provide. It's designed to entertain readers with a variety of narratives. The application is made by Abhay Koul, also known as OEvortex, and it uses the API of HelpingAI, a company by OEvortex. You can learn more about OEvortex on YouTube.")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("© 2023 AI Storyteller by OEvortex, HelpingAI")

    # Main area
    st.markdown("---")
    st.markdown("## Welcome to the AI Storyteller! 📚")
    st.markdown("To get started, please select your story genre, enter your story title, choose the main character, select the story length, choose the language, choose the setting, choose the theme, optionally provide a starting point for the story, choose the number of characters, add the names of the cast and their roles, and choose the type of ending in the sidebar. Then, click 'Generate Story'.")
    st.markdown("The AI will generate a story based on your inputs and display it here. You can then enjoy the narrative crafted by the AI. Happy reading! 🚀")

if __name__ == "__main__":
    main()
