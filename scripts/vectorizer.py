def vectorize(cleaned_X):
    from tensorflow import keras
    from keras.preprocessing.text import Tokenizer
    from keras.utils import pad_sequences

    # Limiting our tokenizers vocab size
    max_words = 10000
    
    # create the tokenizer
    tokenizer = Tokenizer(num_words=max_words)

    # Fit the tokenizer
    tokenizer.fit_on_texts(cleaned_X)

    # Create the sequences for each sentence, basically turning each word into its index position
    sequences = tokenizer.texts_to_sequences(cleaned_X)
    index_word = tokenizer.index_word

    # # Limiting our sequencer to only include 300 words
    max_length = 300

    # # Convert the sequences to all be the same length of 300
    cleaned_X = pad_sequences(sequences, maxlen=max_length, padding='post')

    return cleaned_X