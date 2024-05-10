from textblob import TextBlob
import re
import profanity_filter 

text = "This is some sample text for profanity analysis."
profane_words = ["damn", "hell", "crap"]

# Create a TextBlob object
blob = TextBlob(text)

# Now you can use various TextBlob methods on the 'blob' object
print(f"Sentiment: {blob.sentiment}")
print(f"Nouns: {blob.noun_phrases}")

# Check for profanity using regular expressions
#if any(re.search(word, blob.lower()) for word in profane_words):
if any(word in blob for word in profane_words):
    print("Warning: The text contains profanity.")
else:
    print("The text appears to be clean of profanity.")