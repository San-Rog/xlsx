import pandas as pd
import streamlit as st
from datetime import date

def changeValue(value):
    try:
        return (value.strftime("%d/%m/%Y"))
    except:
        return ""

df = pd.read_csv('feriadosNacionais.csv')
df["Data"] = df["Data"].apply(changeValue)
st.title("Hello world!") 
st.write(df) 
