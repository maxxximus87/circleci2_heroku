from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home(ButtonPressed="No"):
    return render_template("index.html", ButtonPressed=ButtonPressed)
       
@app.route("/button", methods=["POST"])
def button(ButtonPressed="Yes"):
    if request.method == "POST":
        return render_template("button.html", ButtonPressed=ButtonPressed)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)