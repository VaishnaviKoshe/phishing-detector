import os
import time
import requests

from dotenv import load_dotenv
from logger import logger
from requests.exceptions import RequestException

load_dotenv()

VT_API_KEY = os.getenv("VT_API_KEY")

def check_virustotal(url):
    """
    Checks a URL using VirusTotal API.
    Returns: {
        "status": "..."
        "malicious": "..."
        "suspicious": "..."
        "harmless": "..."    
    }
    """
    logger.info(f"Checking VirusTotal for {url}")

    headers = {
        "x-apikey": VT_API_KEY
    }
    
    try:
        submit = requests.post("https://www.virustotal.com/api/v3/urls",
            headers=headers,
            data={"url": url},
            timeout=10
        )

        if submit.status_code == 429:
            logger.warning("VirusTotal rate limit reached.")
            return {
                "status": "Rate Limited",
                "malicious": None,
                "suspicious": None,
                "harmless": None
            }

        if submit.status_code != 200:
            logger.warning("VirusTotal service unavailable.")
            return {
                "status": "Unavailable",
                "malicious": None,
                "suspicious": None,
                "harmless": None
            }

        analysis_id = submit.json()["data"]["id"]

        for _ in range(5):
            time.sleep(2)

            report = requests.get(
                f"https://www.virustotal.com/api/v3/analyses/{analysis_id}",
                headers=headers,
                timeout=10
            )

            if report.status_code != 200:
                continue

            data = report.json()

            status = data["data"]["attributes"]["status"]

            if status == "completed":
                stats = data["data"]["attributes"]["stats"]

                logger.info("VirusTotal analysis completed.")

                return {
                    "status": "Available",
                    "malicious": stats["malicious"],
                    "suspicious": stats["suspicious"],
                    "harmless": stats["harmless"]
                }

        logger.warning("VirusTotal analysis is still pending.")

        return {
            "status": "Pending",
            "malicious": None,
            "suspicious": None,
            "harmless": None
        }

    except RequestException as e:
        logger.error(f"VirusTotal connection failed: {e}")
        return {
            "status": "Error",
            "message": str(e),
            "malicious": None,
            "suspicious": None,
            "harmless": None
        }