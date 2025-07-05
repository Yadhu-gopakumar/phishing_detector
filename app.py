#from flask import Flask, request, render_template
#import pickle
#import re
#
#app = Flask(__name__)
#model = pickle.load(open('model.pkl', 'rb'))
#
#def extract_features(url):
#    return [
#        int('https' in url),
#        len(url),
#        int('@' in url),
#        int(re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url) is not None),
#        url.count('.'),
#        int('-' in url)
#    ]
#
#@app.route('/', methods=['GET', 'POST'])
#def home():
#    if request.method == 'POST':
#        url = request.form['url']
#        features = extract_features(url)
#        result = model.predict([features])[0]
#        return render_template('result.html', url=url, result='Phishing' if result else 'Legitimate')
#    return render_template('index.html')
#
#if __name__ == '__main__':
#    app.run(debug=True)

from flask import Flask, request, jsonify
import pickle, re
from flask_cors import CORS  # ✅ Add this


app = Flask(__name__)
CORS(app)
model = pickle.load(open('model.pkl', 'rb'))

def extract_features(url):
    return [int('https' in url), len(url), int('@' in url),
            int(re.match(r'http[s]?://\d+\.\d+\.\d+\.\d+', url) is not None),
            url.count('.'), int('-' in url)]

@app.route('/check', methods=['POST'])
def check_url():
    url = request.json['url']
    features = extract_features(url)
    result = model.predict([features])[0]
    return jsonify({'result': 'Phishing' if result else 'Legitimate'})

app.run()

