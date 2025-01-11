import requests
from datetime import datetime

# API endpoint to fetch exchange rates
API_URL = "https://api.exchangerate.host/latest?base=INR"

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
    # We can add more currencies and countries as needed
}

def fetch_exchange_rates():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return data['rates'], data['date']
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def update_readme(rates, date):
    # Prepare README content
    readme_content = f"""# 🌏 Currency Exchange Rates (INR)

![Currency Tracker](https://img.shields.io/badge/Currency-Tracker-blue?style=flat-square)
![Update Schedule](https://img.shields.io/badge/Updates-Every%206%20hours-green?style=flat-square)

This repository **automatically updates** the exchange rates of various currencies with respect to **INR (Indian Rupee)** every 6 hours. The data is fetched from a reliable free API ([ExchangeRate API](https://exchangerate.host)) and displayed here in real time.

---

## 📅 Last Updated: **{date} (UTC)**

| 🌍 **Currency** | 🏳️ **Country**           | 💰 **Exchange Rate**        |
|-----------------|--------------------------|-----------------------------|
"""
    for currency, rate in sorted(rates.items()):
        if rate != 0:  # Avoid division by zero
            country = CURRENCY_COUNTRY_MAP.get(currency, "Unknown Country")
            rate_in_inr = 1 / rate
            readme_content += f"| {currency}             | {country}                 | 1 {currency} = {rate_in_inr:.2f} INR |\n"

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
        rates, date = fetch_exchange_rates()
        update_readme(rates, date)
        print("README.md updated successfully!")
    except Exception as e:
        print(f"Error: {e}")
