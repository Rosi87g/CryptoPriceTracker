import requests, streamlit as st, pandas as pd, smtplib, datetime, matplotlib.pyplot as plt
from email.mime.text import MIMEText
from streamlit_autorefresh import st_autorefresh

# --- CONFIG ---
API_KEY = 'CG-MkBbueCASuHXg42RKegRvyYC'
coins = ['bitcoin', 'ethereum']
currency = 'usd'

# --- AUTO-REFRESH (every 10 seconds) ---
st_autorefresh(interval=10 * 1000, limit=100, key="crypto_refresh")

# --- STREAMLIT UI ---
st.set_page_config(page_title="Crypto Price Tracker", layout="wide")
st.title("📈 Crypto Price Tracker")
st.caption("Live prices for Bitcoin & Ethereum in USD with email alerts")
st.caption("Auto Refresh Enchances in 10 Seconds")

# --- USER INPUT ---
email_sender = st.text_input("Your Gmail Address", "your_email@gmail.com")
email_password = st.text_input("Your Gmail App Password", type="password")
email_recipient = email_sender  # You receive alerts yourself

st.subheader("🔔 Set Alert Thresholds (USD)")
thresholds = {}
for coin in coins:
    thresholds[coin] = st.number_input(f"{coin.capitalize()} Alert Price (USD)", min_value=0.0, value=0.0)

# --- FETCH PRICE ---
def get_price(coin, currency='usd'):
    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={currency}"
        headers = {'x-cg-pro-api-key': API_KEY}
        response = requests.get(url, headers=headers)
        data = response.json()
        price = data.get(coin, {}).get(currency)
        if price is None:
            st.warning(f"⚠️ No price found for {coin}")
            return 0
        return price
    except Exception as e:
        st.error(f"Error fetching price for {coin}: {e}")
        return 0

# --- SEND EMAIL ALERT ---
def send_alert(coin, price):
    msg = MIMEText(f"🚨 {coin.upper()} has reached ${price}")
    msg['Subject'] = f"Crypto Alert: {coin.upper()}"
    msg['From'] = email_sender
    msg['To'] = email_recipient
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(email_sender, email_password)
            s.send_message(msg)
        st.success(f"Email sent for {coin.upper()} at ${price}")
    except Exception as e:
        st.error(f"Failed to send email: {e}")

# --- PRICE TABLE ---
price_data = {}
for coin in coins:
    price = get_price(coin)
    price_data[coin] = price
    if price and thresholds[coin] > 0 and price >= thresholds[coin]:
        send_alert(coin, price)

df = pd.DataFrame(price_data.items(), columns=['Coin', f'Price ({currency.upper()})'])
st.subheader("💰 Current Prices")
st.table(df)

# --- LIVE TREND VISUALIZATION ---
st.subheader("📊 Live Price Trends")
if 'price_history' not in st.session_state:
    st.session_state.price_history = {coin: [] for coin in coins}
    st.session_state.timestamps = []

timestamp = datetime.datetime.now().strftime("%H:%M:%S")
st.session_state.timestamps.append(timestamp)

for coin in coins:
    st.session_state.price_history[coin].append(price_data[coin])

fig, ax = plt.subplots(figsize=(10, 5))
for coin in coins:
    ax.plot(st.session_state.timestamps, st.session_state.price_history[coin], label=coin)
ax.set_xlabel("Time")
ax.set_ylabel(f"Price ({currency.upper()})")
ax.set_title("Live Crypto Prices")
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)