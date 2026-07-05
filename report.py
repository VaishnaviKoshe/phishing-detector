def print_report(url, result):

    analysis = result
    vt = analysis["virustotal"]
    ssl = analysis["ssl"]
    
    score = result["score"]

    risk = result["risk"]

    reasons = result["reasons"]
    
    print("\n" + "=" * 45)
    print("PHISHING DETECTION REPORT")
    print("=" * 45)

    print("\nURL")
    print("-" * 25)
    print(url)

    print("\nBasic URL Information")
    print("-" * 25)
    print(f"Scheme             : {analysis['parsed']['scheme']}")
    print(f"Domain             : {analysis['parsed']['domain']}")
    print(f"Path               : {analysis['parsed']['path']}")
    print(f"Query              : {analysis['parsed']['query']}")

    https = "Yes" if analysis["https"] else "No"
    ip = "Yes" if analysis["ip"] else "No"

    print("\nSecurity Analysis")
    print("-" * 25)

    print(f"HTTPS              : {https}")
    print(f"Uses IP Address    : {ip}")

    shortener = "Yes" if analysis["shortener"] else "No"
    print(f"URL Shorteners     : {shortener}")

    print(f"URL Length         : {analysis['url_length']}")
    print(f"Length Status      : {analysis['length_status']}")
    print(f"Dot Count          : {analysis['dot_count']}")
    print(f"Dot Status         : {analysis['dot_status']}")
    print(f"Keywords Found     : {analysis['keywords']}")


    if analysis["special_characters"]:
        print("Special Characters :", ",".join(analysis["special_characters"]))
    else:
        print("Special Characters : None")


    if analysis["typosquatting"]:
        print(f"Typosquatting     : Similar to {analysis['typosquatting']}")
    else:
        print("Typosquatting      : None")


    print(f"Domain Age (days)  : {analysis['domain_age']}")
    print(f"Age Status         : {analysis['age_status']}")


    print(f"DNS Status         : {analysis['dns_status']}")
    print("DNS Records        :")
    if analysis["dns_records"]:
        for record in analysis["dns_records"]:
            print(f" - {record}")
    else: 
        print(" None")


    print("\nSSL Certificate")
    print("-" * 25)

    print(f"Status             : {ssl['status']}")
    print(f"Issuer             : {ssl['issuer']}")
    print(f"Expiry Date        : {ssl['expiry']}")
    print(f"Days Left          : {ssl['days_left']}")

    print("\nVirusTotal")
    print("-" * 25)

    print(f"Status             : {vt['status']}")

    if vt["status"] == "Available":
        print(f"Malicious          : {vt['malicious']}")
        print(f"Suspicious         : {vt['suspicious']}")
        print(f"Harmless           : {vt['harmless']}")

    print("\nReasons")
    print("-" * 25)

    if reasons:
        for reason in reasons:
            print(f"- {reason}")
    else:
        print("No Suspicious Indicators Found.")

    print("\n" + "=" * 45)
    print(f"Risk Score         : {score}/100")
    print(f"Risk Level         : {risk}")
    print("=" * 45)