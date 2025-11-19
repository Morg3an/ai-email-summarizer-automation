import requests
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

LLM_API_KEY = "YOUR_API_KEY_HERE"

@app.route("/", methods=["POST"])
def summarize():
    data = request.json.get("text", "")
    
    combined_text = " ".join([article.get("title", "") for article in data])[:5000]
    
    prompt = f"Summarize the following news headlines in 5 concise bullet points:\n\n{combined_text}"

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [
               {"role": "system", "content": "You are a professional summarizer."},
               {"role": "user", "content": prompt}
            ]
        }
    )

    summary = response.json()["choices"][0]["message"]["content"]

    return jsonify({"summary": summary})