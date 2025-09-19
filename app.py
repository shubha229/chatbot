import gradio as gr
import cohere

API_KEY = "WoKhOQlEsCnBTa3GUstHOLwSJMkogrCbRZ6i9l5q"
co = cohere.ClientV2(api_key=API_KEY)

def chatbot(user_message, history):
    # Send only the latest user message to Cohere
    cohere_messages = [{
        "role": "user",
        "content": [{"type": "text", "text": user_message}]
    }]
    
    response = co.chat(
        messages=cohere_messages,
        temperature=0.3,
        model="command-a-03-2025",
    )
    
    assistant_reply = response.message.content[0].text
    
    # Instead of appending, overwrite history with just this turn
    return [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": assistant_reply},
    ]

with gr.Blocks() as demo:
    gr.Markdown("## 🤖 ShubTalk ")
    gr.ChatInterface(fn=chatbot, type="messages")

if __name__ == "__main__":
    demo.launch()
