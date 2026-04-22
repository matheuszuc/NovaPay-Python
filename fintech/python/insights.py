import pandas as pd
import matplotlib.pyplot as plt


df_clients = pd.read_csv("../dados/fintech_clients.csv")
df_support = pd.read_csv("../dados/fintech_support.csv")


# Canais de Aquisição
marketing = df_clients["acquisition_ch"].value_counts()
print(marketing)


# Taxa de Cancelamento no Marketing
marketing_churned = df_clients.groupby("acquisition_ch")["churned"].mean() * 100
print(marketing_churned)

marketing_churned.sort_values(ascending=False).plot(kind="bar", title="Marketing Churn")
plt.xlabel("")
plt.ylabel("Taxa de Cancelamento (%)")
plt.tight_layout ()
plt.savefig("fintech_churn.png")
plt.show()



marketing.plot(kind="bar", title="Marketing")
plt.xlabel("Marketing")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.savefig("marketing.png")
plt.show()


# Distribuição por Estado
estado = df_clients["state"].value_counts()
print(estado)
estado.plot(kind="barh", title="Estado")
plt.xlabel("Quantidade")
plt.ylabel("Estado")
plt.tight_layout()
plt.savefig("Clientes_por_estado.png")
plt.show()


# Onde melhorar no Suporte
suporte = df_support["category"].value_counts()
print(suporte)
suporte.plot(kind="barh", title="Suporte")
plt.xlabel("Quantidade")
plt.ylabel("")
plt.tight_layout()
plt.savefig("fintech_support.png")
plt.show()



