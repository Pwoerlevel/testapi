from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/test', methods=['POST'])
def test_api():
    return jsonify({"message": "Request received successfully ✅"})

if __name__ == '__main__':
    app.run(debug=True)
