# Phishing Detector

A Python-based phishing detection system that analyzes URLs using multiple security checks, SSL certificate validation, DNS lookups, WHOIS information, URL heuristics, and VirusTotal reputation analysis, and returns a phishing risk score. The project is deployed as a REST API using Flask and Render.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-3.1-green)
![Render](https://img.shields.io/badge/Deployment-Render-success)
![License](https://img.shields.io/badge/License-Educational-orange)

---

## Project Status

**Current Version:** v1.0

### Completed
- ✅ Detection Engine
- ✅ URL Heuristic Analysis
- ✅ DNS & SSL Analysis
- ✅ WHOIS Domain Analysis
- ✅ VirusTotal Integration
- ✅ Risk Scoring Engine
- ✅ Flask REST API
- ✅ PDF & JSON Report Generation
- ✅ Logging
- ✅ GitHub Version Control
- ✅ Cloud Deployment (Render)

### In Progress
- 🚧 Web Interface Integration (Frontend) (developed by Vaani Chandrakar)

### Planned Enhancements
- 🔹 Machine Learning-based Detection
- 🔹 Email Phishing Analysis
- 🔹 Browser Extension
- 🔹 Database Support

---

## Table of Contents

- Features
- Project Structure
- System Architecture
- Technologies Used
- Installation
- Environment Variables
- Running Locally
- API Endpoint
- Risk Levels
- Deployment
- Testing
- Screenshots
- Future Improvements
- Acknowledgements
- Author
- License

---

## Features

- URL validation
- HTTPS verification
- SSL certificate analysis
- WHOIS domain age lookup
- DNS record verification
- Suspicious keyword detection
- URL length analysis
- Dot count analysis
- URL shortener detection
- Special character detection
- IP address detection
- Typosquatting detection
- VirusTotal URL reputation analysis
- Risk scoring system
- JSON API responses
- Logging support
- PDF report generation
- Cloud deployment using Render

---

## Project Structure

```
phishing-detector/
│
├── checks/
│   ├── __init__.py
│   ├── network_checks.py
│   ├── reputation.py
│   └── url_checks.py
│
├── logs/
├── reports/
├── screenshots/
│
├── analyzer.py
├── app.py
├── config.py
├── exporter.py
├── logger.py
├── main.py
├── report.py
├── scoring.py
├── requirements.txt
├── Procfile
├── README.md
└── .env
```

---

## System Architecture

```
                 User
                  │
                  ▼
        Web Interface / API Client
                  │
                  ▼
            Flask REST API
                  │
                  ▼
         Phishing Analysis Engine
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
 URL Checks   Network   VirusTotal
              Checks
        │
        ▼
     Scoring Engine
        │
        ▼
 JSON Response / PDF Report
```

---

## Technologies Used

- Python 3
- Flask
- Gunicorn
- Requests
- python-dotenv
- dnspython
- python-whois
- tldextract
- ReportLab
- VirusTotal API
- Render
- GitHub

---

## Installation

Clone the repository

```bash
git clone https://github.com/VaishnaviKoshe/phishing-detector.git
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a .env file.

Example:

```env
VT_API_KEY=YOUR_VIRUSTOTAL_API_KEY
```

---

## Running Locally

Run the console application

```bash
python main.py
```

Run the API

```bash
python app.py
```

or

```bash
gunicorn app:app
```

Server starts at

```
http://127.0.0.1:5000
```

---

## API Endpoint

### Home

```
GET /
```

Response
```
Phishing Detector API is running!
```

---

### Analyze URL

```
POST /analyze
```

Request Body

```json
{
    "url":"https://google.com"
}
```

### Example Request

```bash
curl -X POST https://phishing-detector-fep7.onrender.com/analyze \
-H "Content-Type: application/json" \
-d "{\"url\":\"https://google.com\"}"
```

### Example Response

```json
{
    "url": "https://google.com",

    "url_details": {
        "scheme": "https",
        "domain": "google.com",
        "path": "",
        "url_length": 18,
        "dot_count": 1,
        "special_characters": false,
        "typosquatting": null
    },

    "ssl": {
        "status": "Valid",
        "issuer": "Google Trust Services",
        "expiry": "2026-09-07",
        "days_left": 63
    },

    "virustotal": {
        "status": "Available",
        "harmless": 64,
        "malicious": 0,
        "suspicious": 0
    },

    "result": {
        "risk": "SAFE",
        "score": 0,
        "reasons": [
            "No suspicious indicators detected."
        ]
    }
}
```

---

## Risk Levels

| Score | Classification |
|--------|---------------|
| 0–29 | SAFE |
| 30–59 | SUSPICIOUS |
| 60–100 | PHISHING |

---

## Deployment

The project is deployed on Render using Gunicorn.

Deployment includes:

- Flask REST API
- Automatic GitHub deployment
- Environment variable support
- HTTPS endpoint

### Live API:
https://phishing-detector-fep7.onrender.com

---

## Testing

The deployed REST API was tested using PowerShell by sending POST requests to the `/analyze` endpoint.

Example:

```powershell
Invoke-RestMethod `
-Uri "https://phishing-detector-fep7.onrender.com/analyze" `
-Method POST `
-ContentType "application/json" `
-Body '{"url":"https://google.com"}'
```

Expected Response:

```json
{
    "result": {
        "risk": "SAFE",
        "score": 0
    }
}
```

The API was also tested with:
- Valid HTTPS URLs
- Invalid URLs
- Domains with missing DNS records
- URLs containing suspicious keywords
- Newly registered domains

---

## Screenshots

### 1. Project Structure

The project is organized into separate modules for URL analysis, scoring, logging, report generation, and the Flask REST API. This modular architecture improves maintainability and makes it easier to extend the application with additional phishing detection techniques.

![Project Structure](screenshots/folder.png)

---

### 2. Flask Backend Running

The Flask application successfully starts the REST API server, making the phishing detector available for analysis requests.

![Flask Backend](screenshots/home.png)

---

### 3. URL Analysis Request

A client sends a POST request containing a URL to the `/analyze` endpoint. The backend receives the request and begins the phishing analysis process.

Example Request:

```json
{
    "url": "https://google.com"
}
```

![API Request](screenshots/api.png)

---

### 4. Phishing Analysis Response

The detector returns a structured JSON response containing the URL's basic information, security checks, SSL analysis, VirusTotal reputation, and the final phishing risk assessment.

![JSON Response](screenshots/analysis.png)

---

### 5. Generated PDF Report

After completing the analysis, the application can generate a PDF report summarizing the phishing detection results, including the URL, risk level, score, SSL status, VirusTotal results, and reasons contributing to the final assessment.

![PDF Report](screenshots/report.png)

---

### 6. Application Logging

The application records important events such as incoming requests, analysis progress, VirusTotal checks, and completion status using Python's logging module. These logs help with debugging and monitoring the system.

![Logs](screenshots/logs.png)

---

### 7. Web Interface *(Pending)*

The backend is designed to integrate seamlessly with a web frontend. Users can enter a URL, submit it for analysis, and view the phishing detection results through a graphical interface.

![Web Interface](screenshots/web.png)

---

## Future Improvements

- Machine Learning-based phishing detection
- Email phishing analysis
- QR code phishing detection
- Browser extension
- Web interface
- User authentication
- Database support
- Threat intelligence integration

---

## Acknowledgements

- VirusTotal Public API
- Flask Documentation
- Render Cloud Platform
- ReportLab

---

## Author

*Vaishnavi Koshe*

Bachelor of CSE

GitHub:
https://github.com/VaishnaviKoshe

---

## License

This project is developed for educational and academic purposes.