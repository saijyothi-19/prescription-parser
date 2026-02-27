from flask import Flask, request, render_template
from translation_voice import process_prescription

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = {
        "medicine": request.form["medicine"],
        "dosage": request.form["dosage"],
        "frequency": request.form["frequency"],
        "duration": request.form["duration"]
    }

    result = process_prescription(data)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)