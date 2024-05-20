import streamlit as st
from joblib import load

# Load the trained model
pipeline = load('regression.joblib')

# Streamlit app
st.title("Sentiment Analysis App")

st.write("This app predicts the sentiment of a sentence as Neutral, Negative, Positive, or Irrelevant.")

# Input fields for the name and the sentence
name = st.text_input("Enter your name:")
sentence = st.text_input("Enter a sentence:")

# Button to perform prediction
if st.button("Predict Sentiment"):
    if sentence:
        # Predict the sentiment
        prediction = pipeline.predict([sentence])[0]
        
        # Display the result
        st.write(f"Hello {name}, the sentiment of the given sentence is **{prediction}**.")
    else:
        st.write("Please enter a sentence to analyze.")

# Run the Streamlit app using the following command:
# streamlit run your_script_name.py
