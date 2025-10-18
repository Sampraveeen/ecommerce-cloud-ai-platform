import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(os.path.dirname(BASE_DIR), "data", "sales.csv")
OUT_DIR = os.path.join(BASE_DIR, "outputs")
os.makedirs(OUT_DIR, exist_ok=True)

# Load
df = pd.read_csv(DATA_PATH)

# Basic cleaning
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Drop rows with critical nulls
df = df.dropna(subset=['date','category','amount']).copy()

# Remove negatives, cap outliers (winsorize-like)
df = df[df['amount'] >= 0]
q99 = df['amount'].quantile(0.99)
df.loc[df['amount'] > q99, 'amount'] = q99

# Save cleaned
cleaned_path = os.path.join(OUT_DIR, "cleaned_sales.csv")
df.to_csv(cleaned_path, index=False)

# --- Visualizations ---

# 1) Total sales by category
by_cat = df.groupby('category', as_index=False)['amount'].sum().sort_values('amount', ascending=False)
plt.figure()
plt.bar(by_cat['category'], by_cat['amount'])
plt.title('Total Sales by Category')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.xticks(rotation=20, ha='right')
plt.tight_layout()
plot1 = os.path.join(OUT_DIR, 'sales_by_category.png')
plt.savefig(plot1, dpi=200)
plt.close()

# 2) Sales trend over time (daily)
daily = df.groupby('date', as_index=False)['amount'].sum().sort_values('date')
plt.figure()
plt.plot(daily['date'], daily['amount'])
plt.title('Sales Trend (Daily)')
plt.xlabel('Date')
plt.ylabel('Amount')
plt.tight_layout()
plot2 = os.path.join(OUT_DIR, 'sales_trend.png')
plt.savefig(plot2, dpi=200)
plt.close()

print("Saved:")
print("-", plot1)
print("-", plot2)
print("-", cleaned_path)
