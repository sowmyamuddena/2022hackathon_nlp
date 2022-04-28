import nltk
import vaderSentiment

# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# function to print sentiments
# of the sentence.
def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)


    print("Overall sentiment dictionary is : ", sentiment_dict)
#   print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
#    print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
#   print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    print("Sentence Overall Rated As", end=" ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")
        return 99

    else:
        print("Neutral")


# Driver code
if __name__ == "__main__":
    print("\n1st statement :")
    sentence = "Your site is not working when I try to upload documents.\
     I contacted support and they could not help me. \
      They left me on hold for 56 min prior to me hanging up and calling again."

    # function calling
    resp1=sentiment_scores(sentence)
    print(resp1)

    print("\n2nd Statement :")
    sentence = "I’m sorry you experienced that. \
    You shouldn’t have to deal with such trouble. \
    You said you’re trying to upload a document?"
    resp1=sentiment_scores(sentence)
    print(resp1)

    print("\n3rd Statement :")
    sentence = "I am very sad today."
    resp3=sentiment_scores(sentence)
    print(resp3)

