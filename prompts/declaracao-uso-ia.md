# Declaração de Uso de IA

**Nome:** Miguel Andrade
**Data:** 22/10/2026

## Ferramenta

Claude Code (modelo Claude Opus 5.5), com as skills do Streamlit instaladas via `streamlit skills` (`.claude/skills/developing-with-streamlit`).

## Prompt usado

Pedido feito ao Claude Code:

> Faça todos os exercícios propostos no documento `Aula-21-Streamlit-parte-1.pdf` do projeto, usando como base o `Aula_11_Pratica_EDA.ipynb`. Ao final, liste tudo que você fez dentro do repositório.

Para o esqueleto do `app.py`, foi usado o prompt estruturado de [layout-skeleton-prompt.md](layout-skeleton-prompt.md) (contexto, entrada com o rascunho `rascunho_dashboard1.png`, restrições e formato de saída).

## O que foi aceito, modificado ou rejeitado e por quê

- **Aceito:**
  - Copiar a EDA da Aula 11 para `notebooks/eda.ipynb` e acrescentar ao final uma seção que salva o dataset original em `data/raw/` e o tratado em `data/clean/`.
  - Remover as colunas `name`, `email`, `phone-number` e `credit_card` do dataset tratado, por serem identificadores pessoais sem valor analítico e porque o arquivo vai para o GitHub.
  - Esqueleto do `app.py` seguindo o rascunho: sidebar com seletor de variáveis (`st.pills`), toggle por situação da reserva e um slider de intervalo por variável; área principal com Correlação e Distribuição lado a lado, com placeholders no lugar dos gráficos.
  - `@st.cache_data` no `load_data()` para não reler o CSV (≈119 mil linhas) a cada interação.
- **Modificado:**
  - A correlação ficou indicada como Spearman no `# TODO`, e não Pearson, porque a EDA mostrou que nenhuma variável quantitativa é normal (Shapiro-Wilk rejeitou em todas).
  - Rótulos dos widgets em português, reaproveitando o dicionário `ROTULOS` da EDA, em vez dos nomes crus das colunas.
- **Rejeitado:**
  - Desenhar os gráficos (heatmap e histograma) já nesta etapa: pela proposta da Aula 21, eles só entram na próxima aula.
  - Fixar a barra de filtros no topo com CSS customizado: não é nativo do Streamlit e a sidebar já atende ao rascunho.
