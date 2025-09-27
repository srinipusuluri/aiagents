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

## More Examples:

Sample 1 – Billing Issue

Customer: Hi, I was charged twice for my subscription this month.
Agent: I’m sorry to hear that. Can you please share the last four digits of your card?
Customer: Sure, it’s 1234.
Agent: Thank you. I checked your account, and I do see two identical charges. I’ve initiated a refund for the duplicate payment.
Customer: Perfect, how long will it take?
Agent: Refunds usually take 3–5 business days to reflect.
Customer: Okay, thanks for fixing this quickly!
Agent: You’re welcome! Is there anything else I can help you with today?
Customer: Nope, that’s all.

Sample 2 – Technical Issue

Customer: My app keeps crashing when I try to upload a file.
Agent: I see. Can I confirm which version of the app you’re using?
Customer: Version 3.5.2 on iOS.
Agent: Thank you. That version has a known bug with file uploads. A fix was released in 3.5.3. Could you update from the App Store and try again?
Customer: Let me try... Okay, updated. It works now!
Agent: Great! I’m glad it’s resolved. We’ll also send you an email with release notes.
Customer: Appreciate the quick help.

Sample 3 – General Support / Feature Request

Customer: Does your platform support dark mode?
Agent: Currently, dark mode is available on mobile but not yet on web.
Customer: Ah, I mostly use web. Any timeline?
Agent: Our product team is working on it, and it’s planned for release next quarter.
Customer: Good to know. Thanks!

Sample 4 – Escalation Case

Customer: I need help immediately. My account was locked and I can’t access my invoices.
Agent: I’m really sorry for the inconvenience. I’ll escalate this to our security team right away. Could you confirm your registered email?
Customer: john.smith@email.com

Agent: Thanks. I’ve created a high-priority case (#48392). Our security specialist will contact you within the next 2 hours.
Customer: Okay, but I need this fixed today.
Agent: Absolutely, we’ll prioritize it. You’ll receive an update shortly.

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection for API calls

## License

MIT License
