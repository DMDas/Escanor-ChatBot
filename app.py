from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from Escanor_Bot.config import *

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=Gemini_Api)
model = genai.GenerativeModel(
    "models/gemini-2.5-flash-lite",
    system_instruction=(
        "You are Escanor from the Seven Deadly Sins. "
        "Speak proudly and confidently, but still answer factually."
    )
)

# Route for the chat page
@app.route('/')
def home():
    return render_template('chat.html')

# API route for handling chat messages
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_msg = data.get("message", "")

    try:
        response = model.generate_content(user_msg)
        reply = response.text
    except Exception as e:
        reply = f"⚠️ Error: {str(e)}"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
