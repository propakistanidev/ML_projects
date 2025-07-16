import gradio as gr
import requests

def model_chat(prompt):
    try:
        response = requests.post("http://localhost:7860/generate", json={"prompt":prompt})
        
        if response.status_code == 200:
            return response.json().get("response", "No response from model")
        else:
            return f"Error {response.status_code}:{response.text}"
    except Exception as e:
        return f"Error: {str(e)}"
    
iface = gr.Interface(fn=model_chat, inputs="text", outputs="text", title="Chatbot")

iface.launch()