from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# دالة لقراءة البيانات من ملف JSON
def load_comments():
    try:
        with open('comments.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "Comments file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format in comments file"}

@app.route('/api/test', methods=['POST'])
def test_api():
    return jsonify({"message": "Request received successfully ✅"})

# API جديد لإرجاع جميع التعليقات
@app.route('/api/all_comments', methods=['GET'])
def get_all_comments():
    comments = load_comments()
    if isinstance(comments, dict) and "error" in comments:
        return jsonify(comments), 500
    return jsonify(comments)

if __name__ == '__main__':
    app.run(debug=True)
