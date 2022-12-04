def homes():
    import streamlit as st
    from streamlit_option_menu import option_menu 
    from scripts.cleaning_data import clean_data
    from scripts.vectorizer import vectorize
    from components.output import outputs
    import pickle
    from tensorflow import keras
    import tensorflow as tf

    loaded_model = keras.models.load_model('models/Valence_Regression/LSTM_Valence_model.h5')

    txt = st.text_area('Please input test:', placeholder="Placeholder", height=140)

    if(st.button('Submit')):
        cleaned_data = clean_data(txt)
        print(cleaned_data)
        vectorized_data = vectorize(cleaned_data)
        print(vectorized_data)

        prediction_valence = loaded_model.predict(vectorized_data)

        st.write('Return:', prediction_valence)
        outputs()
    else:
        st.write('Return:')