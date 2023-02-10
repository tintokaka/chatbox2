import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer  # to reduce words to the stem

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD


lemmatizer = WordNetLemmatizer()

intents = json.loads(open("intents.json").read())


words = []
classes = []
documents = []
ignore_letters = ['!', '?', '.', ',']

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent["tag"]))
        if intent["tag"] not in classes:
            classes.append(intent["tag"])
            
print(words)
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
words = sorted(set(words))
classes = sorted(set(words))

pickle.dump(words, open('words.pkl'), 'wb')
pickle.dump(classes, open('classes.pkl'), 'wb')