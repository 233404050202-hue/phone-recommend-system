import pandas as pd
import numpy as np
import random

# đọc product dataset
products = pd.read_csv("data/products_phone.csv")

ratings = []

num_users = 200

for user_id in range(1, num_users + 1):

    # mỗi user đánh giá 30–35 sản phẩm
    num_ratings = random.randint(30, 35)

    sampled_products = products.sample(num_ratings)

    for _, row in sampled_products.iterrows():

        rating = np.clip(
            np.random.normal(loc=row["rating"], scale=0.5),
            1,
            5
        )

        rating = round(rating, 1)

        ratings.append({
            "user_id": user_id,
            "product_id": row["product_id"],
            "rating": rating
        })

ratings_df = pd.DataFrame(ratings)

# shuffle dataset
ratings_df = ratings_df.sample(frac=1).reset_index(drop=True)

ratings_df.to_csv("data/ratings_phone.csv", index=False)

print("Tạo ratings thành công!")
print("Tổng ratings:", len(ratings_df))
print("Users:", ratings_df["user_id"].nunique())
print("Products được đánh giá:", ratings_df["product_id"].nunique())