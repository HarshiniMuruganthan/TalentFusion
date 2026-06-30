import sys
import os
import json
import subprocess
from flask import Flask, render_template, request, jsonify

app = Flask(
    __name__,
    template_folder="frontend/templates",
    static_folder="frontend/static"
)

UPLOAD_FOLDER = "input"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/transform", methods=["POST"])
def transform():

    try:

        resume = request.files.get("resume")
        csv = request.files.get("csv")

        if not resume or not csv:
            return jsonify({
                "success": False,
                "message": "Please upload both Resume and CSV."
            }), 400

        resume.save(os.path.join(UPLOAD_FOLDER, "resume.pdf"))
        csv.save(os.path.join(UPLOAD_FOLDER, "recruiter.csv"))

        result = subprocess.run(
            [sys.executable, "src/main.py"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return jsonify({
                "success": False,
                "message": result.stderr
            }), 500

        with open("output/result.json", "r") as file:
            data = json.load(file)

        return jsonify({
            "success": True,
            "candidate": data
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)