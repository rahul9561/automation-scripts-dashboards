import os
import sys

# Import scripts
from scripts.data_fetcher import fetch_data
from scripts.data_cleaner import clean_data
from scripts.email_sender import send_email

def main():
    # Paths
    raw_data = "data/amazon.csv"
    clean_data_path = "data/amazon_clean.csv"

    # 1. Fetch Data
    print("📥 Fetching data...")
    fetch_data(output_path=raw_data)

    # 2. Clean Data
    print("🧹 Cleaning data...")
    clean_data(input_path=raw_data, output_path=clean_data_path)

    # 3. Send Email
    print("📧 Sending email...")
    # ⚠️ Replace with ENV variables for security
    sender_email = os.getenv("SENDER_EMAIL", "add@gmail.com")
    sender_password = os.getenv("SENDER_PASSWORD", "app_password")
    receiver_email = os.getenv("RECEIVER_EMAIL", "rec@gmail.com")

    if not sender_email or not sender_password or not receiver_email:
        print("⚠️ Email credentials are missing. Please set environment variables:")
        print("   export SENDER_EMAIL='sender@gmail.com'")
        print("   export SENDER_PASSWORD='app_password'")
        print("   export RECEIVER_EMAIL='rec@gmail.com'")
        sys.exit(1)

    send_email(
        sender_email=sender_email,
        sender_password=sender_password,
        receiver_email=receiver_email,
        attachment_path=clean_data_path
    )

if __name__ == "__main__":
    main()
