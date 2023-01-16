import streamlit as st
import numpy as np
import pandas as pd
import math
import joblib

st.title("Nivel de la carta")

# Add a atk input
atk = st.number_input("Enter atk:")

# Add a def input
defn = st.number_input("Enter defn:")


# Display the entered name
if st.button("Enviar"):

    level_model = joblib.load("level_model.pkl")

    X = pd.DataFrame([["atk", "def"]],
			   columns = ["atk", "def"])

    prediction = level_model.predict(float(X)[0])

    st.text(f"Es un {prediction}")
