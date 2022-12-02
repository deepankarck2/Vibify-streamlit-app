def homes():
    import streamlit as st
    from streamlit_option_menu import option_menu 
    from scripts.cleaning_data import clean_data

    txt = st.text_area('Please input test:', placeholder="Placeholder", height=140)

    if(st.button('Submit')):
        cleaned_data = clean_data(txt)
        st.write('Return:', cleaned_data)
    else:
        
        st.write('Return:')