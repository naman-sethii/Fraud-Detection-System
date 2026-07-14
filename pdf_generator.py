#Can be implemented later on (out of scope for now)

# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet

# def generate_pdf(report):

#     document = SimpleDocTemplate("Fraud_Investigation_Report.pdf")

#     styles = getSampleStyleSheet()

#     story = []

#     story.append(Paragraph(report, styles["BodyText"]))

#     document.build(story)

# if __name__ == "__main__":

#     sample = """
# Fraud Investigation Report

# Executive Summary

# This is a sample report generated using Gemini AI.

# Risk Assessment

# High risk activity detected.

# Recommendations

# Review flagged transactions.

# Conclusion

# Fraud monitoring is functioning correctly.
# """

#     generate_pdf(sample)