import streamlit as st
from streamlit_option_menu import option_menu 

selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
	
selected2
txt = st.text_area('Please input test:', placeholder="Placeholder", height=140)

if(st.button('Submit')):
	st.write('Return:', txt)
else:
	st.write('Return:')
	
# to run: streamlit run app.py
