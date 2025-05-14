import streamlit as st
import os
import time

# 🎉 Welcome Section
st.title("🥳 Welcome to the Birthday Celebration Hub! 🎂")
st.subheader("Let’s make your special day unforgettable with a slice of digital cake! 🍰")

# 🌟 Collect User Info
user_name = st.text_input("🎈 What's your name?")
birthday_wish = st.text_input("💫 Make a wish...")

# Path to the HTML file
html_file = 'birthday-cake.html'

# 🚀 Check if the file exists
if os.path.exists(html_file):
    # 🕹️ Interactive Button
    if st.button("🎁 Reveal Your Birthday Surprise! 🎉"):
        if user_name and birthday_wish:
            with st.spinner(f"🌟 Hang tight, {user_name}! We're whipping up some birthday magic... 🎩✨"):
                time.sleep(2)

            # 🎉 Show personalized message
            st.success(f"🎉 Happy Birthday, {user_name}! 🎂")
            st.write(f"💭 Your wish: *'{birthday_wish}'* is officially out in the universe!")

            # 🎂 Display the Birthday Cake Page
            with open(html_file, 'r') as file:
                html_content = file.read()

            st.components.v1.html(html_content, height=600)
        else:
            st.warning("📝 Don’t forget to share your name and a wish to unlock the surprise! 💖")
else:
    st.error("🚨 Oops! The birthday cake file seems to be missing. Check the file path and try again.")
