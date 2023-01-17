import streamlit as st
import numpy as np
import pandas as pd
import math
import joblib

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://mktg-assets.tcgplayer.com/content/opengraph/How%20To%20Build%20The%20Kuribabylon%20Combo%20Deck.jpg");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}
[data-testid="st-br"] {
textColor = "#000000";
}

[data-testid="stToolbar"] {
right: 2rem;
}
</style>
"""

with st.container():
  st.markdown(page_bg_img, unsafe_allow_html=True)
  st.image("logo.png", width=450)
  st.title("PREDICT A CARD'S LEVEL",key="levelapp")
  st.header('Enter type of the card',key="tipo")
  typec = st.selectbox('',("Normal Monster","Spell Card", "Effect Monster","Trap Card"),key="select")
  st.write('You selected:', typec,key="selected")
  if typec in ("Spell Card") :
    st.subheader("Spell cards they have no level",key="spell")
  elif typec in ("Trap Card") :
    st.subheader("Trap cards they have no level",key="trap")
  else:
      # Add a atk input
      st.header('Attack Points of the card:',key="atkp")
      atk = st.slider("ATK:",0.0, 5000.0,step=100.0,key="atk")

      # Add a def input
      st.header("Defense Points of the card:",key="defp")
      defn = st.slider("DEF:",0.0, 5000.0,step=100.0,key="def")

      # Display the entered name
      if st.button("Enviar"):  st.markdown(page_bg_img, unsafe_allow_html=True)
        level_model = joblib.load("level_model.pkl")
        X = pd.DataFrame([[typec,atk, defn ]],
            columns = ["type","atk", "def"])
        X = X.replace(["Normal Monster","Spell Card", "Effect Monster","Trap Card"], [0.,1.,2.,3.])
        prediction = level_model.predict(X)[0]
        st.subheader(f"The most appropriate level for this card is {round(prediction)}")
