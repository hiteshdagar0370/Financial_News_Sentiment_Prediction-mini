Financial News Sentiment Prediction using Deep Learning & BERT
Project Overview
This project predicts the sentiment of finance-related tweets and news articles using Deep Learning and BERT.

The system classifies text into:

Bullish
Bearish
Neutral
Skills Used
Natural Language Processing (NLP)
Deep Learning
Sentiment Analysis
LSTM
BERT
Hugging Face Transformers
Streamlit
Domain
Finance & FinTech

Problem Statement
Build a sentiment classification system that labels finance-related tweets as:

Bearish
Bullish
Neutral
Dataset
Twitter Financial News Sentiment Dataset

Total Records: 11,932
Training Samples: 9,938
Validation Samples: 2,486
Models Used
1. LSTM Model
A baseline deep learning model built using embedding and recurrent neural networks.

2. BERT Model
A transformer-based model that captures contextual meaning and improves sentiment prediction accuracy.

Results
Model	Accuracy	F1 Score
LSTM	82%	0.80
BERT	95%	0.94
Project Structure
Financial_News_Sentiment_Prediction/

├── Financial_News_Sentiment_Prediction_Complete.ipynb
├── app.py
├── requirements.txt
├── README.md
├── Financial_News_Sentiment_Report.pdf
Installation
pip install -r requirements.txt
Run Application
streamlit run app.py
Conclusion
The BERT model outperformed the LSTM model because it understands contextual relationships in financial text more effectively. The project successfully predicts Bullish, Bearish, and Neutral sentiments from financial news and tweets.
