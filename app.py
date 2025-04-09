from flask import Flask, request, jsonify
from flask_cors import CORS
from g4f.client import Client

app = Flask(__name__)
CORS(app)  # السماح بأي origin

client = Client()  # g4f client

@app.route('/api/test', methods=['POST'])
def test_api():
    return jsonify({"message": "Request received successfully ✅"})

@app.route('/api/chat', methods=['POST'])
def chat_api():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # إرسال الرسالة إلى g4f
    try:
        stream = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_message}],
            stream=True,
            web_search=False
        )

        # تجميع الرد من الـ stream
        full_response = ""
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content:
                full_response += content

        return jsonify({"response": full_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
