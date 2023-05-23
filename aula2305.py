import streamlit as st
import pandas as pd
import numpy as np

st.title('Teste ECMI 2')

st.write("Tabela")

dataframe = pd.DataFrame({
   'Nome': ['Julia', 'Bruna', 'Lavinia', 'Manu'],
   'Salário': [25000, 22500, 15000, 20000]
 })
 dataframe.style.hightlight_max(axis=0)
   
 st.write(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a','b','c'])

st.line_chart(chart_data)
