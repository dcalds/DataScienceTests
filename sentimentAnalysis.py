# Sentimental Analysis Test

from textblob import TextBlob

'''
test = "`Python is great."

tb = TextBlob(test)

# Returns the sentiment of text
sentiment = tb.sentiment.polarity

# Value between -1.0 and 1.0
# Posive values indicates positive comments
# Same to negatives
'''

while True:
    data = input(str("Say something: "))
    blob_data = TextBlob(data)
    sentiment = blob_data.sentiment.polarity
    if sentiment > 0.4:
        print("Thats great!")
    else:
        print("This is such a dumb thing...")
