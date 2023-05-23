import streamlit as st
import pandas as pd

st.title('Teste ECMI 2')

sr.write("Tabela")

dataframe = pd.DataFrame({
   'Nome': ['Julia', 'Bruna', 'Lavinia', 'Manu'],
   'Salário': [25000, 22500, 15000, 20000]
 })
 dataframe.style.hightlight_max(axis=0)
   
 st.write(dataframe)
