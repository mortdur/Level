import streamlit as st
import numpy as np
import pandas as pd
import math
import joblib

st.title("Nivel de la carta")

typec = st.selectbox('Enter type?',("Normal Monster","Spell Card", "Effect Monster","Trap Card"))
st.write('You selected:', typec)

# Add a atk input
atk = st.number_input("Enter atk:")

# Add a def input
defn = st.number_input("Enter defn:")


# Display the entered name
if st.button("Enviar"):

    level_model = joblib.load("level_model.pkl")

    X = pd.DataFrame([[typec,atk, defn ]],
			   columns = ["atk", "def","type"])
    X = X.replace(["Normal Monster","Spell Card", "Effect Monster","Trap Card"], [0.,1.,2.,3.])

    prediction = level_model.predict(X)[0]

    st.text(f"Es un {round(prediction)}")
