const axios = require('axios');

async function main() {
    const url = 'https://api.clashai.eu/v1/chat/completions';

    const payload = {
        model: "gpt-4o",
        messages: [
            { role: "system", content: "system prompt" },
            { role: "user", content: "Hey wassup" }
        ]
    };

    const headers = {
        'Authorization': 'Bearer YOUR_API_KEY'
    };

    const startTime = Date.now();

    try {
        const response = await axios.post(url, payload, { headers });

        if (response.status === 200) {
            console.log(`> Request took ${(Date.now() - startTime) / 1000} seconds`);
            console.log(response.data.choices[0].message.content);
        } else {
            console.log(`Request failed with status code ${response.status}`);
        }
    } catch (error) {
        console.log(`Error: ${error.response ? error.response.status : error.message}`);
    }
}

main();
