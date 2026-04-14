# GPT Models Examples

A comprehensive collection of examples demonstrating how to use OpenAI's GPT models with the modern OpenAI Python SDK (version 2.8.1). This project showcases various AI-powered applications including text generation, summarization, and chatbot functionality.

## Features

### Core AI Applications
- **Text Generation**: Generate creative text continuations using GPT-4.1-mini
- **Text Summarization**: Extract keywords and summarize text content
- **Poetic Chatbot**: Interactive chatbot that responds in poetic verse

### Modern OpenAI Integration
- Updated to use the latest OpenAI Responses API
- Compatible with OpenAI Python SDK v2.8.1+
- Replaces legacy Completion and ChatCompletion APIs

### LangChain Examples
- Modern LangChain patterns (no deprecated chains)
- Explicit memory management
- Document loading and retrieval
- RAG (Retrieval-Augmented Generation) implementation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/lucasharca/gpt_models_examples.git
cd gpt_models_examples
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install openai langchain langchain-openai langchain-community
```

4. Set up your API key:
   - Copy `config_example.py` to `config.py`
   - Replace `"####"` with your actual OpenAI API key

## Usage

### Running Individual Examples

#### Text Generation
```python
from text_generator import TextGenerator
from config import api_key
from openai import OpenAI

client = OpenAI(api_key=api_key)
generator = TextGenerator(client)
text = generator.generate_text("Once upon a time", max_tokens=50)
print(text)
```

#### Text Summarization
```python
from summarize_text import TextSummarize
from config import api_key
from openai import OpenAI

client = OpenAI(api_key=api_key)
summarizer = TextSummarize(client)
keywords = summarizer.text_summarizer("Your text here...")
print(keywords)
```

#### Poetic Chatbot
```python
from simple_chatbot import SimpleChatbot
from config import api_key
from openai import OpenAI

client = OpenAI(api_key=api_key)
chatbot = SimpleChatbot(client)
response = chatbot.poetic_chatbot("When was cheese first made?")
print(response)
```

### Running the Main Script
```bash
python main.py
```

### Jupyter Notebook
Open `GPT+Models+Updated.ipynb` for interactive examples and detailed explanations of:
- API setup and configuration
- Text generation with customizable parameters
- Summarization techniques
- Chatbot implementation
- Modern LangChain integration

## Project Structure

```
gpt_models_examples/
├── config_example.py      # API key template
├── config.py             # Your API configuration (not in repo)
├── main.py               # Main script with example usage
├── text_generator.py     # Text generation class
├── summarize_text.py     # Text summarization class
├── simple_chatbot.py     # Poetic chatbot class
├── GPT+Models+Updated.ipynb  # Comprehensive Jupyter notebook
└── README.md             # This file
```

## Requirements

- Python 3.8+
- OpenAI API key
- Dependencies: `openai`, `langchain`, `langchain-openai`, `langchain-community`

## API Compatibility

This project uses the modern OpenAI Responses API instead of the deprecated:
- `openai.Completion.create()`
- `openai.ChatCompletion.create()`

If you're using an older version of the OpenAI SDK, upgrade with:
```bash
pip install --upgrade openai
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).
