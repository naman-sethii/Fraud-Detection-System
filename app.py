from flask import Flask, render_template, request
import pandas as pd
from fraud_engine import calculate_risk, calculate_probability
import numpy as np
from visualization import generate_pie_chart, generate_bar_chart, generate_reason_chart, generate_scatter_plot
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
def home():

    return render_template(

        "dashboard.html",

        total_transactions=0,
        high_risk=0,
        medium_risk=0,
        safe=0,

        average_risk=0,
        highest_risk=0,
        lowest_risk=0,
        median_risk=0,
        risk_std=0,

        transactions=[]
    )

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

    total_transactions = len(df)

    high_risk = len(df[df["Status"] == "High Risk"])

    medium_risk = len(df[df["Status"] == "Medium Risk"])

    safe = len(df[df["Status"] == "Safe"])

    generate_pie_chart(high_risk, medium_risk, safe)
    generate_bar_chart(df)
    generate_reason_chart(df)
    generate_scatter_plot(df)
    
    risk_scores = df["Risk Score"].to_numpy(dtype=np.int32)

    average_risk = np.mean(risk_scores)

    highest_risk = np.max(risk_scores)

    lowest_risk = np.min(risk_scores)

    risk_std = np.std(risk_scores)

    median_risk = np.median(risk_scores)

    percentage_high = np.round((high_risk / total_transactions) * 100, 2)

    percentage_safe = np.round((safe / total_transactions) * 100, 2)

    return render_template(

        "dashboard.html",

        total_transactions=total_transactions,

        high_risk=high_risk,

        medium_risk=medium_risk,

        safe=safe,

        average_risk=round(average_risk, 2),

        highest_risk=highest_risk,

        lowest_risk=lowest_risk,

        median_risk=median_risk,

        risk_std=round(risk_std, 2),

        transactions = df.to_dict(orient = "records")
    
    )


if __name__ == "__main__":
    app.run(debug=True)