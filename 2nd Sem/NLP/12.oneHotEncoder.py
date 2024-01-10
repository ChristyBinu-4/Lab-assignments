from sklearn.feature_extraction.text import CountVectorizer

text = ['this is a very good book to study',
        'This is second sentence',
        'This is third sentence']

# Initialize CountVectorizer to perform one-hot encoding
vectorizer = CountVectorizer(binary=True)

# Fit and transform the text data
one_hot_encoded = vectorizer.fit_transform(text)

# Get the feature names (unique words)
feature_names = vectorizer.get_feature_names_out()

# Display the one-hot encoded vectors and feature names
print("One-hot encoded vectors:")
print(one_hot_encoded.toarray())
print("\nFeature names:")
print(feature_names)
