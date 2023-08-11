from textblob import TextBlob


    texto = "Tu texto aquí"
    blob = TextBlob(texto)
    sentimiento = blob.sentiment

    print(sentimiento.polarity)
