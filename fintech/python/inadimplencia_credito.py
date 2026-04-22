import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../dados/fintech_loans.csv")


atraso = df["status"].value_counts(normalize=True)
print(atraso)

score = df.groupby("status")["credit_score_at"].mean()
print(score)


df.boxplot(column="credit_score_at", by="status")
plt.show()