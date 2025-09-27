# Customer Service Chat Rating System

A web application built with Gradio that evaluates customer service chat transcripts and provides ratings (Good, Bad, or Neutral) using OpenAI's GPT-3.5-turbo model.

## Features

- Paste customer service chat transcripts
- Get instant ratings: Good, Bad, or Neutral
- Powered by AI for accurate analysis
- Simple web interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/customer-chat-rating-system.git
   cd customer-chat-rating-system
   ```

2. Install dependencies:
   ```bash
   pip install gradio openai
   ```

3. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

Run the application:
```bash
python app.py
```

The app will launch in your browser with a public shareable link.

Paste a chat transcript in the text box and click "Rate Chat" to get the rating.

## Example Transcript

```
Customer: Hi, I need help with my order.
Agent: Hello! I'd be happy to assist. What's your order number?
Customer: It's 12345.
Agent: Thank you. I see your order is delayed. I'll process a refund immediately.
Customer: Thanks so much!
```

Rating: GOOD

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection for API calls

## License

MIT License
