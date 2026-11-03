from datetime import date
from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

# Titulo do sitena na paginação
#st.title("Análise de Vendas")

#st.write("# Sistema de Análise de Dados")
#st.write("## Cadastrar Vendas")
#st.write("## Vendas Cadastradas")
#st.write("## Dashboard")

# Executar: python -m streamlit run sistema.py

st.set_page_config(page_title="Análise de Vendas", page_icon="📊", layout="wide")

# Caminho relativo ao script, não ao diretório de execução
ARQUIVO = Path(__file__).parent / "vendas.csv"
PRECOS = {"Celular": 2000.0, "Notebook": 3500.0, "Fone": 150.0}
VENDEDORES = ["Ana", "Bruno", "Carla"]


def brl(valor: float) -> str:
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


@st.cache_data
def carregar_dados() -> pd.DataFrame:
    return pd.read_csv(ARQUIVO, parse_dates=["data"])


def salvar_venda(venda: dict) -> None:
    pd.DataFrame([venda]).to_csv(
        ARQUIVO, mode="a", header=not ARQUIVO.exists(), index=False
    )
    carregar_dados.clear()  # invalida o cache para a próxima leitura


st.title("📊 Sistema de Análise de Vendas")

aba_cadastro, aba_vendas, aba_dashboard = st.tabs(
    ["📝 Cadastrar Venda", "📋 Vendas Cadastradas", "📈 Dashboard"]
)

# ---------- CADASTRO (antes de carregar, para a venda nova já aparecer) ----------
with aba_cadastro:
    with st.form("form_venda", clear_on_submit=True):
        col1, col2 = st.columns(2)
        data_venda = col1.date_input("Data", value=date.today(), format="DD/MM/YYYY")
        vendedor = col2.selectbox("Vendedor", VENDEDORES)
        produto = col1.selectbox("Produto", list(PRECOS))
        quantidade = col2.number_input("Quantidade", min_value=1, max_value=100, step=1)
        enviado = st.form_submit_button("Cadastrar venda", type="primary")

    if enviado:
        valor = PRECOS[produto] * quantidade
        salvar_venda({
            "data": data_venda.isoformat(),
            "vendedor": vendedor,
            "produto": produto,
            "quantidade": int(quantidade),
            "valor": valor,
        })
        st.success(f"Venda cadastrada: {quantidade}x {produto} ({vendedor}) — {brl(valor)}")

tabela = carregar_dados()

# ---------- FILTROS ----------
with st.sidebar:
    st.header("🔎 Filtros")
    vendedores_sel = st.multiselect("Vendedor", sorted(tabela["vendedor"].unique()),
                                    default=sorted(tabela["vendedor"].unique()))
    produtos_sel = st.multiselect("Produto", sorted(tabela["produto"].unique()),
                                  default=sorted(tabela["produto"].unique()))
    data_min, data_max = tabela["data"].min().date(), tabela["data"].max().date()
    periodo = st.date_input("Período", value=(data_min, data_max),
                            min_value=data_min, max_value=data_max, format="DD/MM/YYYY")
    # Durante a seleção, o intervalo vem com 1 data só
    inicio, fim = periodo if len(periodo) == 2 else (periodo[0], periodo[0])

filtro = (
    tabela["vendedor"].isin(vendedores_sel)
    & tabela["produto"].isin(produtos_sel)
    & tabela["data"].dt.date.between(inicio, fim)
)
df = tabela[filtro]

# ---------- VENDAS CADASTRADAS ----------
with aba_vendas:
    st.caption(f"{len(df)} de {len(tabela)} vendas exibidas")
    st.dataframe(
        df.sort_values("data", ascending=False),
        hide_index=True,
        column_config={
            "data": st.column_config.DateColumn("Data", format="DD/MM/YYYY"),
            "vendedor": "Vendedor",
            "produto": "Produto",
            "quantidade": "Qtd.",
            "valor": st.column_config.NumberColumn("Valor", format="R$ %.2f"),
        },
    )
    st.download_button("⬇️ Baixar CSV filtrado", df.to_csv(index=False).encode("utf-8"),
                       "vendas_filtradas.csv", "text/csv")

# ---------- DASHBOARD ----------
with aba_dashboard:
    if df.empty:
        st.warning("Nenhuma venda para os filtros selecionados.")
    else:
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Faturamento", brl(df["valor"].sum()))
        c2.metric("Nº de vendas", len(df))
        c3.metric("Ticket médio", brl(df["valor"].mean()))
        c4.metric("Itens vendidos", int(df["quantidade"].sum()))

        g1, g2 = st.columns(2)

        mensal = (df.groupby(df["data"].dt.to_period("M").astype(str))["valor"]
                    .sum().reset_index(name="faturamento"))
        g1.plotly_chart(px.bar(mensal, x="data", y="faturamento",
                               title="Faturamento por mês", labels={"data": "Mês"}))

        por_vendedor = (df.groupby("vendedor")["valor"].sum()
                          .sort_values(ascending=False).reset_index())
        g2.plotly_chart(px.bar(por_vendedor, x="vendedor", y="valor",
                               title="Faturamento por vendedor", color="vendedor"))

        g3, g4 = st.columns(2)

        por_produto = df.groupby("produto")["valor"].sum().reset_index()
        g3.plotly_chart(px.pie(por_produto, names="produto", values="valor",
                               title="Participação por produto", hole=0.4))

        diario = df.groupby("data")["valor"].sum().reset_index()
        g4.plotly_chart(px.line(diario, x="data", y="valor",
                                title="Evolução diária", markers=True))