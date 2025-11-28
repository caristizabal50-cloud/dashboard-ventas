import streamlit as st
import pandas as pd

df = pd.read_csv("ventas.csv")

st.title("Dashboard de Ventas")

st.metric("Ingreso Total", df["Ingreso"].sum())
st.metric("Promedio de Ingreso", df["Ingreso"].mean())

st.bar_chart(df["Ingreso"])