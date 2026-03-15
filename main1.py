from model.recommender import recommend


def main():

    print("📱 Phone Recommendation System")
    print("--------------------------------")

    while True:

        product_name = input("\nEnter phone name (or 'exit'): ")

        if product_name.lower() == "exit":
            print("Goodbye!")
            break

        results = recommend(product_name)

        if isinstance(results, str):
            print(results)
        else:
            print("\nRecommended phones:\n")

            print(f"{'name':<25} {'brand':<10} {'ram':<6} {'storage':<8}")
            print("-"*55)

            for _, row in results.iterrows():
                print(f"{row['name']:<25} {row['brand']:<10} {row['ram']:<6} {row['storage']:<8}")


if __name__ == "__main__":
    main()