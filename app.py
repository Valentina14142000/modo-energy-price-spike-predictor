import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#  Page Config 
st.set_page_config(
    page_title="ERCOT Electricity Market Dashboard",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ ERCOT Electricity Market Dashboard")
st.markdown("Real-time monitoring of demand, prices, and price spike detection in the ERCOT market.")

#  Load Data 
@st.cache_data
def load_data():
    df = pd.read_csv("data/ercot_data.csv")
    df['time'] = pd.to_datetime(df['time'])
    return df

df = load_data()

# Show raw data 
with st.expander("View raw data sample (first 100 rows)"):
    st.dataframe(df.head(100))

#  Demand Over Time 
st.subheader("Demand Over Time")
fig1, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(df['time'], df['demand'], color='#1f77b4', linewidth=1.5)
ax1.set_xlabel("Time")
ax1.set_ylabel("Demand (MW)")
ax1.grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig1)

#  Price vs Demand 
st.subheader("Price vs Demand")
fig2, ax2 = plt.subplots(figsize=(10, 5))
ax2.scatter(df['demand'], df['price'], alpha=0.6, s=15, color='#ff7f0e')
ax2.set_xlabel("Demand (MW)")
ax2.set_ylabel("Price ($/MWh)")
ax2.grid(True, alpha=0.3)

# Linear trend line
if len(df) >= 10:
    z = np.polyfit(df['demand'], df['price'], 1)
    p = np.poly1d(z)
    ax2.plot(df['demand'], p(df['demand']), color="red", linewidth=1.5, linestyle="--",
             label=f"Trend (slope = {z[0]:.3f})")
    ax2.legend()

plt.tight_layout()
st.pyplot(fig2)

#  Price Spikes Detection 
st.subheader("Price Spikes Detection")
threshold = df['price'].quantile(0.95)
df['price_spike'] = df['price'] > threshold
spike_count = df['price_spike'].sum()
st.markdown(f"**Detected {spike_count} price spike(s)** (price > ${threshold:,.0f}/MWh)")

if spike_count > 0:
    st.dataframe(
        df[df['price_spike']]
        .sort_values('price', ascending=False)
        .style.format({'price': '${:,.2f}', 'demand': '{:,.0f} MW'})
    )
else:
    st.info("No price spikes detected above the 95th percentile threshold.")

#  Quick Statistics 
st.subheader("Quick Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Max Price", f"${df['price'].max():,.2f}")
col2.metric("95th Percentile", f"${threshold:,.2f}")
col3.metric("Spike Threshold", f">${threshold:,.2f}")