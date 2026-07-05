from exporter import export_pdf

sample = {
    "url": "https://google.com",

    "result": {
        "risk": "Low",
        "score": 0,
        "reasons": [
            "HTTPS enabled",
            "No suspicious keywords",
            "Valid SSL certificate"
        ]
    },

    "ssl": {
        "status": "Valid",
        "issuer": "Google Trust Services",
        "expiry": "2026-09-07",
        "days_left": 64
    },

    "virustotal": {
        "status": "Available",
        "malicious": 0,
        "suspicious": 0,
        "harmless": 95
    }
}

export_pdf(sample)

print("PDF Created Successfully!")