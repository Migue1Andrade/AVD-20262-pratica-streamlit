import pandas as pd
import streamlit as st

from src.data_loader import load_data

st.set_page_config(
    page_title="Hotel Booking Demand: correlação e distribuição",
    page_icon=":material/hotel:",
    layout="wide",
)

st.title("Hotel Booking Demand: correlação e distribuição das variáveis quantitativas")

df = load_data()

# Variáveis quantitativas do estudo (mesma lista VARS_QUANT do notebook de EDA)
VARS_QUANT = ["lead_time", "total_of_special_requests", "adr", "stays_in_week_nights", "previous_cancellations"]

# Rótulos legíveis (mesmo dicionário ROTULOS do notebook de EDA)
ROTULOS = {
    "lead_time": "Antecedência da reserva (dias)",
    "total_of_special_requests": "Pedidos especiais",
    "adr": "Diária média (€)",
    "stays_in_week_nights": "Noites em dias de semana",
    "previous_cancellations": "Cancelamentos anteriores",
}

# Sidebar: filtros (variáveis + intervalo)
with st.sidebar:
    st.header("Filtros")

    variaveis = st.pills(
        "Variáveis quantitativas",
        options=VARS_QUANT,
        default=VARS_QUANT,
        selection_mode="multi",
        format_func=ROTULOS.get,
        help="Variáveis que entram na correlação e ficam disponíveis para a distribuição.",
    )

    separar_por_situacao = st.toggle(
        "Distinguir por situação da reserva",
        value=False,
        help="Colore a distribuição pela situação da reserva (cancelamento: Mantida ou Cancelada).",
    )

    st.subheader("Intervalos")
    st.caption("Restrinja a faixa de valores para excluir extremos e ver se a análise muda.")

    # Um slider de intervalo para cada variável selecionada
    intervalos = {}
    for var in variaveis:
        if pd.api.types.is_integer_dtype(df[var]):
            minimo, maximo, passo = int(df[var].min()), int(df[var].max()), 1
        else:
            minimo, maximo, passo = float(df[var].min()), float(df[var].max()), 1.0
        intervalos[var] = st.slider(
            ROTULOS[var],
            min_value=minimo,
            max_value=maximo,
            value=(minimo, maximo),
            step=passo,
            key=f"intervalo_{var}",
        )

# Mantém só as reservas dentro de todos os intervalos escolhidos
df_filtrado = df
for var, (inicio, fim) in intervalos.items():
    df_filtrado = df_filtrado[df_filtrado[var].between(inicio, fim)]

st.caption(f"{len(df_filtrado):,} de {len(df):,} reservas dentro dos intervalos escolhidos.".replace(",", "."))

# Dashboard 1: correlação (heatmap) à esquerda, distribuição (histograma) à direita
col_correlacao, col_distribuicao = st.columns([1, 1.5])

with col_correlacao:
    with st.container(border=True, height="stretch"):
        st.subheader("Correlação")

        if len(variaveis) < 2:
            st.warning("Selecione pelo menos 2 variáveis para calcular a correlação.")
        else:
            # TODO (Aula 22): matriz de correlação de Spearman (df_filtrado[variaveis].corr(method="spearman")),
            #   já que a EDA mostrou que nenhuma variável é normal
            # TODO (Aula 22): heatmap (plotly px.imshow) e exibir com st.plotly_chart
            st.info("O heatmap de correlação entra na próxima aula.", icon=":material/grid_on:")

with col_distribuicao:
    with st.container(border=True, height="stretch"):
        st.subheader("Distribuição")

        if not variaveis:
            st.warning("Selecione pelo menos 1 variável para ver a distribuição.")
        else:
            variavel_distribuicao = st.selectbox(
                "Variável do histograma",
                options=variaveis,
                format_func=ROTULOS.get,
            )
            # TODO (Aula 22): histograma (plotly px.histogram) de df_filtrado[variavel_distribuicao]
            #   e exibir com st.plotly_chart; se separar_por_situacao: color="cancelamento"
            st.info("O histograma de distribuição entra na próxima aula.", icon=":material/bar_chart:")

# TODO: Dashboard 2 — KPIs (Aula 22)
