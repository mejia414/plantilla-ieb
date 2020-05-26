from flask import Flask
from flask import jsonify
from flask import make_response
from flask import render_template
from flask import redirect
from flask import request


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    response = jsonify
    return 'Hello World'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)