# OpenPerplexity

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/django-5.1.3-green.svg)

An open-source Django REST API that unleashes the power of Perplexity AI for advanced search capabilities, website text extraction, and intelligent information retrieval. OpenPerplexity provides developers with a seamless interface to integrate state-of-the-art AI search functionality into their applications.

## 🚀 Features

### 🤖 Advanced AI Search Capabilities
- **Intelligent Search**: Access Perplexity AI's powerful search capabilities through a simple API
- **Custom Prompts**: Create tailored search experiences with system and user prompt engineering
- **Rich Results**: Retrieve comprehensive search results with citations and sources
- **Multimodal Support**: Handle various content types including text, images, and more

### 📊 Website Content Extraction
- **Text Extraction**: Clean extraction of text content from any website
- **Markdown Conversion**: Transform website content into structured markdown format
- **Document Analysis**: Process and understand document content efficiently

### 🔍 API Integration
- **RESTful Endpoints**: Clean, well-documented API endpoints
- **Flexible Parameters**: Customize search with location, language, and content preferences
- **Authentication**: Secure API key-based authentication
- **CORS Support**: Ready for integration with frontend applications

## 🛠️ Technology Stack

- **Backend**: Django 5.1 with Django REST Framework
- **AI Integration**: OpenperplexSync client library
- **Data Storage**: SQLite (configurable for production databases)
- **Authentication**: API key-based security
- **Environment**: dotenv configuration

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/OpenPerplexity.git
cd OpenPerplexity

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env file to add your Perplexity API key

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

## 🔌 API Endpoints

### Search Endpoints

```
GET /api/search/
POST /api/custom-search/
GET /api/website-text/
GET /api/website-markdown/
```

Example request:
```json
{
  "query": "Latest advancements in quantum computing",
  "system_prompt": "You are a research assistant specializing in quantum physics",
  "location": "US",
  "language": "en",
  "include_citations": true
}
```

## 🧠 Technical Implementation

OpenPerplexity implements several advanced techniques:

1. **Perplexity API Integration**: Seamless integration with Perplexity's powerful search capabilities
2. **Custom Search Parameters**: Flexible parameter configuration for optimized results
3. **Web Content Processing**: Efficient extraction and transformation of web content
4. **Response Handling**: Structured processing of complex API responses
5. **Django REST Architecture**: Clean separation of concerns with a well-structured API design

## 📖 Open Source Philosophy

OpenPerplexity embraces open source principles:

- **Transparency**: All code is open and available for review and improvement
- **Collaboration**: Contributions are welcome through pull requests
- **Education**: Code is structured to serve as a learning resource for AI integration
- **Accessibility**: Makes advanced AI capabilities accessible to developers of all skill levels
- **Community-Driven**: Development roadmap influenced by community needs

## 🔧 Configuration

Configuration is managed through environment variables:

```
PERPLEXITY_API_KEY=your_api_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Made with ❤️ by Anas