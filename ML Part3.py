# Let's create a model that predicts a music genre based on age and gender of people
# pip install sklearn.tree

import pandas as pd

from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_csv('music.csv')

print(music_data)

X = music_data.drop(columns=['genre'])

y = music_data['genre']

model = DecisionTreeClassifier()

# Create a model that takes age and gender (X) and predicts Genre (y)
model.fit(X, y)

predictions = model.predict([[21, 1], [22, 0]])

print(predictions)

