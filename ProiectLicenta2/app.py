import flask
from flask import request
from flask.json import jsonify
from chatbot import chatbot_response
from flask import render_template
from flask_cors import CORS
import nltk
nltk.download('punkt')
nltk.download('wordnet')

app = flask.Flask(__name__)
CORS(app)

@app.route('/chatbot', methods=['GET'])
def get_message():
    message = request.args["message"]
    return jsonify(chatbot = chatbot_response(message))

@app.route("/")
def root():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

