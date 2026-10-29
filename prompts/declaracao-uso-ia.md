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

## Sessão de 29/10/2026

**Ferramenta:** Claude Code (modelo Claude Opus 5.5).

### Prompts usados

1. > esse repositorio ja tem commit?
2. > remove os arquivos .claude e .agents deixa so o prompts
3. > @prompts/prof_rascunho_dashboard1.png e @prompts/rascunho_dashboard1.png melhore esses dois rascunhos
4. > pode adicionar isso a parte de uso de declaração de IA, na verdade tudo que eu mandar aqui pode registrar lá e realizar o commit

### O que foi aceito, modificado ou rejeitado e por quê

- **Aceito:**
  - Conferência do histórico do Git: o repositório já tinha 6 commits e a `main` estava sincronizada com `origin/main`.
  - Remoção local das pastas `.claude/` e `.agents/`. Elas só continham symlinks para a skill `developing-with-streamlit` dentro do `.venv` e já estavam no `.gitignore`, então não houve mudança no repositório. Podem ser recriadas com `streamlit skills`.
  - Redesenho de `rascunho_dashboard1.png` (gerado com matplotlib) como um wireframe mais fiel ao `app.py`: sidebar com os widgets reais (pills das 5 variáveis, toggle Mantida / Cancelada e um slider de intervalo por variável), título e caption com a contagem de reservas filtradas, blocos de Correlação e Distribuição na proporção 1 : 1,5 de `st.columns([1, 1.5])`, um mini heatmap e um histograma esquemáticos, os avisos de validação e uma caixa tracejada reservando o espaço do Dashboard 2.
  - Marcação das três perguntas do dashboard no rascunho (P1 correlação, P2 distribuição por situação, P3 efeito dos extremos), ligando cada bloco à pergunta que responde.
  - Registro de todos os pedidos desta sessão nesta declaração, com commit ao final de cada um.
- **Modificado:**
  - `prof_rascunho_dashboard1.png` foi refeito sem alterar o conteúdo nem as proporções do rascunho do professor: só foram removidos os cantos pretos do recorte do slide, a resolução foi aumentada e entrou o título "Dashboard 1 — layout de referência". O original continua no histórico do Git.
  - Na primeira versão as pills da sidebar vazavam para fora da caixa e as etiquetas P1/P2/P3 ficaram grandes demais; os tamanhos foram corrigidos antes de salvar.
- **Rejeitado:**
  - Usar os dados reais nos gráficos do rascunho: o rascunho é planejamento de layout, e os gráficos de verdade só entram na próxima aula. O heatmap e o histograma desenhados são apenas ilustrativos.
