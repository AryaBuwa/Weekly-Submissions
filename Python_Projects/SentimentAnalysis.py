# A sentiment analysis code using nltk and VADER.

# Importing NLTK library and its SentimentIntensityAnalyzer from vader
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download the VADER Lexicon
nltk.download('vader_lexicon')

# Initializing the Sentiment Analyzer
analyser = SentimentIntensityAnalyzer()

# Initializing function for the Sentiment Analysis
def sentiment_analyser():
    print("Hello! I can tell if your sentence feels happy, sad, or neutral. Type 'exit' to stop chatting with me!")

    while True:
        # Taking input from the user
        sentence = input('Please Type Something for further analysis: ')
        if sentence.lower() == 'exit':
            print('Thank You for your response!')
            break
        # Error handling
        elif sentence.lower() == '':
            print('Please enter any sentence for Sentiment Analysis.')
            continue

        # Now analyzing the sentiment of the sentence
        sentiment = analyser.polarity_scores(sentence)

        # Extracting the compound score from the sentiment
        compound = sentiment['compound']

        # Now deploying scores in conditions according to the sentence for Sentiment Analysis
        if compound >= 0.7:
            Sentiment_Analysis = 'Joyful 😄'
        elif 0.5 <= compound < 0.7:
            Sentiment_Analysis = 'Happy 😊'
        elif 0.0 < compound < 0.5:
            Sentiment_Analysis = 'Trustworthy 🤝'
        elif compound == 0:
            Sentiment_Analysis = 'Surprise 😲'
        elif -0.3 < compound < 0:
            Sentiment_Analysis = 'Anticipation 🤔'
        elif -0.7 <= compound < -0.5:
            Sentiment_Analysis = 'Angry 😡'
        elif -0.5 <= compound < -0.3:
            Sentiment_Analysis = 'Sad 😔'
        else:
            Sentiment_Analysis = 'Neutral'

        # Displaying the results 
        print('Sentiment Scores:', sentiment)
        print('Sentiment Reaction:', Sentiment_Analysis)
        print('-' * 50)


# Running the Sentiment Analysis tool
sentiment_analyser()
