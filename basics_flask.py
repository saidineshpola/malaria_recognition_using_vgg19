from flask import Flask, render_template, request
import pickle
import numpy as np

#model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home_fn():
    return '''<h1>Hello There</h1><br><img src="https://mimo.app/r/hacker.png">
    <br><br><p> hacker image</p><em>We need more cats in the government</em>'''

if __name__=="__main__":
    app.run(debug=True)
    #app.run(host="127.0.0.1", port=2000,debug=True)
