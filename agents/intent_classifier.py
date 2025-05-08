import openai

openai.api_key = "sk-your-api-key"  # Replace or load from env

def classify_intent(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Classify this intent in emotional tone and polarity."},
            {"role": "user", "content": text}
        ]
    )
    result = response['choices'][0]['message']['content']
    print(f"\nAI CLASSIFIER RESULT:\n{text}\n→ {result}")
    return result
