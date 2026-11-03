# 📉 Análise de Cancelamento de Clientes

Notebook Jupyter com análise exploratória de uma base de **50.000 clientes**. O objetivo é encontrar os fatores ligados ao cancelamento (churn).

## Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `analise.ipynb` | Notebook com a análise passo a passo |
| `cancelamentos.csv` | Base de dados (~3,4 MB) |

## Pré-requisitos

| Item | Observação |
|------|------------|
| Python | 3.9 ou superior |
| Jupyter | `notebook`, `jupyterlab` ou a extensão Jupyter do VS Code |
| pandas, plotly | Ver `requirements.txt` |
| nbformat | Exigido pelo `plotly` para exibir gráficos no notebook |

## Execução

```bash
pip install -r requirements.txt
jupyter notebook analise.ipynb
```

> Rode o notebook **de dentro desta pasta**. O CSV é lido por caminho relativo (`pd.read_csv("cancelamentos.csv")`).

## Etapas da análise

1. **Importação:** leitura do CSV e remoção da coluna `CustomerID`.
2. **Inspeção:** `info()` para ver tipos e valores nulos.
3. **Tratamento:** remoção de linhas com nulos (`dropna`).
4. **Análise inicial:** proporção de clientes que cancelaram (`value_counts(normalize=True)`).
5. **Análise detalhada:** um histograma por coluna, com cor por `cancelou`.
6. **Hipóteses:** filtros nos grupos de maior risco, como contratos mensais, e recálculo da taxa de cancelamento.

## Dicionário de dados

| Coluna | Descrição |
|--------|-----------|
| `CustomerID` | Identificador do cliente (removido na análise) |
| `idade` | Idade |
| `sexo` | Sexo |
| `tempo_como_cliente` | Meses como cliente |
| `frequencia_uso` | Frequência de uso do serviço |
| `ligacoes_callcenter` | Ligações para o call center |
| `dias_atraso` | Dias de atraso no pagamento |
| `assinatura` | Plano (`Basic`, `Standard`, `Premium`) |
| `duracao_contrato` | `Monthly`, `Quarterly` ou `Annual` |
| `total_gasto` | Valor total gasto |
| `meses_ultima_interacao` | Meses desde a última interação |
| `cancelou` | `1` = cancelou, `0` = ativo |

## Observações

- Os outputs (gráficos) foram removidos do notebook versionado para reduzir o tamanho de ~7 MB. Execute as células para gerá-los de novo.
- `display()` só funciona em ambiente Jupyter. Fora dele, use `print()`.
