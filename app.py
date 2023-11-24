import streamlit as st
import nltk
from nltk import ngrams
from nltk.tokenize import word_tokenize

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Function to generate n-grams
def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return n_grams

# Streamlit app
def main():
    st.title("N-gram Extractor")

    # User input
    text_input = st.text_area("Enter your text here:", "")

    # Select n-gram order
    n_gram_order = st.selectbox("Select n-gram order:", [2, 3, 4, 5])

    # Process and display n-grams
    if st.button("Generate N-grams"):
        if text_input:
            n_grams = generate_ngrams(text_input, n_gram_order)
            st.write(f"{n_gram_order}-grams:")
            st.write(n_grams)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
