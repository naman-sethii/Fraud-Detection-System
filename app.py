from flask import Flask, render_template, request
import pandas as pd
from fraud_engine import calculate_risk

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

    df["Status"] = ""

    for index, row in df.iterrows():

        score, status = calculate_risk(row)

        df.at[index, "Risk Score"] = score

        df.at[index, "Status"] = status

    total_transactions = len(df)

    high_risk = len(df[df["Status"] == "High Risk"])

    medium_risk = len(df[df["Status"] == "Medium Risk"])

    safe = len(df[df["Status"] == "Safe"])
    
    print("Total :", total_transactions)

    print("High :", high_risk)

    print("Medium :", medium_risk)

    print("Safe :", safe)

    return "CSV Uploaded Successfully!"




if __name__ == "__main__":
    app.run(debug=True)