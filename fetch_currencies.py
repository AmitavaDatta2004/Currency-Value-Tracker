# fetch_currencies.py
import requests
from datetime import datetime, timezone

# Replace this with your actual API key
API_KEY = 'ab5190cdeed8e868c081e4959da09e5e'

# API endpoint to fetch exchange rates (with the access key)
API_URL = f"http://api.exchangerate.host/live?access_key={API_KEY}&base=INR"

# Dictionary to map currency codes to their respective countries
CURRENCY_COUNTRY_MAP = {
    "AED": "United Arab Emirates",
    "AFN": "Afghanistan",
    "ALL": "Albania",
    "AMD": "Armenia",
    "ANG": "Netherlands Antilles",
    "AOA": "Angola",
    "ARS": "Argentina",
    "AUD": "Australia",
    "AWG": "Aruba",
    "AZN": "Azerbaijan",
    "BAM": "Bosnia and Herzegovina",
    "BBD": "Barbados",
    "BDT": "Bangladesh",
    "BGN": "Bulgaria",
    "BHD": "Bahrain",
    "BIF": "Burundi",
    "BMD": "Bermuda",
    "BND": "Brunei",
    "BOB": "Bolivia",
    "BRL": "Brazil",
    "BSD": "Bahamas",
    "BTC": "Bitcoin",
    "BTN": "Bhutan",
    "BWP": "Botswana",
    "BYN": "Belarus",
    "BYR": "Belarus (Old Currency)",
    "BZD": "Belize",
    "CAD": "Canada",
    "CDF": "Democratic Republic of the Congo",
    "CHF": "Switzerland",
    "CLF": "Chile",
    "CLP": "Chile",
    "CNH": "China (Offshore Yuan)",
    "CNY": "China",
    "COP": "Colombia",
    "CRC": "Costa Rica",
    "CUC": "Cuba (Convertible Peso)",
    "CUP": "Cuba",
    "CVE": "Cape Verde",
    "CZK": "Czech Republic",
    "DJF": "Djibouti",
    "DKK": "Denmark",
    "DOP": "Dominican Republic",
    "DZD": "Algeria",
    "EGP": "Egypt",
    "ERN": "Eritrea",
    "ETB": "Ethiopia",
    "EUR": "European Union",
    "FJD": "Fiji",
    "FKP": "Falkland Islands",
    "GBP": "United Kingdom",
    "GEL": "Georgia",
    "GGP": "Guernsey",
    "GHS": "Ghana",
    "GIP": "Gibraltar",
    "GMD": "Gambia",
    "GNF": "Guinea",
    "GTQ": "Guatemala",
    "GYD": "Guyana",
    "HKD": "Hong Kong",
    "HNL": "Honduras",
    "HRK": "Croatia",
    "HTG": "Haiti",
    "HUF": "Hungary",
    "IDR": "Indonesia",
    "ILS": "Israel",
    "IMP": "Isle of Man",
    "INR": "India",
    "IQD": "Iraq",
    "IRR": "Iran",
    "ISK": "Iceland",
    "JEP": "Jersey",
    "JMD": "Jamaica",
    "JOD": "Jordan",
    "JPY": "Japan",
    "KES": "Kenya",
    "KGS": "Kyrgyzstan",
    "KHR": "Cambodia",
    "KMF": "Comoros",
    "KPW": "North Korea",
    "KRW": "South Korea",
    "KWD": "Kuwait",
    "KYD": "Cayman Islands",
    "KZT": "Kazakhstan",
    "LAK": "Laos",
    "LBP": "Lebanon",
    "LKR": "Sri Lanka",
    "LRD": "Liberia",
    "LSL": "Lesotho",
    "LTL": "Lithuania",
    "LVL": "Latvia",
    "LYD": "Libya",
    "MAD": "Morocco",
    "MDL": "Moldova",
    "MGA": "Madagascar",
    "MKD": "North Macedonia",
    "MMK": "Myanmar (Burma)",
    "MNT": "Mongolia",
    "MOP": "Macau",
    "MRU": "Mauritania",
    "MUR": "Mauritius",
    "MVR": "Maldives",
    "MWK": "Malawi",
    "MXN": "Mexico",
    "MYR": "Malaysia",
    "MZN": "Mozambique",
    "NAD": "Namibia",
    "NGN": "Nigeria",
    "NIO": "Nicaragua",
    "NOK": "Norway",
    "NPR": "Nepal",
    "NZD": "New Zealand",
    "OMR": "Oman",
    "PAB": "Panama",
    "PEN": "Peru",
    "PGK": "Papua New Guinea",
    "PHP": "Philippines",
    "PKR": "Pakistan",
    "PLN": "Poland",
    "PYG": "Paraguay",
    "QAR": "Qatar",
    "RON": "Romania",
    "RSD": "Serbia",
    "RUB": "Russia",
    "RWF": "Rwanda",
    "SAR": "Saudi Arabia",
    "SBD": "Solomon Islands",
    "SCR": "Seychelles",
    "SDG": "Sudan",
    "SEK": "Sweden",
    "SGD": "Singapore",
    "SHP": "Saint Helena",
    "SLE": "Sierra Leone",
    "SLL": "Sierra Leone (Old Currency)",
    "SOS": "Somalia",
    "SRD": "Suriname",
    "STD": "São Tomé and Príncipe",
    "SVC": "El Salvador",
    "SYP": "Syria",
    "SZL": "Swaziland",
    "THB": "Thailand",
    "TJS": "Tajikistan",
    "TMT": "Turkmenistan",
    "TND": "Tunisia",
    "TOP": "Tonga",
    "TRY": "Turkey",
    "TTD": "Trinidad and Tobago",
    "TWD": "Taiwan",
    "TZS": "Tanzania",
    "UAH": "Ukraine",
    "UGX": "Uganda",
    "USD": "United States",
    "UYU": "Uruguay",
    "UZS": "Uzbekistan",
    "VEF": "Venezuela",
    "VND": "Vietnam",
    "VUV": "Vanuatu",
    "WST": "Samoa",
    "XOF": "West African CFA Franc (XOF)",
    "XPF": "CFP Franc",
    "YER": "Yemen",
    "ZAR": "South Africa",
    "ZMK": "Zambia (Old Currency)",
    "ZMW": "Zambia",
    "ZWL": "Zimbabwe",
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
    # Convert timestamp to human-readable format using timezone-aware datetime
    time_stamp_date = datetime.fromtimestamp(timestamp, timezone.utc)
    formatted_date = time_stamp_date.strftime("%Y-%m-%d %H:%M:%S UTC")

    # Prepare README content
    readme_content = f"""# 🌏 Currency Exchange Rates (INR)

![Currency Tracker](https://img.shields.io/badge/Currency-Tracker-blue?style=flat-square)
![Update Schedule](https://img.shields.io/badge/Updates-Every%208%20hours-green?style=flat-square)

This repository **automatically updates** the exchange rates of various currencies with respect to **INR (Indian Rupee)** every 8 hours. The data is fetched from a reliable free API ([ExchangeRate API](https://exchangerate.host)) and displayed here in real time.

---

## 📅 Last Updated: **{formatted_date}**

| 🌍 **Currency** | 🏳️ **Country**           | 💰 **Exchange Rate**        |
|-----------------|--------------------------|-----------------------------|"""
    
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
3. **GitHub Actions** ensures the script runs **every 8 hours** and commits the changes back to the repository.

---

## 🌟 Features
- **Automated Updates**: No manual intervention needed.
- **Open Source**: Easily customizable for other currencies or base units.
- **Real-Time Data**: Updated every 8 hours with the latest rates.

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
    # Write to README.md with UTF-8 encoding
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    try:
        rates, timestamp = fetch_exchange_rates()
        update_readme(rates, timestamp)
    except Exception as e:
        print(f"Error: {e}")
