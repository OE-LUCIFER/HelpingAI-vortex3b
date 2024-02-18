import streamlit as st
import requests
import time
import os
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
    st.title("AI Study Notes Generator 📚")
    st.sidebar.image("logo.png", use_column_width=True)  # Display a logo in the sidebar
    st.sidebar.markdown("## Class Selection")
    st.sidebar.markdown("Please select your class and enter the study topic.")

    # User inputs for class and topic
    user_class = st.sidebar.selectbox('Select your class:', ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6',
                                                             'Class 7', 'Class 8', 'Class 9', 'Class 10', 'Class 11', 'Class 12'])
    user_input = st.sidebar.text_input(f'Enter your study topic for {user_class}:', placeholder='e.g., History')

    # User selects the type of notes
    note_type = st.sidebar.selectbox('Select the type of notes:', ['Detailed Explanation', 'Summary', 'Key Points'])

    # User selects the format of the notes
    note_format = st.sidebar.selectbox('Select the format of the notes:', ['Text', 'Bulleted List', 'Numbered List'])

    # Generate study notes when prompted
    if st.sidebar.button('Generate Study Notes'):
        if user_input.lower() in ['quit', 'exit', 'bye']:
            st.success("Goodbye! Have a great day!")
        else:
            with st.spinner("Requesting HelpingAI..."):
                time.sleep(2)  # Wait for 2 seconds
            with st.spinner("Generating study notes. Please wait..."):
                # Detailed and descriptive prompt
                prompt = f"Using advanced AI capabilities, generate {note_type.lower()} for students of {user_class}. The topic of study is '{user_input}'. The notes should be presented in a {note_format.lower()} format to facilitate easy understanding and learning. The content should be accurate, comprehensive, and tailored to the academic level of {user_class}. The goal is to provide a valuable learning resource that can help students grasp the topic effectively."
                response = chat_with_ai(prompt)

                # Display generated study notes
                st.subheader(f"{note_type} in {note_format} format for {user_class} - {user_input}")
                st.markdown(response)

    # About section
    st.sidebar.markdown("## About")
    st.sidebar.markdown("This application uses AI to generate study notes based on the class and topic you provide. It's designed to help students get a quick overview of a topic. The application is made by Abhay Koul, also known as OEvortex, and it uses the API of HelpingAI, a company by OEvortex. You can learn more about OEvortex on YouTube.")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("© 2023 AI Study Notes Generator by OEvortex, HelpingAI")

    # Main area
    st.markdown("---")
    st.markdown("## Welcome to the AI Study Notes Generator! 📚")
    st.markdown("To get started, please select your class and enter your study topic in the sidebar. Then, choose the type and format of the notes you want to generate, and click 'Generate Study Notes'.")
    st.markdown("The AI will generate study notes based on your inputs and display them here. You can then use these notes to study and learn about your chosen topic. Happy studying! 🚀")

if __name__ == "__main__":
    main()