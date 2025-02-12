import streamlit as st
import joblib
import pandas as pd
from prophet.plot import plot_plotly

st.set_page_config(page_title="Tech Challenge - Previsão do Preço do Petróleo", 
                   page_icon="⛽", 
                   layout="wide")

opcoes_abas = ['Explicação Tech Challenge 4', 'Modelo ML','Relatório Power BI']
aba_selecionada = st.sidebar.selectbox('Escolha uma aba', opcoes_abas)

if aba_selecionada == 'Modelo ML':

    st.title("Previsão do Preço do Petróleo Brent")
    st.write('#### Selecione quantos dias deseja prever')
    
    # Carregar o modelo Prophet
    model = joblib.load('modelo_prophet.pkl')

    

        # Entrada do usuário para a previsão
    days = st.number_input("Quantos dias para previsão?", min_value=1, max_value=365, value=90)

    # Gerar datas futuras e adicionar os regressores 'ano', 'mes', 'dia' e 'dia_semana'
    future_dates = model.make_future_dataframe(periods=days)
    future_dates['ano'] = future_dates['ds'].dt.year
    future_dates['mes'] = future_dates['ds'].dt.month
    future_dates['dia'] = future_dates['ds'].dt.day
    future_dates['dia_semana'] = future_dates['ds'].dt.weekday

    # Prever com o modelo
    forecast = model.predict(future_dates)

    # Renomear colunas para exibição
    forecast_display = forecast.rename(columns={'ds': 'Data', 'yhat': 'Preço'})

    # Converter a coluna "Data" para o formato de data
    forecast_display['Data'] = forecast_display['Data'].dt.date

    # Plotar o gráfico com Plotly
    st.write("Previsão do preço em USD para os próximos {} dias:".format(days))
    st.write(forecast_display[['Data', 'Preço']].tail(days))

    # Plotar o gráfico com Plotly
    plot = plot_plotly(model, forecast)
    st.plotly_chart(plot)


elif aba_selecionada == 'Relatório Power BI':

    # URLs dos relatórios do Power BI
    embed_urls = ['https://app.powerbi.com/view?r=eyJrIjoiZGQ3NjE0YTctZTBiNS00YTA3LWJjY2MtYzUxNGQwNjc0MmFjIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9']

    # Exibir os relatórios em um IFRAME e ajustar a posição
    for url in embed_urls:
        st.markdown(f"""
            <center>
                <iframe title="Dashboard_Petroleo_v3" width="1100" height="650" src="{url}" frameborder="0" allowFullScreen="true"></iframe>
            </center>
            """, unsafe_allow_html=True)

elif aba_selecionada == "Explicação Tech Challenge 4":

  #CSS para estilizar a capa
  st.markdown("""
    <style>
        .main {
            background-image: url('https://clickpetroleo.com.br/wp-content/uploads/2024/11/DALL%C2%B7E-2024-11-04-12.31.19-Create-a-vibrant-image-of-a-deep-sea-offshore-oil-rig-with-a-modern-FPSO-vessel-operating-nearby.-The-setting-is-a-calm-clear-ocean-under-a-bright-bl.webp');
            background-size: cover;
            background-position: center;
            height: 100vh;
        }
        .title {
            font-size: 48px;
            font-weight: bold;
            color: black;
            text-shadow: 2px 2px 4px #000000;
            text-align: center;
        }
        .subtitle {
            font-size: 24px;
            color: black;
            text-shadow: 1px 1px 2px #000000;
            text-align: center;
        }
    </style>
  """, unsafe_allow_html=True)


  st.markdown('<div class="title">Tech Challenge - Fase 4</div>', unsafe_allow_html=True)
  # Layout da capa
  st.markdown('<div class="subtitle">- Data Analytics - FIAP</div>', unsafe_allow_html=True)
  st.markdown('<div class="main">', unsafe_allow_html=True)
  st.markdown('<div class="subtitle">- Dashboard Interativo e Previsão de Preços do Petróleo</div>', unsafe_allow_html=True)
  st.markdown('<div class="text">- O dashboard interativo foi desenvolvido para permitir uma análise detalhada da variação dos preços do petróleo Brent ao longo do tempo. A solução oferece uma visão clara das tendências históricas e permite explorar fatores que impactam diretamente os preços, como crises econômicas, eventos geopolíticos e variações na demanda global por energia. Através de gráficos dinâmicos e filtros personalizados, os usuários podem utilizar informações analíticas para tomada de decisões estratégicas baseadas em dados concretos.</div>', unsafe_allow_html=True)
  st.markdown('<div class="subtitle">- Analisando dados históricos e tendências do mercado</div>', unsafe_allow_html=True)
  st.markdown('<div class="text">- Para realizar a previsão do preço do petróleo Brent, foi desenvolvido um modelo de Machine Learning baseado em séries temporais. A análise considerou as variações dos dados históricos, considerando fatores externos que podem influenciar as oscilações de preço. Diversas abordagens foram testadas para garantir maior precisão nas previsões, incluindo algoritmos como ARIMA, SARIMA, SARIMAX e Prophet. A performance do modelo foi avaliada por métricas como MAE, MSE e MAPE garantindo previsões confiáveis. O modelo foi então integrado ao Streamlit, permitindo que os usuários visualizem as projeções futuras e utilizem essas informações para embasar suas decisões estratégicas.</div>', unsafe_allow_html=True)
  st.markdown('</div>', unsafe_allow_html=True)

  # Rodapé
  st.markdown("### ⛽ Projeto desenvolvido para análise e previsão de preços do petróleo Brent")
  st.markdown("""
      <div style="position: fixed; bottom: 0; width: 100%; background-color: black; padding: 10px; text-align: center;">
          <a href="https://github.com/Mauro010BR/Tech-Challenge-Fase-4" target="_blank" style="text-decoration: none; color: white; font-size: 18px;">
              <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="25px" style="vertical-align: middle; margin-right: 5px;">
              Acesse o repositório no GitHub
          </a>
      </div>
  """, unsafe_allow_html=True)