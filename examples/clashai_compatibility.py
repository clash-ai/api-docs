import clashai

client = clashai.Client(api_key="YOUR_API_KEY")
completion = client.chat.completions.create(
    messages=[
            {'role': 'system', 'content': 'Here comes your System-Prompt.'},
            {'role': 'user', 'content': 'Hello, ClashAI!'},
    ]
)

print(completion['choices'][0]['message']['content'])