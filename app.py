from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # السماح بأي origin


@app.route('/api/test', methods=['POST'])
def test_api():
    return jsonify({"message": "Request received successfully ✅"})

@app.route('/abobest', methods=['POST'])
def test_api():
    return jsonify({"message": "2021"})


if __name__ == '__main__':
    app.run(debug=True)
