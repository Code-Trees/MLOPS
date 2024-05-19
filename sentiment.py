import streamlit as st
import pickle
import re
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the logistic regression model
with open('Sentiment-LR-model.pickle', 'rb') as model_file:
    model = pickle.load(model_file)

# Load the TfidfVectorizer
with open('Incoder-ngram-(1,2).pickle', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Dictionary containing all emojis
emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad', 
          ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
          ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed', 
          ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
          '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
          '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink', 
          ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}

# Set containing all stopwords
stopwordlist = ['a', 'about', 'above', 'after', 'again', 'ain', 'all', 'am', 'an',
             'and','any','are', 'as', 'at', 'be', 'because', 'been', 'before',
             'being', 'below', 'between','both', 'by', 'can', 'd', 'did', 'do',
             'does', 'doing', 'down', 'during', 'each','few', 'for', 'from', 
             'further', 'had', 'has', 'have', 'having', 'he', 'her', 'here',
             'hers', 'herself', 'him', 'himself', 'his', 'how', 'i', 'if', 'in',
             'into','is', 'it', 'its', 'itself', 'just', 'll', 'm', 'ma',
             'me', 'more', 'most','my', 'myself', 'now', 'o', 'of', 'on', 'once',
             'only', 'or', 'other', 'our', 'ours','ourselves', 'out', 'own', 're',
             's', 'same', 'she', "shes", 'should', "shouldve",'so', 'some', 'such',
             't', 'than', 'that', "thatll", 'the', 'their', 'theirs', 'them',
             'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 
             'through', 'to', 'too','under', 'until', 'up', 've', 'very', 'was',
             'we', 'were', 'what', 'when', 'where','which','while', 'who', 'whom',
             'why', 'will', 'with', 'won', 'y', 'you', "youd","youll", "youre",
             "youve", 'your', 'yours', 'yourself', 'yourselves']

# Function to preprocess the input text
def preprocess_text(text):
    text = text.lower()
    # Replace all URLs with 'URL'
    text = re.sub(r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)", "URL", text)
    # Replace all emojis with their meanings
    for emoji, meaning in emojis.items():
        text = text.replace(emoji, "EMOJI" + meaning)
    # Replace @USERNAME with 'USER'
    text = re.sub(r'@[^\s]+', 'USER', text)
    # Replace all non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    return text

# Function to predict sentiment
def predict_sentiment(sentence):
    # Preprocess the input sentence
    preprocessed_sentence = preprocess_text(sentence)
    # Vectorize the preprocessed sentence
    vectorized_sentence = vectorizer.transform([preprocessed_sentence])
    # Predict sentiment
    sentiment = model.predict(vectorized_sentence)[0]
    return sentiment

# Function to display sentiment prediction result
def display_result(sentiment):
    if sentiment == 1:
        st.write("😊 The sentence seems happy!")
    else:
        st.write("😞 The sentence seems sad.")

def main():
    st.title("Sentiment Analysis App")
    st.write("Enter a sentence below to predict its sentiment:")

    # Text input field for user to enter a sentence
    sentence = st.text_input("Enter a sentence:")

    if st.button("Predict Sentiment"):
        if sentence:
            # Predict sentiment
            sentiment = predict_sentiment(sentence)
            # Display the result
            display_result(sentiment)
        else:
            st.write("Please enter a sentence.")

if __name__ == "__main__":
    main()
