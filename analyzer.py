from url_checks import *
from network_checks import *
from reputation import *
from scoring import calculate_score, classify_score
from logger import logger

def analyze_url(url):

    logger.info(f"Starting analysis for {url}")
    parsed = parse_url(url)
    https_status = check_https(parsed)
    keywords = check_suspicious_keywords(url)
    ip_status = contains_ip(parsed["domain"])
    url_length, length_status = check_url_length(url)
    dot_count, dot_status = check_dot_count(parsed["domain"])
    shortener = check_url_shortener(parsed["domain"])
    special_chars = check_special_characters(url)
    typosquatting = check_typosquatting(parsed["domain"])
    domain_age, age_status = check_domain_age(parsed["domain"])
    dns_status, dns_records = check_dns(parsed["domain"])
    
    if https_status:
        ssl_info = check_ssl_certificate(parsed["domain"])
    else: 
        ssl_info = {
            "status": "Not Applicable",
            "issuer": None,
            "expiry": None,
            "days_left": None
        }

    vt_result = check_virustotal(url)

    analysis = {}

    analysis["parsed"] = parsed
    analysis["https"] = https_status
    analysis["keywords"] = keywords
    analysis["ip"] = ip_status
    analysis["url_length"] = url_length
    analysis["length_status"] = length_status
    analysis["dot_count"] = dot_count
    analysis["dot_status"] = dot_status
    analysis["shortener"] = shortener
    analysis["special_characters"] = special_chars
    analysis["typosquatting"] = typosquatting
    analysis["domain_age"] = domain_age
    analysis["age_status"] = age_status
    analysis["dns_status"] = dns_status
    analysis["dns_records"] = dns_records
    analysis["ssl"] = ssl_info
    analysis["virustotal"] = vt_result

    logger.info(f"HTTPS: {https_status}")
    logger.info(f"DNS Status: {dns_status}")
    logger.info(f"VirusTotal: {vt_result['status']}")

    logger.info("URL analysis completed.")

    return analysis
    

def analyze_url_complete(url):
    """
    Performs the complete URL analysis, including scoring and risk classification.

    Return: A dictionary containing all analysis results.
    """
    logger.info("analyze_url_complete() called")

    analysis = analyze_url(url)

    score, reasons = calculate_score(analysis)

    risk = classify_score(score)

    logger.info(f"Score: {score}")
    logger.info(f"Risk: {risk}")

    analysis["score"] = score
    analysis["risk"] = risk
    analysis["reasons"] = reasons

    logger.info("Analysis completed successfully.")

    return {
        "url": url,

        "basic_info": {
            "scheme": analysis["parsed"]["scheme"],
            "domain": analysis["parsed"]["domain"],
            "path": analysis["parsed"]["path"],
            "query": analysis["parsed"]["query"]
        },

        "checks": {
            "https": analysis["https"],
            "ip_address": analysis["ip"],
            "keywords": analysis["keywords"],
            "url_length": analysis["url_length"],
            "length_status": analysis["length_status"],
            "dot_count": analysis["dot_count"],
            "dot_status": analysis["dot_status"],
            "shortener": analysis["shortener"],
            "special_characters": analysis["special_characters"],
            "typosquatting": analysis["typosquatting"],
            "dns_status": analysis["dns_status"],
            "dns_records": analysis["dns_records"],
            "domain_age": analysis["domain_age"],
            "age_status": analysis["age_status"]
        },

        "ssl": analysis["ssl"],

        "virustotal": analysis["virustotal"],

        "result": {
            "score": score,
            "risk": risk,
            "reasons": reasons
        }
    }