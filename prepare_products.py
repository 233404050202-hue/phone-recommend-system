import pandas as pd

# đọc dataset
df = pd.read_csv("data/Flipkart_Mobiles.csv")

# đặt lại tên cột
df.columns = [
    "brand",
    "model",
    "color",
    "ram",
    "storage",
    "rating",
    "price",
    "original_price"
]

# tạo tên sản phẩm
df["name"] = df["brand"] + " " + df["model"]

# xoá sản phẩm trùng
df = df.drop_duplicates(subset=["name","ram","storage"])

# reset index
df = df.reset_index(drop=True)

# tạo product_id
df["product_id"] = df.index + 1

# chọn cột
products = df[[
    "product_id",
    "name",
    "brand",
    "ram",
    "storage",
    "price",
    "rating"
]]

# lưu file
products.to_csv("data/products_phone.csv", index=False)

print(products.head())
print("Số sản phẩm:", len(products))