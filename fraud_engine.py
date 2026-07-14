#Configurable weights and thresholds (can be altered later)

HOME_COUNTRY = "India"

# Transaction Thresholds
AMOUNT_LIMIT = 50000
VERY_HIGH_AMOUNT = 100000

# Login Attempt Thresholds
LOGIN_ATTEMPT_LIMIT = 4
HIGH_LOGIN_ATTEMPT_LIMIT = 8

# Risk Weights
AMOUNT_RISK = 40
VERY_HIGH_AMOUNT_RISK = 20
NEW_DEVICE_RISK = 30
FOREIGN_LOCATION_RISK = 40
LOGIN_ATTEMPTS_RISK = 50
HIGH_LOGIN_ATTEMPTS_RISK = 100

# Risk Classification Thresholds
MEDIUM_RISK_THRESHOLD = 40
HIGH_RISK_THRESHOLD = 80

# Maximum Possible Risk Score
MAX_RISK_SCORE = (
    AMOUNT_RISK +
    VERY_HIGH_AMOUNT_RISK +
    NEW_DEVICE_RISK +
    FOREIGN_LOCATION_RISK +
    HIGH_LOGIN_ATTEMPTS_RISK
)


def calculate_risk(transaction):

    risk_score = 0
    reasons = []

    # Rule 1 : High Transaction Amount
    if transaction["Amount"] > AMOUNT_LIMIT:
        risk_score += AMOUNT_RISK
        reasons.append("High Transaction Amount")

    # Rule 2 : Very High Transaction Amount
    if transaction["Amount"] > VERY_HIGH_AMOUNT:
        risk_score += VERY_HIGH_AMOUNT_RISK
        reasons.append("Very High Transaction Amount")

    # Rule 3 : New Device Used
    if transaction["Device"] == "New Device":
        risk_score += NEW_DEVICE_RISK
        reasons.append("New Device Used")

    # Rule 4 : Foreign Transaction
    if transaction["Location"] != HOME_COUNTRY:
        risk_score += FOREIGN_LOCATION_RISK
        reasons.append("Foreign Transaction")

    # Rule 5 : Login Attempts
    if transaction["LoginAttempts"] >= HIGH_LOGIN_ATTEMPT_LIMIT:
        risk_score += HIGH_LOGIN_ATTEMPTS_RISK
        reasons.append("Very High Login Attempts")

    elif transaction["LoginAttempts"] > LOGIN_ATTEMPT_LIMIT:
        risk_score += LOGIN_ATTEMPTS_RISK
        reasons.append("Login Attempts Exceeded")

    # Final Risk Status
    if risk_score >= HIGH_RISK_THRESHOLD:
        status = "High Risk"

    elif risk_score >= MEDIUM_RISK_THRESHOLD:
        status = "Medium Risk"

    else:
        status = "Safe"

    return risk_score, status, reasons


def calculate_probability(score):

    # Probability cannot exceed 100%
    return min(score, 100)