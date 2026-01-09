import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def gerar_dados_marketing():
    np.random.seed(42)
    data_inicial = datetime(2025, 1, 1)
    registros = 1000
    
    canais = ['Google Ads', 'Meta Ads', 'LinkedIn Ads', 'E-mail Marketing', 'Orgânico']
    status_lead = ['Novo', 'Qualificado', 'Negociação', 'Fechado', 'Perdido']
    
    dados = {
        'Data': [data_inicial + timedelta(days=np.random.randint(0, 365)) for _ in range(registros)],
        'Canal_Origem': np.random.choice(canais, registros, p=[0.3, 0.3, 0.2, 0.1, 0.1]),
        'Lead_ID': range(1000, 1000 + registros),
        'Status': np.random.choice(status_lead, registros, p=[0.4, 0.2, 0.15, 0.1, 0.15]),
        'Investimento_Ads': np.random.uniform(10, 50, registros), # Custo por clique/lead
        'Valor_Contrato': [np.random.normal(5000, 1000) if s == 'Fechado' else 0 for s in np.random.choice(status_lead, registros)]
    }
    
    df = pd.DataFrame(dados)
    # Ajustando valor para quem não fechou ser zero
    df.loc[df['Status'] != 'Fechado', 'Valor_Contrato'] = 0
    
    df.to_csv("vendas_marketing.csv", index=False)
    print("✅ Base 'vendas_marketing.csv' gerada com sucesso!")

if __name__ == "__main__":
    gerar_dados_marketing()