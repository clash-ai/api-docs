import asyncio, time
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key='YOUR_API_KEY', base_url='not released yet...')

async def main():
    start_time = time.time()
    response = await client.chat.completions.create(
        messages=[
            {'role': 'system', 'content': 'system prompt'},
            {'role': 'user', 'content': 'Hey wassup'},
        ],
        model='gpt-4o'
    )
    print(f"> Request took {round(time.time() - start_time, 2)} seconds")
    print(response.choices[0].message.content)

if __name__ == '__main__':
    asyncio.run(main())