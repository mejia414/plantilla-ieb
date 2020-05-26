from flask import Flask
from flask import jsonify
from flask import make_response
from flask import render_template
from flask import redirect
from flask import request

from flask_ngrok import run_with_ngrok

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    response = jsonify
    return render_template('index.html')

@app.route('/download', methods=['GET'])
def download():
    response = jsonify
    return render_template('download.html')

@app.route('/upload', methods=['GET'])
def upload():
    response = jsonify
    return render_template('upload.html')

@app.route('/api', methods=['GET'])
def api():
    response = jsonify
    return render_template('api.html')

@app.route('/about', methods=['GET'])
def about():
    response = jsonify
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
