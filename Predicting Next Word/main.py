import pickle
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import json

# Load model and tokenizer
@st.cache_resource
def load_lstm_model():
    return load_model('lstm_new_model.h5')

@st.cache_resource
def load_tokenizer():
    # Load the tokenizer
    with open('tokenizer.pkl', 'rb') as file:
        tokenizer = pickle.load(file)
    return tokenizer


# Initialize components
model = load_lstm_model()
tokenizer = load_tokenizer()


# Function to predict top N words
def predict_top_words(input_text, top_n=5):
    # Tokenize and pad the input text
    token_text = tokenizer.texts_to_sequences([input_text])[0]
    padded_token_text = pad_sequences([token_text], maxlen=60, padding="pre")

    # Get prediction probabilities
    predictions = model.predict(padded_token_text)

    # Get the top N predicted indices
    top_indices = predictions[0].argsort()[-top_n:][::-1]

    # Map indices to words
    predicted_words = []
    for idx in top_indices:
        for word, index in tokenizer.word_index.items():
            if index == idx:
                predicted_words.append(word)
                break
    return predicted_words

# Streamlit App
st.title("Word Prediction App")
st.write("Type continuously in the text box below, and see the top 4 predicted words displayed below.")

# Input text box
input_text = st.text_input("Type here:", value="", key="input_text")

# Display predictions
if input_text.strip():
    st.write("Predicted Next Words:")
    predicted_words = predict_top_words(input_text, top_n=5)

    # Highlight predictions and display in one line
    highlighted_words = " ".join([
        f"<span style='background-color: rgb(239, 176, 54); padding: 5px; border-radius: 5px; color: #000; width:100vw;'>{word}</span>"
        for word in predicted_words
    ])
    
    st.markdown(
        f"<div style='font-size: 16px;'>{highlighted_words}</div>",
        unsafe_allow_html=True
    )
