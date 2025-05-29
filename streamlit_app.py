import streamlit as st
import requests
from urllib.parse import quote

st.title("🎵 Song Lyrics and Playback")

# User inputs
artist = st.text_input("Enter artist name:", "")
song = st.text_input("Enter song title:", "")

if artist and song:
    # Fetch lyrics from lyrics.ovh
    encoded_artist = quote(artist)
    encoded_song = quote(song)
    lyrics_url = f"https://api.lyrics.ovh/v1/{encoded_artist}/{encoded_song}"
    response = requests.get(lyrics_url)

    if response.status_code == 200:
        lyrics = response.json().get("lyrics", "Lyrics not found.")
        st.subheader("🎤 Lyrics:")
        st.text(lyrics)
    else:
        st.error("Could not find lyrics. Please check the artist and song name.")

    # Embed YouTube search
    st.subheader("▶️ Play Song:")
    search_query = f"{artist} {song} official"
    youtube_url = f"https://www.youtube.com/results?search_query={quote(search_query)}"
    st.markdown(f"[Search on YouTube]({youtube_url})", unsafe_allow_html=True)

    # Embed first result (alternative option using iframe, but YouTube restricts autoplay for search pages)
    st.components.v1.iframe(f"https://www.youtube.com/embed?listType=search&list={quote(search_query)}", height=400)
else:
    st.info("Please enter both artist and song title to get started.")
