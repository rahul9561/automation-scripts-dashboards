import pandas as pd

def clean_data(input_path="data/amazon.csv", output_path="data/amazon_clean.csv"):
    df = pd.read_csv(input_path)

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Handle missing values
    df.fillna({
        "rating": 0,
        "rating_count": 0,
        "discount_percentage": 0,
        "img_link": "https://via.placeholder.com/150",
        "product_link": "#"
    }, inplace=True)

    # Ensure rating is within [0,5]
    df["rating"] = df["rating"].clip(0, 5)

    df.to_csv(output_path, index=False)
    print(f"🧹 Cleaned data saved to {output_path}")

if __name__ == "__main__":
    clean_data()
