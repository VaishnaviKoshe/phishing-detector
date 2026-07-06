from flask import Flask, request, jsonify, render_template
from analyzer import analyze_url_complete
from logger import logger

app = Flask(__name__)
app.json.sort_keys = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan")
def scan():
    return render_template("scan.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    
    if not data or "url" not in data:
        return jsonify({
            "error": "No URL provided."
        }), 400

    logger.info(f"Received URL: {data['url']}")
    
    result = analyze_url_complete(data["url"])

    logger.info("Analysis completed successfully.")

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
