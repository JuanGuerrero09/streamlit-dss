import streamlit as st

st.title("Mini dashboard")

q = st.slider("Selected flow", 0, 100, 4)

st.write(f"Current flow: {q} L/s")
st.bar_chart({"flow": [q]})
