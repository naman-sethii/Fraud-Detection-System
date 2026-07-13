# Risk Configuration with configurable variables
HOME_COUNTRY = "India"

AMOUNT_LIMIT = 50000
VERY_HIGH_AMOUNT = 100000

AMOUNT_RISK = 40
VERY_HIGH_AMOUNT_RISK = 20
NEW_DEVICE_RISK = 30
FOREIGN_LOCATION_RISK = 20

HIGH_RISK_THRESHOLD = 70
MEDIUM_RISK_THRESHOLD = 40

#  For configurations (later purposes, if need to add fields)
MAX_RISK_SCORE = (
    AMOUNT_RISK +
    VERY_HIGH_AMOUNT_RISK +
    NEW_DEVICE_RISK +
    FOREIGN_LOCATION_RISK
)


def calculate_risk(transaction):

    risk_score = 0
    reasons = []

    # Rule 1
    if transaction["Amount"] > AMOUNT_LIMIT:
        risk_score += AMOUNT_RISK
        reasons.append("High Transaction Amount")

    # Rule 2
    if transaction["Amount"] > VERY_HIGH_AMOUNT:
        risk_score += VERY_HIGH_AMOUNT_RISK
        reasons.append("Very High Transaction Amount")

    # Rule 3
    if transaction["Device"] == "New Device":
        risk_score += NEW_DEVICE_RISK
        reasons.append("New device used")

    # Rule 4
    if transaction["Location"] != HOME_COUNTRY:
        risk_score += FOREIGN_LOCATION_RISK
        reasons.append("Foreign Transaction")

    if risk_score >= HIGH_RISK_THRESHOLD:
        status = "High Risk"

    elif risk_score >= MEDIUM_RISK_THRESHOLD:
        status = "Medium Risk"

    else:
        status = "Safe"

    return risk_score, status, reasons

# Helping out risk probability 

def calculate_probability(score):
    return round((score / MAX_RISK_SCORE) * 100)