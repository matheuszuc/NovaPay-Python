import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("../dados/fintech_clients.csv")


planos = df["plan"].value_counts()
print(planos)

planos_churned = df.groupby("plan")["churned"].mean() *100
print(planos_churned)


planos_churned.plot(kind="barh", title="Taxa de Cancelamento")
plt.ylabel("Planos")
plt.xlabel("Taxa de Cancelamento")
plt.tight_layout()
plt.savefig("taxa_de_cancelamento.png")
plt.show()

