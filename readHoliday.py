import pandas as pd
import streamlit as st

df = pd.read_csv('feriadosNacionais.csv')  
st.title("Hello world!") 
st.write(df) 