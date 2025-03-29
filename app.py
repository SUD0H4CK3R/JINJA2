from flask import Flask, request, render_template_string
import os

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        user_input = request.form.get("name", "")
        output = render_template_string(f"Hello {user_input}")  # Vulnerable to CSTI
    
    return '''
    <html>
    <head><title>Render This!</title></head>
    <body>
        <h2>Welcome to Render This!</h2>
        <form method="post">
            <input type="text" name="name" placeholder="Say something...">
            <button type="submit">Submit</button>
        </form>
        <p>{}</p>
    </body>
    </html>
    '''.format(output)

if __name__ == "__main__":
    app.run(debug=True)
