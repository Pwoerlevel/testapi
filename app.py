from flask import Flask, request, jsonify
from flask_cors import CORS
from g4f.client import Client

app = Flask(__name__)
CORS(app)  # السماح بأي origin


@app.route('/api/test', methods=['POST'])
def test_api():
    return jsonify({"message": "Request received successfully ✅"})

@app.route('/hello/<name>', methods=['POST'])
def test_api():
    return jsonify({"message": f"hello {name} "})


if __name__ == '__main__':
    app.run(debug=True)
