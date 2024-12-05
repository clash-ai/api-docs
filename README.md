ClashAI › FREE AI API
======
› Access the latest and most advanced AI models with our API. Completely free and easy to use.

Table of Contents
------------
- **Overview**: Is this page to get you started quickly
- **Getting Started**: Learn how to begin using the ClashAI API
- **Endpoints**: List of Models, Generate Text, Generate Images
- **Code Examples**: Take a look at code examples to better understand our API

Key Features
------------
- Fast and uncomplicated
- Low limits. 25 requests per minute, 500 requests per day
- High accuracy and performance
- Comprehensive documentation
- Responsive support team

Get your API Key
------------
› Join our Discord server with this link https://discord.gg/RjX2CpdPpd go to the `・api-docs` channel and create your API key.

> **Important**: Make sure you do not reveal your API key to anyone, as it can grant access to your key.

```
curl -X POST "https://api.clashai.eu/v1/chat/completions" 
-H "Authorization: Bearer YOUR_API_KEY"
-H "Content-Type: application/json" 
-d "{\"model\": \"gpt-4\", \"messages\": [{\"role\": \"user\", \"content\": \"Hi\"}, {\"role\": \"system\", \"content\": \"Hi GPT\"}]}"
```

You can find code examples in the ``examples`` directory.
- If you use our code examples, look that you have everything installed:
**JavaScript**: ``axios``\
**Python**: ``time`` & ``openai / clashai`` / ``requests`` 

> **Note**: We do not own, control or have any affiliation with these companies that own the models.