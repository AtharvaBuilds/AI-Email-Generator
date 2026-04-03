from flask import Flask, request, render_template

from connection import get_response

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def ask():
    if request.method=="GET":
        return render_template('userinput.html')
    elif request.method=="POST":
        situation = request.form["situation"]
        whom=request.form["whom"]
        generate=request.form["generate"]

        user_prompt=f"""
Write a professional email based on the following details:

Recipient: {whom}
Situation/Purpose: {situation}

Generate a complete email draft in clean, Gmail-compatible HTML format so it can be directly copied and pasted into an email client.

Requirements:
- Include a suitable Subject line
- Include greeting, body, closing, and signature
- Maintain a professional tone unless the situation suggests otherwise
- Use proper paragraph spacing and readable formatting
- Do not include unnecessary explanations

After the email, display a "Copy Email" button below the draft.
"""
        ai_response=get_response(user_prompt)
        return render_template('output.html',ai_response=ai_response)


app.run(debug=True)