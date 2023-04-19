#%%
import streamlit as st
import random

st.header("TDS Week 8: Largest Among 3")
st.write("#### Enter 3 numbers")
st.write("Submitted by: Anirudh Murthy (21f1000931)")
st.write("PS: A random number between $$1$$ and $$100$$ is generated for each number by default")
st.write("---")
a = st.number_input("Enter 1st number", value=random.randint(1,100))
b = st.number_input("Enter 2nd number", value=random.randint(1,100))
c = st.number_input("Enter 3rd number", value=random.randint(1,100))

calc = st.button("Find Largest")
if calc:
    lg = max(a, b, c)
    st.header(f"Largest number is: {lg}")
# %%
# %%
