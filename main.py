from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
Ollama_url= "http://localhost:11434"

@app.route('/generate', methods=['POST'])
def generate():
    data =request.get_json()
    prompt=data.get('prompt')
    
    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    
    try:
        response = requests.post(f"{Ollama_url}/api/generate", json={"model":"llama3.2:latest", "prompt":prompt, "stream":False})
        if response.status_code != 200:
            return jsonify({"error":f"Ollama Error {response.status_code}", "details":response.text}),500
        result = response.json()
        return jsonify({"response":result.get("response", "No response from model")})
    
    except Exception as e:
        return jsonify({"error":"Something went wrong", "details":str(e)}),500
    

if __name__ == '__main__':
    app.run(debug=True)