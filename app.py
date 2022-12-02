import streamlit as st
from streamlit_option_menu import option_menu 
from components.home import homes
from components.output import outputs

selected = option_menu(None, ["Home", "App", "About Us"], 
    icons=['house', 'cloud-upload', "bi-file-person"], 
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
     styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},

    }
    )
	
if selected == "Home":
    homes()
if selected == "App":
    outputs()
        
# to run: streamlit run app.py
