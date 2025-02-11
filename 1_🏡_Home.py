import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Home",
    page_icon="🏡",
    layout="wide"
)


if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"]>= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall",ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA 2023 OFFICIAL DATASET ⚽")
st.sidebar.markdown("Desenvolvido por [Asimov Academy](htpps://asimov.academy)")

bnt = st.link_button("Acesse os dados no Kaggle")
if bnt:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """Segue um texto genérico e direto sobre um conjunto de dados de jogadores do FIFA 2023:

---

Este conjunto de dados contém informações detalhadas sobre jogadores do FIFA 2023, abrangendo atributos essenciais para análise de desempenho no futebol virtual. Inclui características como nome, idade, nacionalidade, posição, time, e habilidades específicas como passe, drible, finalização e defesa. Também estão disponíveis dados sobre a classificação geral (overall) e o potencial máximo de cada jogador, além de valores de mercado e salários. Esse conjunto é ideal para análises estatísticas, criação de times otimizados, ou até para explorar padrões de habilidades e estilos de jogo em diferentes posições. É uma ferramenta poderosa para entusiastas de futebol e ciência de dados, oferecendo insights valiosos para entender o desempenho e a evolução dos atletas virtuais no game."""
)