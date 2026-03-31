# Mini Project: Filtering Spam Messages from Student Inbox
# Name: [Your Name]
# Idea: I wanted to see how spam messages like "win money" can be detected

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# I created this dataset based on messages I usually see
inbox_messages = [
    "Win a free phone now!!!",
    "Bro are you coming to class?",
    "You have won a prize claim fast",
    "Assignment submission is tomorrow",
    "Earn money online without effort",
    "Let's revise ML today"
]

# marking messages manually (my understanding)
# 1 = spam, 0 = normal
message_labels = [1, 0, 1, 0, 1, 0]

df = pd.DataFrame({
    "message_text": inbox_messages,
    "is_spam": message_labels
})

# I noticed spam messages often contain certain words
# so I made a small helper function
def detect_common_spam_words(text_msg):
    suspicious_terms = ["win", "free", "prize", "money", "earn"]
    
    for term in suspicious_terms:
        if term in text_msg.lower():
            return 1
    return 0

# checking how my manual rule performs
df["rule_based_flag"] = df["message_text"].apply(detect_common_spam_words)

# converting messages into numbers so model can understand
vectorizer_model = CountVectorizer()
numeric_data = vectorizer_model.fit_transform(df["message_text"])

target_output = df["is_spam"]

# training the model
spam_classifier = MultinomialNB()
spam_classifier.fit(numeric_data, target_output)

# testing on a new message (realistic example)
new_inbox_message = ["Get free money now by clicking this link"]

try:
    new_msg_vector = vectorizer_model.transform(new_inbox_message)

    ml_prediction = spam_classifier.predict(new_msg_vector)[0]
    rule_prediction = detect_common_spam_words(new_inbox_message[0])

    # combining both (my logic: if either says spam → spam)
    if ml_prediction == 1 or rule_prediction == 1:
        final_result = "Spam"
    else:
        final_result = "Not Spam"

    print("Message:", new_inbox_message[0])
    print("Prediction:", final_result)

except Exception as e:
    print("Something went wrong while processing the message:", e)
