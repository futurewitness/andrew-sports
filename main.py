from flask import Flask, jsonify
from flask import render_template

app = Flask(__name__)

@app.route('/')
def serve():
    return render_template("index.html")



@app.route('/hello')
def hello_world():
    return jsonify(message="Hello, world!")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
