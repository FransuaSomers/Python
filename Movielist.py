import pandas as pd
import numpy as np
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

import nltk
nltk.download('stopwords')
#reviews_df = pd.read_csv('/Desktop/Python/movie_reviews.csv')


# Load the dataset of movie reviews
reviews_df = pd.read_csv('movie_reviews.csv')

# Clean and preprocess the text data
corpus = []
for i in range(len(reviews_df)):
    review = re.sub('[^a-zA-Z]', ' ', reviews_df['review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Convert the text data into numerical features using the bag-of-words model
cv = CountVectorizer(max_features = 5000)
X = cv.fit_transform(corpus).toarray()

# Apply term frequency-inverse document frequency (TF-IDF) weighting to the features
tfidf_transformer = TfidfTransformer()
X_tfidf = tfidf_transformer.fit_transform(X).toarray()

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, reviews_df['sentiment'], test_size = 0.2, random_state = 0)

# Train a Naive Bayes classifier on the training data
clf = MultinomialNB()
clf.fit(X_train, y_train)

# Evaluate the performance of the classifier on the test data
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
