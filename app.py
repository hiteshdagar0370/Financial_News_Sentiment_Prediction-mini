import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Financial News Sentiment Prediction")

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

classifier = load_model()

st.title("Financial News Sentiment Prediction using BERT")

text = st.text_area("Enter Financial News or Tweet")

if st.button("Predict Sentiment"):
    if text.strip():

        result = classifier(text)

        label = result[0]["label"]

        if label.lower() == "positive":
            sentiment = "Bullish"
        elif label.lower() == "negative":
            sentiment = "Bearish"
        else:
            sentiment = "Neutral"

        st.success(f"Predicted Sentiment: {sentiment}")
        st.write(f"Confidence Score: {result[0]['score']:.2f}")
    else:
        st.warning("Please enter some text")
