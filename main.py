import streamlit as st
import os

# Your Streamlit app content
st.title("Birthday Cake Page")

# Path to the HTML file
html_file = 'birthday-cake.html'

# Check if the file exists
if os.path.exists(html_file):
    # Button to render the HTML content
    if st.button('Open Birthday Cake Page'):
        # Read the HTML file
        with open(html_file, 'r') as file:
            html_content = file.read()

        # Render HTML inside Streamlit app
        st.components.v1.html(html_content, height=600)  # You can adjust height as needed
else:
    st.error(f"File '{html_file}' not found.")
