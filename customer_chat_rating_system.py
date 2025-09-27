import gradio as gr
from openai import OpenAI
import os
import json

def rate_chat(chat_transcript):
    """
    You are a chat quality evaluator.

Task:
- You will receive one or more customer service chat transcripts.
- For each transcript, provide an overall rating: Good, Bad, or Neutral.
- Do not merge transcripts. Rate each independently.
- Output should be structured in JSON with transcript number, rating, and optional reason.

Guidelines:
- "Good" = issue resolved politely and efficiently, positive customer sentiment.
- "Bad" = rude agent, unresolved issue, or customer frustration remains.
- "Neutral" = mixed outcome, slow resolution, or unclear sentiment.
- Be concise in reasoning (one short sentence).

Input format:
[Transcript 1]
Customer: ...
Agent: ...

[Transcript 2]
Customer: ...
Agent: ...

Output format:
[
  { "transcript": 1, "rating": "Good", "reason": "Refund processed quickly" },
  { "transcript": 2, "rating": "Bad", "reason": "Agent was dismissive, issue unresolved" }
]
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    client = OpenAI(api_key=openai_api_key)

    system_prompt = """
You are a chat quality evaluator.

Task:
- You will receive one or more customer service chat transcripts.
- For each transcript, provide an overall rating: Good, Bad, or Neutral.
- Do not merge transcripts. Rate each independently.
- Output should be structured in JSON with transcript number, rating, and optional reason.

Guidelines:
- "Good" = issue resolved politely and efficiently, positive customer sentiment.
- "Bad" = rude agent, unresolved issue, or customer frustration remains.
- "Neutral" = mixed outcome, slow resolution, or unclear sentiment.
- Be concise in reasoning (one short sentence).

Input format:
[Transcript 1]
Customer: ...
Agent: ...

[Transcript 2]
Customer: ...
Agent: ...

Output format:
[
  { "transcript": 1, "rating": "Good", "reason": "Refund processed quickly" },
  { "transcript": 2, "rating": "Bad", "reason": "Agent was dismissive, issue unresolved" }
]
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": chat_transcript}
        ],
        max_completion_tokens=200,
        temperature=0.5
    )

    result = response.choices[0].message.content.strip()
    ratings = json.loads(result)
    # Assuming single transcript, return the first rating
    rating = ratings[0]['rating']
    return rating.lower()

def chat_rating_agent(chat_transcript):
    """Main function for the customer service chat rating system"""
    if not chat_transcript.strip():
        return "Please provide a chat transcript to rate."

    rating = rate_chat(chat_transcript)
    return f"Chat Rating: {rating.upper()}"

# Create Gradio interface
with gr.Blocks(title="Customer Service Chat Rating System", theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 💬 Customer Service Chat Rating System")
    gr.Markdown("Paste a customer service chat transcript below to get an overall rating: good, bad, or neutral.")

    transcript_input = gr.Textbox(
        placeholder="Paste your chat transcript here...",
        label="Chat Transcript",
        lines=10
    )
    rate_button = gr.Button("Rate Chat")
    rating_output = gr.Textbox(label="Rating Result", interactive=False)

    def rate_transcript(transcript):
        result = chat_rating_agent(transcript)
        return result

    rate_button.click(rate_transcript, inputs=transcript_input, outputs=rating_output)

if __name__ == "__main__":
    demo.launch(share=True)
