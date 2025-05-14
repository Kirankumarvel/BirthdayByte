import streamlit as st
import os
import time

# Your Streamlit app content
st.title("🎂 Welcome to the Birthday Cake Page! 🎂")

# Add a brief description or message
st.write("Click the button below to open the Birthday Cake Page 🎉")

# Path to the HTML file
html_file = 'birthday-cake.html'

# Check if the file exists
if os.path.exists(html_file):
    # Button to render the HTML content with some flair
    button = st.button('🎈 Click to Unwrap the Birthday Cake! 🎁')
    
    if button:
        # Show a loading spinner while the content is being processed
        with st.spinner("🎉 Unwrapping the cake... Please wait! 🎂"):
            # Simulate a slight delay for a more interactive feel
            time.sleep(2)
            
            # Read the HTML file
            with open(html_file, 'r') as file:
                html_content = file.read()

            # Display the birthday cake HTML content
            st.components.v1.html(html_content, height=600)  # You can adjust height as needed
            
            # Display a thank you message after showing the content
            st.success("🎂 Happy Birthday! Enjoy your cake! 🎉")

else:
    st.error(f"Oops! It seems the file '{html_file}' isn't found.")
