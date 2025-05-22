<div align="center">

<h1>🤖  OpenAI Chatbot </h1>

<h3>🤖 Streamlit-Powered OpenAI Chatbot 🚀</h3>

[![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-412991.svg?style=for-the-badge&logo=openai)](https://openai.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)](https://python.org/)

</div>

---

## 🌟 What Makes This Special?

<table>
<tr>
<td width="33%" align="center">

### 🧠 **Smart Conversations**
Powered by OpenAI's GPT-3.5-turbo
for intelligent responses

</td>
<td width="33%" align="center">

### ⚡ **Simple & Fast**
Built with Streamlit for
instant deployment

</td>
<td width="33%" align="center">

### 🎨 **Clean Interface**
Beautiful, responsive chat UI
with message persistence

</td>
</tr>
</table>

## 🎯 Features

```mermaid
mindmap
  root((Streamlit Chatbot))
    🤖 AI Features
      GPT-3.5-turbo Integration
      Context Awareness
      Streaming Responses
      Message History
    🛠️ Technical
      Python Backend
      Streamlit Framework
      Session State Management
      OpenAI API Integration
    🎨 User Experience
      Real-time Chat
      Message Persistence
      Clean Interface
      Responsive Design
    🔧 Developer Tools
      Easy Setup
      Minimal Dependencies
      Environment Variables
      Apache 2.0 License
```

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have:

- 🐍 **Python** (3.8 or higher)
- 🔑 **OpenAI API Key** ([Get one here](https://platform.openai.com/account/api-keys))
- 💾 **Git** installed

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/venom/chatbot-openai.git
   cd chatbot-openai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Enter your OpenAI API Key**
   - Open the app in your browser (usually http://localhost:8501)
   - Enter your OpenAI API key in the sidebar
   - Start chatting!

🎉 **That's it!** Your chatbot is ready to use!

## 💬 Usage

### Getting Your API Key
1. Visit [OpenAI Platform](https://platform.openai.com/account/api-keys)
2. Create an account or sign in
3. Generate a new API key
4. Copy and paste it into the app

### Alternative: Using Secrets
You can also store your API key in Streamlit secrets:

1. Create `.streamlit/secrets.toml` file:
   ```toml
   OPENAI_API_KEY = "your-api-key-here"
   ```

2. Access it in code:
   ```python
   openai_api_key = st.secrets["OPENAI_API_KEY"]
   ```

## 🏗️ How It Works

```mermaid
graph LR
    A[User Input] --> B[Streamlit App]
    B --> C[OpenAI API]
    C --> D[GPT-3.5-turbo]
    D --> E[Streaming Response]
    E --> F[Chat Display]
    F --> G[Session State]
    G --> B
    
    style A fill:#e1f5fe
    style C fill:#ffecb3
    style D fill:#e8f5e8
    style F fill:#fce4ec
```

## 📁 Project Structure

```
chatbot-openai/
├── 📄 streamlit_app.py    # Main Streamlit application
├── 📄 requirements.txt    # Python dependencies
├── 📄 LICENSE            # Apache 2.0 License
└── 📄 README.md          # This file

Optional:
├── 📁 .streamlit/
│   └── 📄 secrets.toml   # API key storage
```

## 🔧 Code Overview

The chatbot is built with just a few key components:

```python
# OpenAI client initialization
client = OpenAI(api_key=openai_api_key)

# Session state for message persistence
if "messages" not in st.session_state:
    st.session_state.messages = []

# Streaming response generation
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=st.session_state.messages,
    stream=True
)
```

## 🎨 Screenshots

<div align="center">

### 💻 Chat Interface
*Clean, intuitive design with real-time streaming responses*

### 🔐 API Key Input
*Secure API key input with helpful links and instructions*

</div>

## 🛣️ Features & Roadmap

- ✅ **OpenAI GPT-3.5-turbo Integration**
- ✅ **Streamlit Web Interface**
- ✅ **Message History Persistence**
- ✅ **Streaming Responses**
- ✅ **Secure API Key Input**
- 📋 **Multiple Model Support** (GPT-4, etc.)
- 📋 **Conversation Export**
- 📋 **Custom System Prompts**
- 📋 **File Upload Support**
- 📋 **Dark/Light Theme Toggle**

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### 🐛 Found a Bug?
1. Check existing [Issues](https://github.com/venom/chatbot-openai/issues)
2. Create a new issue with steps to reproduce
3. Include error messages and screenshots

### 💡 Feature Ideas?
1. Open a [Discussion](https://github.com/venom/chatbot-openai/discussions)
2. Describe your feature request
3. Explain the use case

### 🔧 Want to Contribute Code?
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📚 Learn More

- 📖 [Streamlit Documentation](https://docs.streamlit.io/)
- 🤖 [OpenAI API Documentation](https://platform.openai.com/docs/)
- 🎓 [Building Conversational Apps Tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)

## 🔒 Security Notes

- Never commit your API keys to version control
- Use environment variables or Streamlit secrets for production
- Be mindful of API usage limits and costs
- Consider implementing rate limiting for production deployments

## 📜 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🤖 **OpenAI** for the amazing GPT models
- 🎈 **Streamlit** for the fantastic framework
- 💻 **The Python community** for excellent libraries

---

<div align="center">

**Made with ❤️ using Streamlit and OpenAI**

⭐ **Star this repo if you find it helpful!** ⭐

</div>