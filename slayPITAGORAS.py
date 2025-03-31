
import streamlit as st
st.title("Kalkulator Pitagorasa (pokazcie Celince)")

a = st.number_input("Podaj długość boku a:")
b = st.number_input("Podaj długość boku c:")

#c is equal

c = (a**2 + b**2)**0.5

st.write()