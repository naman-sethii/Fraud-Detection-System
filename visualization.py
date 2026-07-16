import matplotlib.pyplot as plt


def generate_pie_chart(high, medium, safe):

    labels = ["High Risk", "Medium Risk", "Safe"]

    sizes = [high, medium, safe]

    plt.figure(figsize=(6,6))

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Fraud Distribution")

    plt.savefig("static/charts/pie_chart.png")

    plt.close()

def generate_bar_chart(df):
    
    transaction_ids = df["TransactionID"]
    risk_scores = df["Risk Score"]
    statuses = df["Status"]
    colors = []

    for status in statuses:

        if status == "High Risk":
            colors.append("red")

        elif status == "Medium Risk":
            colors.append("orange")

        else:
            colors.append("green")


    plt.figure(figsize=(8,5))

    plt.bar(transaction_ids, risk_scores, color=colors)

    plt.title("Risk Score Distribution")
    plt.xlabel("Transaction ID")
    plt.ylabel("Risk Score")

    plt.savefig("static/charts/bar_chart.png")
    plt.close()

def generate_reason_chart(df):
    reason_count = {}

    for reasons in df["Reasons"]:
        reason_list = reasons.split(", ")
    
        for reason in reason_list:

            reason = reason.strip()

            if reason == "":
                continue

            if reason in reason_count:
                reason_count[reason] += 1
            else:
                reason_count[reason] = 1
    
    labels = list(reason_count.keys())

    counts = list(reason_count.values())

    plt.figure(figsize=(8,5))

    plt.barh(labels, counts)

    plt.title("Fraud Indicator Frequency")

    plt.xlabel("Frequency")

    plt.tight_layout()

    plt.savefig("static/charts/reason_chart.png")

    plt.close()


def generate_scatter_plot(df):

    login_attempts = df["LoginAttempts"]
    risk_scores = df["Risk Score"]

    plt.figure(figsize=(8,5))

    plt.scatter(login_attempts, risk_scores)

    plt.title("Login Attempts vs Risk Score")

    plt.xlabel("Login Attempts")

    plt.ylabel("Risk Score")

    plt.grid(True)

    plt.savefig("static/charts/scatter_plot.png")

    plt.close()