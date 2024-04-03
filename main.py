from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def serve():
    return render_template("index.html")



@app.route('/hello')
def hello_world():
    return jsonify(message="Hello, world!")

@app.route('/game')
def game():
    return render_template("game.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
