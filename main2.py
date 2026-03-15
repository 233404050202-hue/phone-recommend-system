from model.collaborative import recommend_item_based


# hàm cho Flask gọi
def recommend(user_id):

    results = recommend_item_based(user_id)

    # nếu không tìm thấy user
    if isinstance(results, str):
        return []

    output = []

    for phone, score in results.items():
        output.append((phone, round(score, 2)))

    return output


# code CLI cũ của bạn (giữ nguyên)
def main():

    print("Collaborative Filtering Recommendation System")
    print("---------------------------------------------")

    while True:

        user_input = input("\nEnter user id (or 'exit'): ")

        if user_input.lower() == "exit":
            break

        try:
            user_id = int(user_input)

            results = recommend_item_based(user_id)

            if isinstance(results, str):
                print(results)
                continue

            print("\nRecommended phones:\n")

            for phone, score in results.items():
                print(f"{phone:35} score: {score:.2f}")

        except ValueError:
            print("Invalid user id")


if __name__ == "__main__":
    main()