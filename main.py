import streamlit as st
import os
import time

# 🎉 Welcome Section
st.title("🥳 Welcome to the Birthday Celebration Hub! 🎂")
st.subheader("🎊 Woohoo!")
st.balloons()
st.markdown("Your Birthday Surprise is Here! Enter your details below to get started! 🎁✨")

# 🌟 Collect User Info
user_name = st.text_input("🎈 What's your name?")
birthday_wish = st.text_input("💫 Make a wish...")

# Path to the HTML file
html_file = 'birthday-cake.html'

# Display content only after clicking the button
if st.button("🎁 Reveal Your Birthday Surprise! 🎉"):
    if user_name and birthday_wish:
        # Show loading spinner
        with st.spinner(f"🌟 Hang tight, {user_name}! We're whipping up some birthday magic... 🎩✨"):
            time.sleep(2)

        # 🎉 Display personalized message
        st.success(f"🎉 Happy Birthday, {user_name}! 🎂")
        st.write(f"💭 Your wish: *'{birthday_wish}'* is officially out in the universe!")

        # 🚀 Check if the file exists
        if os.path.exists(html_file):
            # 🎂 Display the Birthday Cake Page
            with open(html_file, 'r') as file:
                html_content = file.read()
            st.components.v1.html(html_content, height=600)

            # 🎈 End Celebration
            st.balloons()
            st.markdown("""
            ### 🎊 Woohoo! Your Birthday Surprise is Unlocked! 🎉  
            Let’s make your special day unforgettable with a slice of digital cake! 🍰  
            Thanks for celebrating with us at [BirthdayByte](https://birthdaybyte.streamlit.app/)!  
            Keep dreaming big, smiling wide, and partying hard! 🥳🎂
            """)
        else:
            st.error("🚨 Oops! The birthday cake file seems to be missing. Check the file path and try again.")
    else:
        st.warning("📝 Don’t forget to share your name and a wish to unlock the surprise! 💖")
