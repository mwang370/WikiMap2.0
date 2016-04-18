# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import wikiscrape, json


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
    topic = request.form['topic']
    result = wikiscrape.topic_search(topic)
    return result

@app.route('/search2', methods=['POST', 'GET'])
def search2():
    topic = request.args.get('b')
    result = wikiscrape.topic_search(topic)
    return result

@app.route('/summary', methods=['POST', 'GET'])
def summary():
    name = request.args.get('a')
    summ = wikiscrape.summary(name)
    return json.dumps({'summary': summ})

if __name__ == '__main__':
    app.run(debug=True)
