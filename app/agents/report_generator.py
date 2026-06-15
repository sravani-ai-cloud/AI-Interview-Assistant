from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(data):

    filename = "Interview_Report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = [
        Paragraph("AI Interview Report", styles["Title"]),
        Paragraph(f"Candidate: {data.candidate_name}", styles["Normal"]),
        Paragraph(f"Question: {data.question}", styles["Normal"]),
        Paragraph(f"Answer: {data.answer}", styles["Normal"]),
        Paragraph(f"Score: {data.score}", styles["Normal"]),
        Paragraph(f"Recommendation: {data.recommendation}", styles["Normal"]),
    ]

    doc.build(content)

    return {
        "message": "Report Generated",
        "file": filename
    }