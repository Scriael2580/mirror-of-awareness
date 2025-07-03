import requests

# 🔑 مفتاح API من OpenRouter (⚠️ لا تنشره علنًا في النسخ العامة)
API_KEY = "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"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a poetic mirror of the user's self-awareness. Every day, you write a symbolic reflection that carries meaning, transformation, and inner clarity."},
        {"role": "user", "content": "Give me today’s symbolic reflection in a poetic and metaphorical style."}
    ]
}

response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

if response.status_code == 200:
    reflection = response.json()["choices"][0]["message"]["content"]
    print("🌞 Daily Symbolic Reflection:\n")
    print(reflection)
else:
    print("❌ Error:", response.status_code)
    print(response.text)
