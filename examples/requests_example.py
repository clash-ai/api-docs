import requests, time

def main():
    url = 'https://api.clashai.eu/v1/chat/completions'

    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "system prompt"},
            {"role": "user", "content": "Hey wassup"}
        ]
    }
    headers = {'Authorization': 'Bearer YOUR_API_KEY'}

    start_time = time.time()
    response = requests.post(url, json=payload, headers=headers)

    if response.ok:
        print(f"> Request took {round(time.time() - start_time, 2)} seconds")
        print(response.json()['choices'][0]['message']['content'])
    else:
        print(f"Request failed with status code {response.status_code}")

if __name__ == '__main__':
    main()