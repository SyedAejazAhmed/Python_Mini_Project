import groq
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

API_KEY = "Enter Your API_KEY"

def call_groq_api(api_key, chat_history):
    client = groq.Groq(api_key=api_key)
    user_input = chat_history[-1]["content"]

    completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_input}
        ],
        model="llama3-8b-8192"
    )

    if completion:
        assistant_response = completion.choices[0].message.content
        response_type = "code" if "```" in assistant_response else "text"
        return assistant_response, response_type
    else:
        return None, None

@app.route('/')
def home():
    return render_template('OPENAI.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    chat_history = request.json.get('chat_history', [])
    chat_history.append({"role": "user", "content": user_input})

    assistant_response, response_type = call_groq_api(API_KEY, chat_history)

    if assistant_response:
        chat_history.append({"role": "assistant", "content": assistant_response, "type": response_type})
        return jsonify({"response": assistant_response, "response_type": response_type, "chat_history": chat_history})
    else:
        return jsonify({"error": "Failed to get a response from the API."}), 500

if __name__ == "__main__":
    app.run(debug=True)
