from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods = ["GET", "POST"])
def chat():
    if request.method == 'POST':
        try:
            msg = request.form["msg"]
            input_text = msg
            genai.configure(api_key='AIzaSyAlU2UVOfoqC1-tWEcO-IFfNo8v03FW66c')
            model = genai.GenerativeModel("gemini-1.5-pro-latest")
            response = model.generate_content(input_text)

            bot_response = response.text if hasattr(response, 'text') else str(response)

            return jsonify({"sender": "Bot", "message": bot_response})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
