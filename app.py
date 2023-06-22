import re
import requests
import streamlit as st

def get_direct_download_link(gdrive_link):
    # Extract file ID from the Google Drive link
    file_id = re.search(r"/file/d/([A-Za-z0-9_-]+)", gdrive_link)
    if file_id:
        file_id = file_id.group(1)
    else:
        return None

    # Construct the direct download link
    direct_link = f"https://drive.google.com/uc?export=download&id={file_id}"
    return direct_link

# Streamlit app
st.title("Google Drive Link to Direct Download Link Converter")
st.write("Enter a Google Drive file link to get the direct download link.")

# Input field for the Google Drive link
gdrive_link = st.text_input("Google Drive Link")

# Button to convert the link
if st.button("Convert"):
    if gdrive_link:
        direct_download_link = get_direct_download_link(gdrive_link)
        if direct_download_link:
            st.success(f"Direct Download Link: {direct_download_link}")
        else:
            st.error("Failed to convert the link. Please make sure it is a valid Google Drive file link.")
    else:
        st.warning("Please enter a Google Drive file link.")
