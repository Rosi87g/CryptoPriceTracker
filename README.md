# CryptoPriceTracker

# 📈 Crypto Price Tracker (Streamlit + CoinGecko Pro API)

A real-time cryptocurrency price tracker built with **Streamlit**, powered by the **CoinGecko Pro API**, and enhanced with **email alerts** when Bitcoin or Ethereum cross user-defined thresholds.

---

## 🚀 Features

- 🔄 Auto-refresh every 10 seconds
- 📊 Live price visualization for Bitcoin & Ethereum
- 📧 Email alerts when prices exceed thresholds
- 🧠 Built with Python, Streamlit, and Matplotlib
- 🔐 Secure Gmail integration using App Passwords

---

## 🛠️ Requirements

Make sure you have Python 3.7+ installed.

Install dependencies using pip:

``bash
pip install streamlit streamlit-autorefresh matplotlib pandas requests

📦 Installation
- Clone the repository:
git clone https://github.com/your-username/crypto-price-tracker.git
cd crypto-price-tracker

- Save the main script as:
main.py

- Run the Streamlit app:
streamlit run main.py

🔐 Gmail Setup for Alerts
To send email alerts securely:
1. 	Enable 2-Step Verification on your Gmail account
2. 	Generate an App Password from Google Account Settings
3. 	Use that App Password in the app (not your regular Gmail password)

⚙️ Configuration
Inside , you can customize:
• 	 → Add/remove coins
• 	 → Change to , , etc.
• 	 → Replace with your CoinGecko Pro key

📸 Screenshots

<img width="1818" height="633" alt="Screenshot 2025-09-20 203625" src="https://github.com/user-attachments/assets/bf21e8ca-f240-45a6-863e-3fb2a48ee678" />


<img width="1796" height="767" alt="image" src="https://github.com/user-attachments/assets/cc04924c-97e6-436c-bb20-39bb70dbf08b" />
