import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import re

data = pd.read_csv("phishing.csv")  # Must contain 'url' and 'label' columns

def extract_features(url):
    return [
        int('https' in url),
        len(url),
        int('@' in url),
        int(re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url) is not None),
        url.count('.'),
        int('-' in url)
    ]

X = data['url'].apply(extract_features).tolist()
y = data['label']

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))
print("✅ Trained model saved as model.pkl")
