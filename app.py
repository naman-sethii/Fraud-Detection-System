from flask import Flask, render_template, request
import pandas as pd
from fraud_engine import calculate_risk, calculate_probability
import numpy as np
from visualization import generate_pie_chart

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["csvFile"]

    print("File Received Successfully!")
    print("Filename:", file.filename)

    df = pd.read_csv(file)

    df["Risk Score"] = 0
    df["Fraud Probability"] = ""
    df["Status"] = ""
    df["Reasons"] = ""
    

    for index, row in df.iterrows():

        score, status, reasons = calculate_risk(row)

        probability = calculate_probability(score)

        df.at[index, "Risk Score"] = score

        df.at[index, "Fraud Probability"] = f"{probability}%"

        df.at[index, "Status"] = status

        df.at[index, "Reasons"] = ", ".join(reasons)

    print(df)

    total_transactions = len(df)

    high_risk = len(df[df["Status"] == "High Risk"])

    medium_risk = len(df[df["Status"] == "Medium Risk"])

    safe = len(df[df["Status"] == "Safe"])

    generate_pie_chart(high_risk, medium_risk, safe)
    
    print("Total :", total_transactions)

    print("High :", high_risk)

    print("Medium :", medium_risk)

    print("Safe :", safe)

    risk_scores = df["Risk Score"].to_numpy(dtype=np.int32)

    average_risk = np.mean(risk_scores)

    highest_risk = np.max(risk_scores)

    lowest_risk = np.min(risk_scores)

    risk_std = np.std(risk_scores)

    median_risk = np.median(risk_scores)

    percentage_high = np.round((high_risk / total_transactions) * 100, 2)

    percentage_safe = np.round((safe / total_transactions) * 100, 2)


if __name__ == "__main__":
    app.run(debug=True)