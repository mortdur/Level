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

[data-testid="stMarkdownContainer"] {
color : rgb(0, 0, 0);
font-size: 40px;
}

[data-testid="stVerticalBlock"] {
background: rgba(138, 156, 253, 0.15);
border-radius: 15px 50px;
padding: 0px 16px;
}

p {
margin: 0px 0px 1rem;
padding: 0px;
font-size: 20px;
font-weight: 400;
text-shadow: 1px 1px 1px #ff00001f, 2px 2px 1px #ff00002e;
}

.st-bs {
color : rgb(189, 0, 0);
text-shadow: 1px 1px 1px #0000002e, 2px 2px 1px #0000002b
}

[data-testid="stToolbar"] {
right: 2rem;
}

[data-testid="stThumbValue"] {
font-size: 15px;
text-shadow: 1px 1px 1px #ff00001f, 2px 2px 1px #ff00002e;
}

[data-testid="stTickBarMin"] {
font-size: 15px;
text-shadow: 1px 1px 1px #0000002e, 2px 2px 1px #0000002b
}

[data-testid="stImage"] {
width: 95%;
height: auto;
}

.css-17z41qg p {
font-size: 15px;
}

h2 {
color : rgb(255, 186, 113);
text-shadow: 1px 1px 1px #0000002e, 2px 2px 1px #0000002b;
}

h1 {
color : rgb(255, 83, 83);
text-shadow: 1px 1px 1px #ff00001f, 2px 2px 1px #ff00002e;
}

span {
text-shadow: 1px 1px 1px #0000006b, 2px 2px 1px #0000002e;
}
</style>
"""

with st.container():
  st.markdown(page_bg_img, unsafe_allow_html=True)
  st.image("logo.png")
  st.title("PREDICT A CARD'S LEVEL")
  st.header('Enter type of the card')
  typec = st.selectbox(' ',("Normal Monster","Spell Card", "Effect Monster","Trap Card"))
  st.write('You selected:', typec)
  if typec in ("Spell Card") :
    st.subheader("Spell cards have no level")
  elif typec in ("Trap Card") :
    st.subheader("Trap cards have no level")
  else:
      # Add a atk input
      st.header('Attack Points of the card:')
      atk = st.slider("ATK:",0.0, 5000.0,step=100.0,key="atk")

      # Add a def input
      st.header("Defense Points of the card:")
      defn = st.slider("DEF:",0.0, 5000.0,step=100.0,key="def")

      # Display the entered name
      if st.button("Enviar") :
        level_model = joblib.load("level_model.pkl")
        X = pd.DataFrame([[typec,atk, defn ]],
          columns = ["type","atk", "def"])
        X = X.replace(["Normal Monster","Spell Card", "Effect Monster","Trap Card"], [0.,1.,2.,3.])
        prediction = level_model.predict(X)[0]
        st.subheader(f"The most appropriate level for this card is {round(prediction)}")
