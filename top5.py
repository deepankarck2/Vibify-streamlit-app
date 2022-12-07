def get_results(df, results, cleaned_X):
    import pandas as pd
    import re

    output_list = []

    for i in results.argsort()[:-6:-1]:
        if results[i] > 0:
            res_string = str("{} with {}% match".format(
                df.loc[i].song_by_artist, round(100*results[i])))
            output_list.append(res_string)
    return output_list


def top5_func(cleaned_X):

    import numpy as np
    import pandas as pd
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer
    from sklearn.metrics.pairwise import cosine_similarity
    from scipy import sparse
    from cleaning_data import clean_data
    # import re

    df = pd.read_csv('data/preprocessed_dataset.csv')
    df.dropna(inplace=True)
    cv = CountVectorizer()

    doc_term_matrix = cv.fit_transform(
        df['clean_lyrics'])  # type is csr_matrix
    idfs = TfidfTransformer()
    idfs.fit(doc_term_matrix)
    idfs_df = pd.DataFrame(
        idfs.idf_, index=cv.get_feature_names(), columns=["idfs"])
    tf_idfs = idfs.transform(doc_term_matrix)

    # tf_idfs_top5 = sparse.load_npz("data/tf_idfs_top5.npz") # DOESNT WORK WITH THIS
    query_term_matrix = cv.transform([cleaned_X])

    results = cosine_similarity(tf_idfs, query_term_matrix)
    results = results.reshape((-1,))

    print("Search results for input: \n ")
    print("{}".format(cleaned_X))
    print("\nTop 5 most similar songs based on lyrics are: \n")

    output_list = get_results(df, results, cleaned_X)
    return output_list

    # OPTIMIZE: Need to figure out how to load the tfidf file
    # I need to compare tf_idfs (saved matrix) with query_term_matrix (user input that has been cv.transformed)
    # for use in: results = cosine_similarity(tf_idfs, query_term_matrix)

    # does not work:
    # tf_idfs_top5 = sparse.load_npz("data/tf_idfs_top5.npz")
    # query_term_matrix = cv.transform([cleaned_X])
