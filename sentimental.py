from sentiment_analysis_spanish import sentiment_analysis


class SentimentalProcessor:
    @staticmethod
    def process(text):
        sentiment = sentiment_analysis.SentimentAnalysisSpanish()
        return sentiment.sentiment(text)
        #print(sentiment.sentiment("me parece terrible esto que me estás diciendo"))


"""
Output and meaning:

The function sentiment(text) returns a number between 0 and 1. This is the probability of string variable text of being "positive". Low probabilities mean that the text is negative (numbers close to 0), high probabilities (numbers close to 1) mean that the text is positive. The space in between corespond to neutral texts.
    """