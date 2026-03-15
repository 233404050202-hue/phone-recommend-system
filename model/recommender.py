import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# load data
products = pd.read_csv("data/products_phone.csv")
products["brand"] = products["brand"].fillna("")
products["ram"] = products["ram"].fillna("")
products["storage"] = products["storage"].fillna("")
# tạo feature text
products["features"] = (
    products["brand"].astype(str) + " " +
    products["ram"].astype(str) + " " +
    products["storage"].astype(str)
)

# TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(products["features"])

# similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)


def recommend(product_name, top_n=5):

    # tìm index của phone
    idx = products[
    products.apply(
        lambda row: product_name.lower() in str(row.values).lower(),
        axis=1
        )
    ]
    
    if idx.empty:
        return "Phone not found!"

    idx = idx.index[0]

    # similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))

    # sort
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # bỏ chính nó
    sim_scores = sim_scores[1:top_n+1]

    phone_indices = [i[0] for i in sim_scores]

    return products.iloc[phone_indices][["name", "brand", "ram", "storage"]]