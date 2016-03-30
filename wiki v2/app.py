# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import wikiscrape


app = Flask(__name__)

@app.route('/')
def hello_world(): 
    return render_template('index.html')
    
@app.route('/search', methods=['POST', 'GET'])
def search():
    topic = request.form['topic']
    result = wikiscrape.topic_search(topic)
    return result
    
if __name__ == '__main__':
    app.run(debug=True)