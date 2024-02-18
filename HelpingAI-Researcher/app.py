import os
import streamlit as st
import requests

#hello world

# Create a session for reusing connections
session = requests.Session()

# Function to interact with the AI
def chat_with_ai(message, user_input):
    api_url = os.getenv("CHAT_API_URL") # Vortex 3b models API
    payload = {"message": message, "user_input": user_input}

    try:
        with session.post(api_url, json=payload) as response:
            if response.status_code == 200:
                return response.json().get('response')  # Access 'response' key
            else:
                st.error("Failed to get a response from the AI API. 😞")
    except requests.RequestException as e:
        st.error(f"Error: {e}")

# Function to perform web search
def web_search(query):
    url = os.getenv("SEARCH_API_URL") # Webscout API
    payload = {"query": query}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: {response.status_code}")

# Main function
def main():
    st.set_page_config(page_title='HelpingAI Research Assistant', page_icon=":mag:")
    st.title("🔍 HelpingAI Research Assistant")
    st.sidebar.header("🛠️ Settings")
    query = st.sidebar.text_input("🔎 Enter your research query: ")
    generate_report = st.sidebar.button("📝 Generate Report")

    st.sidebar.markdown("---")
    st.sidebar.header("📚 Recent Reports")
    recent_reports = st.sidebar.empty()  # Placeholder for recent reports

    st.sidebar.markdown("---")
    st.sidebar.header("ℹ️ About this App")
    st.sidebar.info("This app uses chat and web search APIs by HelpingAI. The founder of HelpingAI is Abhay Koul. The web search API used in this app is publicly available and its name is Webscout API. For any inquiries or assistance, please contact the developer: Telegram: @OEvortex, Email: helpingai5@gmail.com.")

    st.sidebar.markdown("---")
    st.sidebar.header("🌐 How to Get Webscout API")
    st.sidebar.info("""
    1. Sign up for a RapidAPI account if you haven't already.
    2. Subscribe to the "webscout-api" on the RapidAPI marketplace to acquire your API key.
    3. Choose the pricing tier that best fits your usage needs and budget.
    4. Integrate the API into your applications using the provided endpoints.
    """)

    st.sidebar.markdown("---")
    st.sidebar.markdown("© 2024 HelpingAI. All rights reserved.")

    if generate_report:
        if query:
            with st.spinner('🔄 Searching...'):
                # Perform web search
                search_results = web_search(query)
            
            # Pass the search results to the AI for generating a report
            prompt = f"Generate a detailed research report based on the following information: {search_results}. The user's query was: '{query}'. Please include an overview, key findings, and any relevant details in the report. If the search results are insufficient, answer the user's question using the information available."
            with st.spinner('🔄 Generating report...'):
                report = chat_with_ai(prompt, query)
            
            # Display the report
            if isinstance(report, dict) and 'error' in report:
                st.error(report['error'])
            else:
                st.write(report)

            # Update recent reports
            recent_reports.text(query)
        else:
            st.sidebar.error("❗ Please enter a research query.")

if __name__ == "__main__":
    main()
