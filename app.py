from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 👈 هذا يسمح بالوصول من أي Origin

@app.route('/api/test', methods=['POST'])
def test_api():
    return jsonify({"message": "Request received successfully ✅"})

if __name__ == '__main__':
    app.run(debug=True)
