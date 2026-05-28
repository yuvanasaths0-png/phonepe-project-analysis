
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("aggregated_transaction.csv")

st.title("PhonePe Transaction Dashboard")

st.subheader("Top 10 States by Transaction Amount")

top_states = df.groupby("State")["Amount"].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots()

top_states.plot(kind="bar", ax=ax)

plt.xticks(rotation=45)

st.pyplot(fig)
