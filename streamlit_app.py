import streamlit as st
import wikipedia

st.title("📚 Wikipedia Explorer")

# User input
query = st.text_input("Search for a topic:", "Python programming")

if query:
    try:
        # Get summary
        summary = wikipedia.summary(query, sentences=3)
        page = wikipedia.page(query)

        st.subheader(f"🔍 Summary of {query.title()}:")
        st.write(summary)

        # Show more info
        st.markdown("📎 [Read Full Article on Wikipedia](%s)" % page.url)

        # Optional: Show links to related topics
        st.subheader("📌 Related Topics:")
        st.write(", ".join(page.links[:10]))  # Show first 10 related pages

    except wikipedia.exceptions.DisambiguationError as e:
        st.warning("Too many options. Please be more specific.")
        st.write("Options:", e.options[:5])
    except wikipedia.exceptions.PageError:
        st.error("No page found for this topic.")
