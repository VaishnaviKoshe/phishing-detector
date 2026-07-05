import validators
import ipaddress

from urllib.parse import urlparse
from difflib import SequenceMatcher
from config import SUSPICIOUS_KEYWORDS
from config import URL_SHORTENERS
from config import TRUSTED_DOMAINS

def validate_url(url):
    return validators.url(url)


def parse_url(url):
    parsed = urlparse(url)

    return {
        "scheme": parsed.scheme,
        "domain": parsed.netloc,
        "path": parsed.path,
        "query": parsed.query
    }    


def check_https(parsed_data):
    if parsed_data["scheme"] == "https":
        return True
    else:
        return False    


def check_suspicious_keywords(url):
    found = []
    url = url.lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in url:
            found.append(keyword)

    return found


def contains_ip(domain):
    host = domain.split(":")[0]

    try: 
        ipaddress.ip_address(host)
        return True

    except ValueError:
        return False


def check_url_length(url):
    length = len(url)

    if length < 50:
        return length, "Normal"

    elif length < 75:
        return length, "Suspicious"

    else: 
        return length, "Highly Suspicious"


def check_dot_count(domain):
    dot_count = domain.count(".")

    if dot_count <= 2:
        status = "Normal"

    elif dot_count <= 4:
        status = "Suspicious"

    else: 
        status = "Highly Suspicious"

    return dot_count, status


def check_url_shortener(domain):
    domain = domain.lower()
    
    return domain in URL_SHORTENERS


def check_special_characters(url):

    findings = []

    if "@" in url:
        findings.append("@ symbol")

    if "%" in url:
        findings.append("Encoded character (%)")

    if "_" in url:
        findings.append("Underscore (_)")

    if url.count("-") >= 3:
        findings.append("Multiple hyphens")

    return findings


def check_typosquatting(domain):
    """
    Checks if a domain closely resembles a trusted domain.
    Returns the matching trusted domain if found,
    otherwise returns None.
    """

    domain = domain.lower()

    for trusted in TRUSTED_DOMAINS:

        if domain == trusted:
            return None

        similarity = SequenceMatcher(
            None,
            domain,
            trusted
        ).ratio()

        if similarity >= 0.85:
            return trusted

    return None