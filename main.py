import streamlit as st
import os
import time

# Title and introduction
st.title("🎉 Welcome to the Birthday Cake Page! 🎂")
st.write("Let's celebrate with a virtual birthday cake! 🎈🍰")

# Collect user's name for a personalized experience
user_name = st.text_input("What's your name?", "")

# Collect user's birthday wish
birthday_wish = st.text_input("What's your special birthday wish?", "")

# Path to the HTML file
html_file = 'birthday-cake.html'

# Check if the file exists
if os.path.exists(html_file):
    # Button to open the Birthday Cake page with more engaging interaction
    button = st.button('🎁 Open Your Birthday Cake Page! 🎂')

    if button:
        if user_name and birthday_wish:
            # Show a fun spinner while the page is being opened
            with st.spinner(f"🎉 {user_name}, we're preparing your cake... Please wait! 🍰"):
                time.sleep(2)  # Simulate a slight delay

            # Display personalized birthday message before showing the cake
            st.write(f"🎉 **Happy Birthday, {user_name}!** 🎉")
            st.write(f"🎂 Your wish: *'{birthday_wish}'* is now part of the celebration!")
            
            # Read and display the HTML content (birthday cake page)
            with open(html_file, 'r') as file:
                html_content = file.read()

            # Show the birthday cake HTML content
            st.components.v1.html(html_content, height=600)

            # Show a success message
            st.success(f"🎂 **Enjoy your cake, {user_name}!** 🎉")

        else:
            st.warning("Please enter your name and a birthday wish to make it extra special! 🎉")

else:
    st.error(f"Oops! It seems the file '{html_file}' isn't found. Please check the file path.")
