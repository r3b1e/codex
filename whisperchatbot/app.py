from flask import Flask, request, jsonify, send_from_directory
import os
from openai import OpenAI
import warnings

app = Flask(__name__)

# Initialize OpenAI client with API key from environment variable
client = OpenAI(api_key='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') 
if not client: 
    raise ValueError("OPENAI_API_KEY environment variable is not set.")
client = OpenAI(api_key=client) 
@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/api', methods=['POST'])
def chat_api():
    data = request.json
    user_message = data.get('message', '')

    # Call the OpenAI API to get a response
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Use your preferred model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        bot_response = completion.choices[0].message['content']
    except Exception as e:
        bot_response = f"Error occurred: {str(e)}"

    return jsonify({'reply': bot_response})

if __name__ == '__main__':
    app.run(debug=True)