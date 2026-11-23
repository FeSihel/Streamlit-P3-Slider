# Dia 8: st.slider
import streamlit as st
from datetime import time, datetime

st.header("st.slider")

age = st.slider("Quantos anos você tem?", 0, 120, 18) # Obs: o 3o número qual você quer que esteja indicado logo ao abrir.
# Se quiser deixar em decimal, basta colocar .0 nos números.
st.write("Eu tenho ", age, " anos")

shift = st.slider(
    "Qual seu horário de estudo/trabalho?", 
    value = (time(0, 0), time(23, 59)))
st.write("Seu horário compromissado é de:", shift)

year = st.slider(
    "Quando você vai aprender Streamlit?",
    value = datetime(2027, 1, 1, 0, 0), # Obs: a data escolhida estará como meio termo (mostra 15 dias antes e depois). Só é possível deslizar entre dias.
    format = "DD/MM/YY - HH:mm",
)
st.write("Vou aprender em:", year, ". Eu juro!")