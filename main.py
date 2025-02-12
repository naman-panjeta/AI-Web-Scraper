import streamlit as st
from scrape import scrape_website, clean_body, extract_body, split_dom_content
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    
    result = scrape_website(url)
    if not result:
        st.error("Failed to retrieve website content.")
    else:
        body_content = extract_body(result)
        clean_content = clean_body(body_content)

        st.session_state.dom_content = clean_content

        with st.expander("View DOM Content"):
            st.text_area("DOM Content", clean_content, height=300)

if "dom_content" in st.session_state:
    parse_desc = st.text_area("Describe what you want to parse?")
    if st.button("Parse Content"):
        if parse_desc:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_desc)
            st.write(result)