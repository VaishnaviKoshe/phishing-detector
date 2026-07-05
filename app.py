from flask import Flask, request, jsonify
from analyzer import analyze_url_complete
from logger import logger

app = Flask(__name__)

@app.route("/")
def home():
    return "Phishing Detector API is running!"

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
