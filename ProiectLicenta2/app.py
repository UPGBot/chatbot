import flask
from flask import request
from flask.json import jsonify
from chatbot import chatbot_response

app = flask.Flask(__name__)

@app.route('/chatbot', methods=['GET'])
def get_message():
    message = request.args["message"]
    return jsonify(chatbot = chatbot_response(message))

app.run()
