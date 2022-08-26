

from flask import Flask,request,jsonify,render_template
import numpy as np
import pickle
import re

from yaml import load
## Loading model
loaded_model = pickle.load(open("Statics/sentiment_analysis.sav",'rb'))


app = Flask(__name__)



@app.route("/",methods=['GET'])
def home():
    return render_template('index.html')







@app.route("/sentiment/<news>",methods=['GET'])
def sentiment(news):
    sentiment_ =loaded_model.predict([news])[0]
    print(type(sentiment_))
    _sentiment_='Netural'
    if sentiment_==1:
        _sentiment_='Positive'
    elif sentiment_==0:
        _sentiment_='Netural'
    elif sentiment_==-1:
        _sentiment_='Negative'
    return jsonify({'News':news,'Sentiment_score':sentiment_,'Sentiment':_sentiment_})

if __name__=='__main__':
    app.run(debug=True)