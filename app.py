import streamlit as st

txt = st.text_area('Please input test:', placeholder="Placeholder", height=140)

if(st.button('Submit')):
	st.write('Return:', txt)
else:
	st.write('Return:')