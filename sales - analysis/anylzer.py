import pandas as pd
from helper import calculate_total, format_currency

df = pd.read_csv('data/sales.csv')

totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

df['total'] = totals

print("Sales Data:")
for index, row in df.iterrows():
    format_total = format_currency(row['total'])
    print(f"{row['product']}: {format_total}")

grand_total = df['total'].sum()
format_grand_total = format_currency(grand_total)
print(f"Grand Total: {format_grand_total}")    