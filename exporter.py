import json

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def export_json(result, filename="report.json"):
    with open(filename, "w") as file:
        json.dump(result, file, indent=4)

    return filename

def export_pdf(result, filename="report.pdf"):
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Phishing Detection Report", styles["Title"]))

    story.append(Paragraph(f"<b>URL:</b> {result['url']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Risk Level:</b> {result['result']['risk']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Score:</b> {result['result']['score']}", styles["BodyText"]))

    story.append(Paragraph("<br/><b>SSL Information</b>", styles["Heading2"]))
    story.append(Paragraph(
        f"Status: {result['ssl']['status']}",
        styles["BodyText"]
    ))

    story.append(Paragraph("<br/><b>VirusTotal</b>", styles["Heading2"]))
    story.append(Paragraph(
        f"Status: {result['virustotal']['status']}",
        styles["BodyText"]
    ))

    story.append(Paragraph(
        f"Malicious: {result['virustotal']['malicious']}",
        styles["BodyText"]
    ))

    story.append(Paragraph(
        f"Suspicious: {result['virustotal']['suspicious']}",
        styles["BodyText"]
    ))

    story.append(Paragraph(
        f"Harmless: {result['virustotal']['harmless']}",
        styles["BodyText"]
    ))

    story.append(Paragraph("<br/><b>Reasons</b>", styles["Heading2"]))

    if result["result"]["reasons"]:
        for reason in result["result"]["reasons"]:
            story.append(Paragraph(f"• {reason}", styles["BodyText"]))
    else:
        story.append(Paragraph("No suspicious indicators detected.", styles["BodyText"]))

    doc.build(story)

    return filename