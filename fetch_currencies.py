import requests
from datetime import datetime

# Replace this with your actual API key
API_KEY = 'ab5190cdeed8e868c081e4959da09e5e'

# API endpoint to fetch exchange rates (with the access key)
API_URL = f"http://api.exchangerate.host/live?access_key={API_KEY}&base=INR"

# Dictionary to map currency codes to their respective countries
CURRENCY_COUNTRY_MAP = {
    "AED": "United Arab Emirates",
    "AUD": "Australia",
    "CAD": "Canada",
    "CNY": "China",
    "EUR": "European Union",
    "GBP": "United Kingdom",
    "JPY": "Japan",
    "USD": "United States",
    # Add more currencies and countries as needed
}

def fetch_exchange_rates():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # This will raise an error for bad status codes (e.g., 404)

        # Print the raw API response for debugging
        print("API Response:", response.json())  # This will show the entire response structure

        data = response.json()

        if 'quotes' in data:  # Check if 'quotes' key exists in the response
            return data['quotes'], data['timestamp']
        else:
            raise ValueError("API response does not contain 'quotes' field.")
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"Request failed: {e}")
    except ValueError as e:
        raise SystemExit(f"Data error: {e}")
    except Exception as e:
        raise SystemExit(f"Unexpected error: {e}")

def update_readme(rates, timestamp):
    # Convert timestamp to human-readable format
    time_stamp_date = datetime.utcfromtimestamp(timestamp)
    formatted_date = time_stamp_date.strftime("%Y-%m-%d %H:%M:%S UTC")

    # Prepare README content
    readme_content = f"""# 🌏 Currency Exchange Rates (INR)

![Currency Tracker](https://img.shields.io/badge/Currency-Tracker-blue?style=flat-square)
![Update Schedule](https://img.shields.io/badge/Updates-Every%206%20hours-green?style=flat-square)

This repository **automatically updates** the exchange rates of various currencies with respect to **INR (Indian Rupee)** every 6 hours. The data is fetched from a reliable free API ([ExchangeRate API](https://exchangerate.host)) and displayed here in real time.

---

## 📅 Last Updated: **{formatted_date}**

| 🌍 **Currency** | 🏳️ **Country**           | 💰 **Exchange Rate**        |
|-----------------|--------------------------|-----------------------------|
"""
    for currency, rate in sorted(rates.items()):
        if rate != 0:  # Avoid division by zero
            country = CURRENCY_COUNTRY_MAP.get(currency[3:], "Unknown Country")  # Extract 3-letter currency code
            rate_in_inr = rate / 100  # Handle rates like USDINR, GBPINR
            readme_content += f"| {currency[3:]}             | {country}                 | 1 {currency[3:]} = {rate_in_inr:.2f} INR |\n"

    readme_content += """
---

## 🚀 How It Works
1. A **Python script** fetches the latest exchange rates using the [ExchangeRate API](https://exchangerate.host).
2. The script updates this `README.md` file with the latest rates.
3. **GitHub Actions** ensures the script runs **every 6 hours** and commits the changes back to the repository.

---

## 🌟 Features
- **Automated Updates**: No manual intervention needed.
- **Open Source**: Easily customizable for other currencies or base units.
- **Real-Time Data**: Updated every 6 hours with the latest rates.

---

### 📈 Example Use Cases
- Financial apps displaying live exchange rates.
- Currency conversion calculators.
- Data visualization for global markets.

---

### 🛠️ Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request to enhance this project.

---

### 📜 License
This project is licensed under the **MIT License**.
"""
    # Write to README.md
    with open("README.md", "w") as file:
        file.write(readme_content)

if __name__ == "__main__":
    try:
        rates, timestamp = fetch_exchange_rates()
        update_readme(rates, timestamp)
        print("README.md updated successfully!")
    except Exception as e:
        print(f"Error: {e}")
