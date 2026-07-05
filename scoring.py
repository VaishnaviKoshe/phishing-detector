def calculate_score(analysis):
    https_status = analysis["https"]
    keywords = analysis["keywords"] 
    ip_status = analysis["ip"]
    length_status = analysis["length_status"]
    dot_status = analysis["dot_status"]
    shortener = analysis["shortener"]
    special_chars = analysis["special_characters"]
    typosquatting = analysis["typosquatting"]
    age_status = analysis["age_status"]
    dns_status = analysis["dns_status"]
    ssl_info = analysis["ssl"]
    vt = analysis["virustotal"]
    
    score = 0
    reasons = []

    if not https_status:
        score += 20
        reasons.append("Uses HTTP instead of HTTPS")

    if ip_status: 
        score += 30
        reasons.append("Uses an IP address instead of a domain")

    if keywords:
        score += len(keywords) * 10
        reasons.append(f"Contains suspicious keywords: {','.join(keywords)}")

    if length_status == "Suspicious":
        score += 10
        reasons.append("URL is unusually long")

    elif length_status == "Highly Suspicious":
        score += 20
        reasons.append("URL is extremely long")

    if shortener:
        score += 25
        reasons.append("Uses a URL shortening service")

    if dot_status == "Suspicious":
        score += 10
        reasons.append("Contains multiple subdomains")

    elif dot_status == "Highly Suspicious":
        score += 20
        reasons.append("Contains excessive subdomains")

    if special_chars:
        score += len(special_chars) * 10
        reasons.append(f"Contains suspicious characters: {','.join(special_chars)}")

    if typosquatting:
        score += 35
        reasons.append(f"Domain resembles trusted site: {typosquatting}")

    if age_status == "Suspicious":
        score += 15
        reasons.append("Domain is relatively new")

    elif age_status == "Highly Suspicious":
        score += 30
        reasons.append("Domain was registered very recently")

    if dns_status == "Invalid":
        score += 25
        reasons.append("Domain has no valid DNS records")

    if ssl_info["status"] == "Unavailable":
        score += 20
        reasons.append("SSL certificate unavailable")

    elif ssl_info["status"] == "Expired":
        score += 25
        reasons.append("SSL certificate has expired")

    elif ssl_info["status"] == "Expiring Soon":
        score += 5
        reasons.append("SSL certificate expires soon")

    if vt["status"] == "Available":
        if vt["malicious"] > 0:
            score += min(vt["malicious"] * 5, 40)
            reasons.append(
                f"VirusTotal detected malicious activity({vt['malicious']} vendors)"
            )

        elif vt["suspicious"] > 0:
            score += min(vt["suspicious"] * 3, 20)
            reasons.append(
                f"VirusTotal flagged URL as suspicious({vt['suspicious']} vendors)"
            )

    if score > 100:
        score = 100

    if not reasons:
        reasons.append("No suspicious indicators detected.")

    return score, reasons


def classify_score(score):
    
    if score == 0:
        return "SAFE"

    elif score <= 20:
        return "LOW"

    elif score <= 50:
        return "MEDIUM"

    elif score <= 80:
        return "HIGH"

    else:
        return "CRITICAL"


 