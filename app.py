from flask import Flask, request, jsonify, render_template, send_file
from analyzer import analyze_url_complete
from logger import logger
from exporter import export_pdf, export_json

app = Flask(__name__)
app.json.sort_keys = False

last_result = None

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

    global last_result

    data = request.get_json()
    
    if not data or "url" not in data:
        return jsonify({
            "error": "No URL provided."
        }), 400

    logger.info(f"Received URL: {data['url']}")
    
    result = analyze_url_complete(data["url"])

    last_result = result

    logger.info("Analysis completed successfully.")

    return jsonify(result)

@app.route("/download/pdf")
def download_pdf():

    global last_result

    if last_result is None:
        return jsonify({"error": "No analysis available"}), 400

    filename = export_pdf(last_result)

    return send_file(filename, as_attachment=True)


@app.route("/download/json")
def download_json():

    global last_result

    if last_result is None:
        return jsonify({"error": "No analysis available"}), 400

    filename = export_json(last_result)

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
