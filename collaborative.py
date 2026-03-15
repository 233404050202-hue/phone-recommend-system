import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

ratings = pd.read_csv("data/ratings_phone.csv")
products = pd.read_csv("data/products_phone.csv")

# map id -> name
product_map = dict(zip(products["product_id"], products["name"]))

# user-item matrix
user_item = ratings.pivot_table(
    index="user_id",
    columns="product_id",
    values="rating"
).fillna(0)

# item-item similarity
item_similarity = cosine_similarity(user_item.T)

item_similarity_df = pd.DataFrame(
    item_similarity,
    index=user_item.columns,
    columns=user_item.columns
)

def recommend_item_based(user_id, top_n=5):

    if user_id not in user_item.index:
        return "User not found"

    user_ratings = user_item.loc[user_id]

    scores = {}

    for product_id, rating in user_ratings.items():

        if rating > 0:

            similar_items = item_similarity_df[product_id]

            for item, sim in similar_items.items():

                if user_ratings[item] == 0:

                    if item not in scores:
                        scores[item] = 0

                    scores[item] += sim * rating

    rec_series = pd.Series(scores).sort_values(ascending=False).head(top_n)

    rec_series.index = rec_series.index.map(lambda x: product_map.get(x, "Unknown"))

    return rec_series