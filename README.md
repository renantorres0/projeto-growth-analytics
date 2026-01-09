# 📈 Growth Analytics Dashboard: Otimização de ROI e Funil

![Status do Projeto](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen)
![Versão](https://img.shields.io/badge/Vers%C3%A3o-2.0-blue)
![Python](https://img.shields.io/badge/Python-3.12%2B-blue)

Este projeto é um Dashboard de Performance de Marketing e Vendas desenvolvido para a **TechSolutions**. O objetivo é transformar dados brutos de CRM e Ads em insights acionáveis, focando na redução do Custo de Aquisição de Clientes (CAC) e no aumento do Retorno sobre Investimento (ROI).

Link para ter uma prévia do Dashboard antes de clonar o repositório: https://projeto-growth-analytics.streamlit.app/

---

## 🚀 Como Executar o Projeto

Para visualizar este projeto em sua máquina local, siga os passos abaixo:

### 1. Clonar o Repositório

```bash
git clone [https://github.com/renantorres0/projeto-growth-analytics.git](https://github.com/renantorres0/projeto-growth-analytics.git)
cd projeto-growth-analytics
```

### 2. Configurar o Ambiente Virtual

```bash
python -m venv .venv
# No Windows:
.venv\Scripts\activate
# No Mac/Linux:
source .venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Gerar Base de Dados e Rodar o App

Como os dados são proprietários, este repositório inclui um script para gerar uma base sintética realista:

```bash
python gerar_dados_marketing.py
streamlit run app.py
```

## 📊 Funcionalidades e Análises

O dashboard oferece uma visão 360º da jornada de crescimento:

**- KPIs de Negócio:**
    Monitoramento em tempo real de Leads, Conversão, Vendas, Receita Total e Ticket Médio.

**- Funil de Vendas Reativo:**
    Visualização das etapas (Novo -> Qualificado -> Negociação -> Fechado) com taxas de quebra entre fases.

**- Evolução Mensal:**
    Gráfico de tendência temporal para identificar sazonalidade e crescimento do volume de entrada.

**- Performance por Canal (ROI/CAC):**
    Comparação direta entre Google Ads, Meta Ads, LinkedIn e Orgânico para identificar onde o capital é mais eficiente.

**- Exportação de Relatórios:**
    Ferramenta integrada para baixar a tabela de eficiência filtrada em formato CSV para apresentações executivas.

## 🛠️ Tecnologias Utilizadas

**Python 3.12:** Linguagem base para processamento de dados.

**Streamlit (v2.0+):** Framework para criação da interface web interativa.

**Pandas:** Manipulação, limpeza e agregação de dados.

**Plotly Express & Graph Objects:** Criação de gráficos dinâmicos e funis estratégicos.

## 📧 Contato
Desenvolvido por Renan Torres.

**LinkedIn:** https://www.linkedin.com/in/renan-torres-121a06106/

**Portfólio:** https://share.streamlit.io/
