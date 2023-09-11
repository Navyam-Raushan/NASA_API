import streamlit as st
import requests

API_KEY = "xUcQJT0jkvnh706V8NwiilbAAJ4LdkmITjPUDD6w"
url = "https://api.nasa.gov/planetary/apod?" \
      f"{API_KEY}"


# Getting data for the page
response = requests.get(url)
content = response.json()
img_url = content["hdurl"]
info = content["explanation"]
title = content["title"]

st.title(title)
st.image(img_url)
st.info(info)

