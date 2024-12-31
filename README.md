# Chatbot OpenAI

A powerful and customizable chatbot built using OpenAI's GPT-4 API. This chatbot can be integrated into various platforms to provide intelligent, conversational experiences for users. Whether you're looking to enhance customer support, create interactive applications, or experiment with AI-driven conversations, this project offers a solid foundation to get you started.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Configuration](#configuration)
- [Usage](#usage)
- [Customization](#customization)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

## Features

- **Natural Language Understanding:** Leverages OpenAI's GPT-4 to understand and respond to user inputs intelligently.
- **Multi-platform Support:** Easily integrate the chatbot into websites, messaging apps, or other platforms.
- **Customizable Responses:** Tailor the chatbot's behavior and responses to suit specific needs.
- **Extensible Architecture:** Modular design allows for easy addition of new features and functionalities.
- **Secure:** Implements best practices for handling API keys and user data.
- **Scalable:** Designed to handle multiple concurrent users with efficient performance.

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- **Node.js** (v14 or later)
- **npm** or **yarn**
- **OpenAI API Key**: Sign up at [OpenAI](https://platform.openai.com/) to obtain your API key.
- **Git**: For cloning the repository.

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yxshee/chatbot-openai.git
   cd chatbot-openai
   ```

2. **Install Dependencies**

   Using npm:

   ```bash
   npm install
   ```

   Or using yarn:

   ```bash
   yarn install
   ```

3. **Create Environment Variables**

   Create a `.env` file in the root directory and add the following:

   ```env
   OPENAI_API_KEY=your-openai-api-key
   PORT=3000
   ```

   - Replace `your-openai-api-key` with your actual OpenAI API key.
   - You can change the `PORT` number if needed.

## Configuration

The chatbot can be configured to suit your specific requirements. Below are some key configuration options:

- **Model Selection:** Choose between different OpenAI models (e.g., GPT-4, GPT-3.5-turbo).
- **Temperature:** Adjust the creativity of the responses.
- **Max Tokens:** Control the length of the responses.
- **Prompt Engineering:** Customize the initial prompt to guide the chatbot's behavior.

You can modify these settings in the `config.js` file:

```javascript
module.exports = {
  openai: {
    apiKey: process.env.OPENAI_API_KEY,
    model: 'gpt-4',
    temperature: 0.7,
    maxTokens: 150,
  },
  server: {
    port: process.env.PORT || 3000,
  },
};
```

## Usage

Start the chatbot server with the following command:

```bash
npm start
```

Or if you're using yarn:

```bash
yarn start
```

The server will start on the port specified in the `.env` file (default is `3000`). You can access the chatbot via:

```
http://localhost:3000
```

### API Endpoints

- **POST `/api/chat`**

  Send a message to the chatbot.

  **Request Body:**

  ```json
  {
    "message": "Hello, how are you?"
  }
  ```

  **Response:**

  ```json
  {
    "reply": "I'm doing well, thank you! How can I assist you today?"
  }
  ```

## Customization

### Integrate with Frontend

You can integrate the chatbot with your frontend application. Here's a basic example using HTML and JavaScript:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Chatbot Integration</title>
</head>
<body>
  <div id="chatbox">
    <div id="messages"></div>
    <input type="text" id="userInput" placeholder="Type your message..." />
    <button onclick="sendMessage()">Send</button>
  </div>

  <script>
    async function sendMessage() {
      const input = document.getElementById('userInput').value;
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input }),
      });
      const data = await response.json();
      const messages = document.getElementById('messages');
      messages.innerHTML += `<p><strong>You:</strong> ${input}</p>`;
      messages.innerHTML += `<p><strong>Bot:</strong> ${data.reply}</p>`;
      document.getElementById('userInput').value = '';
    }
  </script>
</body>
</html>
```

### Adding New Features

The chatbot's architecture allows for easy addition of new features such as:

- **User Authentication:** Secure the chatbot with user login.
- **Persistent Conversations:** Store and retrieve past conversations.
- **Multi-language Support:** Enable the chatbot to understand and respond in multiple languages.
- **Analytics:** Track user interactions and chatbot performance.

Refer to the project structure and documentation to implement these features.

## API Reference

### `POST /api/chat`

**Description:** Sends a user message to the chatbot and retrieves a response.

**Request Body:**

| Field   | Type   | Description                |
| ------- | ------ | -------------------------- |
| message | string | The user's input message.  |

**Response:**

| Field | Type   | Description                       |
| ----- | ------ | --------------------------------- |
| reply | string | The chatbot's generated response. |

**Example Request:**

```bash
curl -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me a joke."}'
```

**Example Response:**

```json
{
  "reply": "Why did the scarecrow win an award? Because he was outstanding in his field!"
}
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the Repository**

   Click the "Fork" button at the top right of this page.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your-username/chatbot-openai.git
   cd chatbot-openai
   ```

3. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

4. **Make Your Changes**

   Implement your feature or bug fix.

5. **Commit Your Changes**

   ```bash
   git commit -m "Add your message here"
   ```

6. **Push to Your Fork**

   ```bash
   git push origin feature/YourFeature
   ```

7. **Create a Pull Request**

   Go to the original repository and create a pull request from your fork.

### Code of Conduct

Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) when contributing to this project.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

- **Author:** [Yash Dogra](https://github.com/yxshee)
- **Project Link:** [yxshee/chatbot-openai](https://github.com/yxshee/chatbot-openai)

## Acknowledgements

- [OpenAI](https://openai.com/) for providing the powerful GPT-4 API.
- [Node.js](https://nodejs.org/) for the runtime environment.
- [Express](https://expressjs.com/) for the web framework.
- [dotenv](https://github.com/motdotla/dotenv) for environment variable management.
- [Axios](https://axios-http.com/) for HTTP requests.

---
