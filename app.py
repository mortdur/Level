import streamlit as st
import numpy as np
import pandas as pd
import math
import joblib

st.title("PREDICT A CARD'S LEVEL")

typec = st.selectbox('Enter type of the card',("Normal Monster","Spell Card", "Effect Monster","Trap Card"))
st.write('You selected:', typec)
if typec in ("Spell Card") :
	st.header("Spell cards they have no level")
elif typec in ("Trap Card") :
	st.header("Trap cards they have no level")
else:

    # Add a atk input
    atk = st.number_input('Attack Points of the card:')

    # Add a def input
    defn = st.number_input("Enter Defense Points of the card:")


    # Display the entered name
    if st.button("Enviar"):

        level_model = joblib.load("level_model.pkl")

        X = pd.DataFrame([[typec,atk, defn ]],
            columns = ["type","atk", "def"])
        X = X.replace(["Normal Monster","Spell Card", "Effect Monster","Trap Card"], [0.,1.,2.,3.])


        prediction = level_model.predict(X)[0]

        st.text(f"Es un {round(prediction)}")
