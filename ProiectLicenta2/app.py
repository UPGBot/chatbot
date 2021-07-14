import flask
from flask import request
from flask.json import jsonify
from chatbot import chatbot_response
import nltk
nltk.download('punkt')
nltk.download('wordnet')

app = flask.Flask(__name__)

@app.route('/chatbot', methods=['GET'])
def get_message():
    message = request.args["message"]
    return jsonify(chatbot = chatbot_response(message))

if __name__ == "__main__":
    app.run()

