import pandas as pd

def fetch_data(output_path="data/amazon.csv"):
    # Simulated product data (replace with API/scraping logic later)
    data = [
        {
            "product_name": "Wireless Earbuds",
            "category": "Electronics",
            "rating": 4.5,
            "rating_count": 1200,
            "discount_percentage": 20,
            "img_link": "https://via.placeholder.com/150",
            "product_link": "https://amazon.com/earbuds"
        },
        {
            "product_name": "Smart Watch",
            "category": "Electronics",
            "rating": 4.2,
            "rating_count": 900,
            "discount_percentage": 15,
            "img_link": "https://via.placeholder.com/150",
            "product_link": "https://amazon.com/smartwatch"
        },
        {
            "product_name": "Running Shoes",
            "category": "Fashion",
            "rating": 4.7,
            "rating_count": 500,
            "discount_percentage": 30,
            "img_link": "https://via.placeholder.com/150",
            "product_link": "https://amazon.com/shoes"
        },
    ]

    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"✅ Data saved to {output_path}")

if __name__ == "__main__":
    fetch_data()
