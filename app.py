from flask import Flask, request, jsonify
from flask_cors import CORS
from g4f.client import Client

app = Flask(__name__)
CORS(app)  # السماح بأي origin

client = Client()  # g4f client

@app.route('/api/test', methods=['POST'])
def test_api():
    return jsonify({"message": "Request received successfully ✅"})




if __name__ == '__main__':
    app.run(debug=True)
