def homes():
    import streamlit as st
    from streamlit_option_menu import option_menu 
    from scripts.cleaning_data import clean_data
    from scripts.vectorizer import vectorize
    from components.output import outputs
    import pickle
    from tensorflow import keras
    import tensorflow as tf

    model = tf.saved_model.load('models/Valence_Regression/LSTM_Valence_model')
    
    txt = st.text_area('Please input test:', placeholder="Placeholder", height=140)

    if(st.button('Submit')):
        cleaned_data = clean_data(txt)
        vectorized_data = vectorize(cleaned_data)

        prediction_valence = model(vectorized_data)
        
        st.write('Return:', prediction_valence)
        
    else:
        st.write('Return:')