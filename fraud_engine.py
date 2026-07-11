def calculate_risk(transaction):

    risk_score = 0

    # Rule 1
    if transaction["Amount"] > 50000:
        risk_score += 40

    # Rule 2
    if transaction["Amount"] > 100000:
        risk_score += 20

    # Rule 3
    if transaction["Device"] == "New Device":
        risk_score += 30

    # Rule 4
    if transaction["Location"] != "India":
        risk_score += 20

    if risk_score >= 70:
        status = "High Risk"

    elif risk_score >= 40:
        status = "Medium Risk"

    else:
        status = "Safe"

    return risk_score, status