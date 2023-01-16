import streamlit as st
import numpy as np
import pandas as pd
import math
import joblib

st.title("PREDICT A CARD'S LEVEL")

st.header('Enter type of the card')
typec = st.selectbox('',("Normal Monster","Spell Card", "Effect Monster","Trap Card"))
st.write('You selected:', typec)
if typec in ("Spell Card") :
	st.subheader("Spell cards they have no level")
elif typec in ("Trap Card") :
	st.subheader("Trap cards they have no level")
else:

    # Add a atk input
    st.header('Attack Points of the card:')
    atk = st.number_input('')

    # Add a def input
    st.header('Defense Points of the card:', key = "def")
    defn = st.number_input('')


    # Display the entered name
    if st.button("Enviar"):

        level_model = joblib.load("level_model.pkl")

        X = pd.DataFrame([[typec,atk, defn ]],
            columns = ["type","atk", "def"])
        X = X.replace(["Normal Monster","Spell Card", "Effect Monster","Trap Card"], [0.,1.,2.,3.])


        prediction = level_model.predict(X)[0]

        st.text(f"Es un {round(prediction)}")
