import streamlit as st
import numpy as np
import pandas as pd
import math
import joblib

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("background-color: #e5e5f7;
opacity: 0.6;
background: linear-gradient(135deg, #444cf755 25%, transparent 25%) -20px 0/ 40px 40px, linear-gradient(225deg, #444cf7 25%, transparent 25%) -20px 0/ 40px 40px, linear-gradient(315deg, #444cf755 25%, transparent 25%) 0px 0/ 40px 40px, linear-gradient(45deg, #444cf7 25%, #e5e5f7 25%) 0px 0/ 40px 40px;");
background-size: cover;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st.image("logo.png", width=450)
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
    atk = st.slider("ATK:",0.0, 5000.0,step=100.0)

    # Add a def input
    st.header("Defense Points of the card:")
    defn = st.slider("DEF:",0.0, 5000.0,step=100.0,key="def")

    # Display the entered name
    if st.button("Enviar"):

        level_model = joblib.load("level_model.pkl")

        X = pd.DataFrame([[typec,atk, defn ]],
            columns = ["type","atk", "def"])
        X = X.replace(["Normal Monster","Spell Card", "Effect Monster","Trap Card"], [0.,1.,2.,3.])


        prediction = level_model.predict(X)[0]

        st.subheader(f"The most appropriate level for this card is {round(prediction)}")
