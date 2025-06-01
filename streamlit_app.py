import streamlit as st
import requests
import pandas as pd
import altair as alt

# ========== Streamlit UI Setup ==========
st.set_page_config(page_title="🎬 TMDb Movie Explorer", layout="centered")
st.title("🎥 :rainbow[TMDb Movie Explorer App]")
st.markdown("Search movies by title and explore ratings, genres, and details.")

# ========== Developer API Key ==========
API_KEY = "4f658b3a4df357c0e36dea39fe745497"

# ========== User Input ==========
query = st.text_input("Enter a movie title:", "Sheriff: Narko Integriti")

# ========== TMDb API Call Functions ==========

def search_movie(query, api_key):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={query}"
    response = requests.get(url)
    return response.json()

def get_movie_details(movie_id, api_key):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    return response.json()

# ========== Fetch and Display Data ==========
if st.button("Search Movie"):
    search_result = search_movie(query, API_KEY)

    if "results" not in search_result or len(search_result["results"]) == 0:
        st.error("❌ No movie found with that title.")
    else:
        movie = search_result["results"][0]
        movie_id = movie["id"]
        details = get_movie_details(movie_id, API_KEY)

        # ========== Movie Info ==========
        st.subheader(f"🎞 {details['title']} ({details['release_date'][:4]})")
        st.image(f"https://image.tmdb.org/t/p/w500{details['poster_path']}")
        st.markdown(f"*Overview*: {details['overview']}")
        st.markdown(f"*Runtime*: {details['runtime']} mins")
        st.markdown(f"*Vote Average*: {details['vote_average']}")
        st.markdown(f"*Total Votes*: {details['vote_count']}")

        # ========== Visualization 1: Vote Rating vs Count ==========
        vote_data = pd.DataFrame({
            "Metric": ["Average Rating", "Vote Count"],
            "Value": [details["vote_average"], details["vote_count"]]
        })

        st.subheader("📊 Rating and Vote Count")
        bar_chart = alt.Chart(vote_data).mark_bar().encode(
            x="Metric",
            y="Value",
            color="Metric",
            tooltip=["Metric", "Value"]
        ).properties(width=600)
        st.altair_chart(bar_chart)

        # ========== Visualization 2: Genre Breakdown ==========
        genres = [g["name"] for g in details["genres"]]
        genre_df = pd.DataFrame({"Genre": genres, "Count": [1]*len(genres)})

        st.subheader("🎨 Genre Breakdown")
        pie_chart = alt.Chart(genre_df).mark_arc().encode(
            theta="Count",
            color="Genre",
            tooltip="Genre"
        )
        st.altair_chart(pie_chart)
