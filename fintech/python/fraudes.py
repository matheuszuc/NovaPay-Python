import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../dados/fintech_transactions.csv")


fraudes = df[df["is_fraud_flag"] == True]
print(fraudes["type"].value_counts())


fraudes_tipo = df.groupby("type")["is_fraud_flag"].mean()
print(fraudes_tipo)

transacoes = df.groupby("is_fraud_flag")["amount_brl"].mean()
print(transacoes)

df.boxplot(column="amount_brl", by="is_fraud_flag")
plt.show()