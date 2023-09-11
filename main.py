import streamlit as st
import requests

API_KEY = "xUcQJT0jkvnh706V8NwiilbAAJ4LdkmITjPUDD6w"
url = "https://api.nasa.gov/planetary/apod?" \
      "api_key=xUcQJT0jkvnh706V8NwiilbAAJ4LdkmITjPUDD6w"


response = requests.get(url)
content = response.json()
img_url = content["hdurl"]
info = content["explanation"]

st.title("This is the image")
st.image(img_url)
st.info(info)

