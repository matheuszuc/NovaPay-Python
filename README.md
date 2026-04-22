# 📊 NovaPay — Análise de Dados Financeiros

Projeto de portfólio simulando o ambiente de dados de uma fintech brasileira fictícia (**NovaPay**).  
O objetivo foi investigar problemas reais de negócio e gerar insights acionáveis a partir de dados brutos.

---

## 🏢 Contexto

A NovaPay é uma fintech que oferece contas digitais, cartões, PIX, empréstimos e suporte ao cliente.  
Como analista de dados júnior, recebi três problemas levantados pelo board e precisei investigá-los com SQL e Python.

---

## 🗂️ Datasets

| Arquivo | Descrição | Registros |
|---|---|---|
| `fintech_clients.csv` | Cadastro de clientes (plano, score, churn, estado) | 3.000 |
| `fintech_accounts.csv` | Contas vinculadas aos clientes | 4.146 |
| `fintech_transactions.csv` | Transações (PIX, TED, cartão, etc.) | 50.000 |
| `fintech_loans.csv` | Empréstimos concedidos | 1.031 |
| `fintech_support.csv` | Tickets de suporte abertos | 1.915 |

---

## 🔧 Ferramentas

- **Python** (Pandas, Matplotlib)
- **PyCharm**
- **Git / GitHub**

---

## 🚨 Problemas Investigados

### 1. Churn por Plano (`01_taxa_cancelamento.py`)
**Hipótese do board:** o plano Básico estava perdendo muitos clientes.

**Resultado:**
| Plano | Taxa de Churn |
|---|---|
| Básico | ~30% |
| Profissional | ~15% |
| Premium | ~7% |

**Conclusão:** hipótese confirmada. O plano Básico lidera o churn com 30%. O plano Profissional também merece atenção com 15% — sinal de alerta secundário.

---

### 2. Inadimplência na Carteira de Crédito (`02_inadimplencia_credito.py`)
**Hipótese do board:** qualidade da carteira de empréstimos estava em risco.

**Resultado:**
- **29% da carteira** está em status "Atrasado" ou "Inadimplente"
- O credit score na concessão **não explica** a inadimplência — distribuição praticamente igual entre todos os status

**Conclusão:** o modelo de concessão de crédito precisa ser revisado. O credit score isolado não é um bom preditor de risco — variáveis como valor do empréstimo e prazo devem ser investigadas.

---

### 3. Perfil das Transações Fraudulentas (`03_fraudes.py`)
**Hipótese do board:** transações suspeitas passando pelo radar.

**Resultado:**
- **Saque** lidera em taxa de fraude por tipo de transação
- Transações fraudulentas têm valor médio **8,5x maior** que transações normais
- Casos extremos ultrapassam **R$ 100.000**

**Conclusão:** o perfil da fraude é de alto valor em operações de saque. O sistema de detecção deve priorizar alertas para saques com valores acima da média.

---

## 💡 Insights Gerados (`04_insights.py`)

### 📍 Distribuição Geográfica
São Paulo concentra a maior base de clientes. Estados como PE, CE e GO apresentam baixa penetração — oportunidade de expansão.

### 📢 Canal de Aquisição vs Retenção
| Canal | Taxa de Churn |
|---|---|
| Google Ads | ~19% ✅ |
| Indicação | ~20% |
| Orgânico | ~21% |
| Instagram | ~20% |
| App Store | ~23% ⚠️ |
| Parceiro | ~24% ⚠️ |

**Recomendação:** priorizar investimento em Google Ads (melhor retenção). Revisar estratégia de aquisição via App Store e Parceiros.

### 🎫 Categorias de Suporte
Fraude e "Outros" lideram os tickets de suporte. A categoria "Outros" sendo tão expressiva indica necessidade de **melhor categorização** e possível lacuna no produto.

---

## 📁 Estrutura do Projeto

```
fintech/
│
├── 01_taxa_cancelamento.py
├── 02_inadimplencia_credito.py
├── 03_fraudes.py
├── 04_insights.py
│
├── fintech_clients.csv
├── fintech_accounts.csv
├── fintech_transactions.csv
├── fintech_loans.csv
├── fintech_support.csv
│
└── README.md
```

---

## 🧠 Aprendizados

- Números absolutos enganam — sempre normalizar antes de comparar grupos
- Média esconde distribuição — boxplot revela o que `groupby().mean()` não mostra
- Um bom insight não é só "achei curioso" — precisa ter **recomendação de negócio**

---

*Projeto desenvolvido como parte do portfólio de análise de dados.*
