import streamlit as st
import webbrowser
import os

# Your Streamlit app content
st.title("Birthday Cake Page")

# Path to the HTML file
html_file = 'birthday-cake.html'

# Check if the file exists
if os.path.exists(html_file):
    # Button to open the HTML file in the browser
    if st.button('Open Birthday Cake Page'):
        webbrowser.open('file://' + os.path.abspath(html_file))
else:
    st.error(f"File '{html_file}' not found.")
