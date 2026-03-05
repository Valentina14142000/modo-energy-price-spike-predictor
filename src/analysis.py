import pandas as pd

def load_ercot_data(file_path="data/ercot_data.csv"):
    """
    Load ERCOT CSV data and prepare datetime.
    """
    df = pd.read_csv(file_path)
    df['time'] = pd.to_datetime(df['time'])
    return df

def detect_peak_demand(df, percentile=0.95):
    """
    Detect hours where demand exceeds the given percentile threshold.
    """
    threshold = df['demand'].quantile(percentile)
    df['peak_demand'] = df['demand'] > threshold
    return df, threshold

def battery_trading_simulator(df, capacity_mwh=10, max_charge_mw=2, efficiency=0.95):
    """
    Simulate battery charge/discharge to maximize profit based on prices.
    Heuristic: charge low (<25th percentile), discharge high (>75th percentile)
    """
    df = df.copy()
    df['battery_soc'] = 0.0      # State of charge
    df['charge_action'] = 0.0    # +ve = charging, -ve = discharging
    df['profit'] = 0.0
    
    soc = 0.0
    
    low_price = df['price'].quantile(0.25)
    high_price = df['price'].quantile(0.75)
    
    for i, row in df.iterrows():
        price = row['price']
        
        if price <= low_price:  # Charge
            charge = min(max_charge_mw, capacity_mwh - soc)
            soc += charge * efficiency
            profit = -charge * price
            df.at[i, 'charge_action'] = charge
        elif price >= high_price:  # Discharge
            discharge = min(max_charge_mw, soc)
            soc -= discharge
            profit = discharge * price
            df.at[i, 'charge_action'] = -discharge
        else:  # Hold
            profit = 0
        
        df.at[i, 'battery_soc'] = soc
        df.at[i, 'profit'] = profit
    
    total_profit = df['profit'].sum()
    return df, total_profit