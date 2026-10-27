# Template: rascunho de layout → esqueleto do app

Preencha cada bloco e envie à ferramenta de IA.

## Contexto

Sou aluno da disciplina Análise e Visualização de Dados (Cesar School, 2026.2). Estou construindo o Dashboard 1 (correlação + distribuição das variáveis quantitativas) em Streamlit a partir da minha EDA da Aula 11, feita no dataset **Hotel Booking Demand** (Kaggle, `mojtaba142/hotel-booking`): reservas de dois hotéis portugueses (City e Resort) entre 2015 e 2017, com o alvo `cancelamento` (Mantida / Cancelada).

Estrutura do repositório: `app.py` na raiz, `src/data_loader.py` com `load_data()` lendo `data/clean/dataset.csv` (exportado ao final de `notebooks/eda.ipynb`), `.streamlit/config.toml` com o tema.

## Entrada

Rascunho do layout: `prompts/rascunho_dashboard1.png`.

Colunas usadas no dashboard (as mesmas `VARS_QUANT` da EDA):

| Coluna | Rótulo | Tipo |
| --- | --- | --- |
| `lead_time` | Antecedência da reserva (dias) | inteiro |
| `total_of_special_requests` | Pedidos especiais | inteiro |
| `adr` | Diária média (€) | decimal |
| `stays_in_week_nights` | Noites em dias de semana | inteiro |
| `previous_cancellations` | Cancelamentos anteriores | inteiro |
| `cancelamento` | Situação da reserva (Mantida / Cancelada) | texto |

Perguntas que o dashboard deve responder:

1. Como as variáveis quantitativas se correlacionam entre si?
2. Como cada variável se distribui, e essa distribuição muda entre reservas mantidas e canceladas?
3. Remover os valores extremos (ex.: diárias muito altas, antecedências acima de 1 ano) muda essas conclusões?

Descrição do layout: sidebar à esquerda com o seletor de variáveis, um toggle para separar por situação da reserva e um slider de intervalo por variável selecionada; na área principal, uma linha com a contagem de reservas filtradas e, abaixo, dois blocos lado a lado: Correlação (mais estreito) e Distribuição (mais largo).

## Restrições

- Streamlit (API atual, seguindo as skills de `.claude/skills/developing-with-streamlit`) e plotly para os gráficos futuros.
- Editar somente `app.py`; carregar os dados apenas via `src/data_loader.py` (com `st.cache_data`).
- Gerar só o esqueleto estrutural, sem lógica de gráficos: os espaços do heatmap e do histograma ficam com placeholders.
- Widgets mínimos: 1 seletor de variáveis e 1 filtro de intervalo (slider).
- Não usar CSS customizado nem `unsafe_allow_html`.

## Formato de saída

Um único `app.py` completo, pronto para `streamlit run app.py`, com comentários `# TODO` marcando onde entram o heatmap, o histograma e o Dashboard 2.
