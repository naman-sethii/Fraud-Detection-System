import matplotlib.pyplot as plt


def generate_pie_chart(high, medium, safe):

    labels = ["High Risk", "Medium Risk", "Safe"]

    values = [high, medium, safe]

    plt.figure(figsize=(6,6))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Fraud Distribution")

    plt.savefig("static/charts/pie_chart.png")

    plt.close()