import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Configuração da Página
st.set_page_config(page_title="Growth Analytics 2026", layout="wide")

# 2. Carga de Dados
@st.cache_data
def load_data():
    try:
        dados = pd.read_csv("vendas_marketing.csv")
        dados['Data'] = pd.to_datetime(dados['Data'])
        return dados
    except FileNotFoundError:
        return None

df_raw = load_data()

# 3. Sidebar com Filtros Reativos
if df_raw is not None:
    with st.sidebar:
        st.header("🎯 Filtros de Performance")
        
        # Filtro de Data
        min_date = df_raw['Data'].min().date()
        max_date = df_raw['Data'].max().date()
        data_sel = st.date_input("Período", value=(min_date, max_date))
        
        # Filtro de Canal
        canais = df_raw['Canal_Origem'].unique().tolist()
        canais_sel = st.multiselect("Canais", options=canais, default=canais)

    # Aplicação dos Filtros (Criando o df_filtrado)
    if len(data_sel) == 2:
        mask = (df_raw['Data'].dt.date >= data_sel[0]) & \
               (df_raw['Data'].dt.date <= data_sel[1]) & \
               (df_raw['Canal_Origem'].isin(canais_sel))
        df = df_raw.loc[mask]
    else:
        df = df_raw

    # 4. Título e KPIs
    st.title("📈 Dashboard de Growth & Performance")
    
    # Cálculos das Métricas
    total_leads = len(df)
    vendas = len(df[df['Status'] == 'Fechado'])
    taxa_conv = (vendas / total_leads * 100) if total_leads > 0 else 0
    receita_total = df['Valor_Contrato'].sum()
    ticket_medio = receita_total / vendas if vendas > 0 else 0

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Total Leads", total_leads)
    c2.metric("Conversão", f"{taxa_conv:.1f}%")
    c3.metric("Vendas", vendas)
    c4.metric("Receita", f"R$ {receita_total:,.0f}")
    c5.metric("Ticket Médio", f"R$ {ticket_medio:,.0f}")

    st.markdown("---")

    # 5. Gráficos Principais
    col_esq, col_dir = st.columns(2)

    with col_esq:
        st.subheader("Funil de Vendas")
        status_ordem = ['Novo', 'Qualificado', 'Negociação', 'Fechado']
        contagem = [len(df[df['Status'] == s]) for s in status_ordem]
        fig_funnel = go.Figure(go.Funnel(y=status_ordem, x=contagem, textinfo="value+percent initial"))
        st.plotly_chart(fig_funnel, width='stretch')

    with col_dir:
        st.subheader("Evolução Mensal")
        df_time = df.set_index('Data').resample('ME')['Lead_ID'].count().reset_index()
        fig_time = px.line(df_time, x='Data', y='Lead_ID', markers=True, color_discrete_sequence=['#2E8B57'])
        st.plotly_chart(fig_time, width='stretch')

    st.markdown("---")

    # 6. Análise de ROI e Distribuição
    col_inf1, col_inf2 = st.columns(2)

    with col_inf1:
        st.subheader("ROI por Canal")
        df_roi = df.groupby('Canal_Origem').agg({'Investimento_Ads':'sum', 'Valor_Contrato':'sum'}).reset_index()
        df_roi['ROI'] = (df_roi['Valor_Contrato'] / df_roi['Investimento_Ads']).round(2)
        fig_roi = px.bar(df_roi, x='Canal_Origem', y='ROI', color='ROI', color_continuous_scale='Blues')
        st.plotly_chart(fig_roi, width='stretch')

    with col_inf2:
        st.subheader("Distribuição de Status")
        fig_pie = px.pie(df, names='Status', hole=0.4)
        st.plotly_chart(fig_pie, width='stretch')

    # 7. Tabela de Detalhamento
    st.markdown("---")
    st.subheader("📊 Detalhamento de Eficiência")
    df_tab = df.groupby('Canal_Origem').agg({'Lead_ID':'count', 'Investimento_Ads':'sum', 'Valor_Contrato':'sum'}).reset_index()
    df_tab['CAC'] = df_tab['Investimento_Ads'] / df_tab['Lead_ID']
    df_tab.columns = ['Canal', 'Leads', 'Investimento', 'Receita', 'CAC']
    
    st.dataframe(df_tab.style.format({'Investimento': 'R$ {:,.2f}', 'Receita': 'R$ {:,.2f}', 'CAC': 'R$ {:,.2f}'}), 
                 width='stretch', hide_index=True)
    
    # --- BOTÃO DE EXPORTAÇÃO ---
    st.markdown("### 📥 Exportar Resultados")
    
    # Transformando o dataframe filtrado em CSV
    csv = df_tab.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="Baixar Relatório de Eficiência (CSV)",
        data=csv,
        file_name='relatorio_performance_growth.csv',
        mime='text/csv',
    )
else:
    st.error("Rode o script de geração de dados primeiro!")