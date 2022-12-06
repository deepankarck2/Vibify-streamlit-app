import streamlit as st 
from pages.home import homes
from streamlit_option_menu import option_menu 
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(initial_sidebar_state="collapsed")

selected = option_menu(None, ["Result", "Predict", "About Us"], 
icons=['cloud-upload', "bi-file-person"], 
menu_icon="cast", 
default_index=0, 
orientation="horizontal",
    styles={
    "container": {"padding": "1!important", "background-color": "#fafafa"},})



st.write("Valence Prediction is: ", st.session_state['prediction_valence'])
st.write("Genre Prediction is: ", st.session_state['prediction_genre'])

if selected == "Predict":
    switch_page("app")
   
