import whois
import dns.resolver
import socket
import ssl

from datetime import datetime

def check_domain_age(domain):
    """
    Checks the age of a domain using WHOIS information.
    Returns: (age_in_days, status)
    """

    try:
        domain = domain.split(":")[0]
        info = whois.whois(domain)

        creation_date = info.creation_date

        if not creation_date:
            return None, "Unknown"

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date.tzinfo is not None:
            creation_date = creation_date.replace(tzinfo=None)

        age = (datetime.utcnow() - creation_date).days

        if age < 30:
            status = "Highly Suspicious"
        elif age < 180:
            status = "Suspicious"
        else:
            status = "Normal"

        return age, status

    except Exception as e:
        print("WHOIS Error:", e)
        return None, "Unknown"


def check_dns(domain):
    """
    Checks whether a domain has valid DNS A records.
    Returns: (status, ip_addresses)
    """
    try:
        answers = dns.resolver.resolve(domain, "A")
        ips = []

        for answer in answers:
            ips.append(answer.to_text())
        return "Valid", ips

    except Exception:
        return "Invalid", []


def check_ssl_certificate(domain):
    """
    Retrieves SSl certificate information for a domain.
    Returns: {
        "status": "...",
        "issuer": "...",
        "expiry": "...",
        "days_left": "..."
    }
    """
    domain = domain.split(":")[0]
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as secure_sock:
                cert = secure_sock.getpeercert()

                issuer = {}
                for item in cert["issuer"]:
                    issuer.update(dict(item))

                issuer_name = issuer.get("organizationName", "Unknown")
                expiry = datetime.strptime(
                    cert["notAfter"], 
                    "%b %d %H:%M:%S %Y %Z"
                )
                days_left = (expiry - datetime.utcnow()).days
                if days_left < 0:
                    status = "Expired"
                elif days_left < 30:
                    status = "Expiring Soon"
                else:
                    status = "Valid"

                return {
                    "status": status,
                    "issuer": issuer_name,
                    "expiry": expiry.strftime("%Y-%m-%d"),
                    "days_left": days_left
                }

    except Exception as e:
        print("SSL Error:", e)
        return {
            "status": "Unavailable",
            "issuer": None,
            "expiry": None,
            "days_left": None
        }