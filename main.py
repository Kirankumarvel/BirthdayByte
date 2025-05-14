import webbrowser
import os

# Path to the HTML file
html_file = 'birthday-cake.html'

# Check if the file exists
if os.path.exists(html_file):
    # Open the HTML file in the default web browser
    webbrowser.open('file://' + os.path.abspath(html_file))
else:
    print(f"File '{html_file}' not found.")
