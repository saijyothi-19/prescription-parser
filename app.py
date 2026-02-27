from flask import Flask, request, jsonify, render_template
@app.route("/")
def home():
    return render_template("index.html")