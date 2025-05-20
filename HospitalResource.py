import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load datasets
financial_data = pd.read_csv("C:/Users/borgo/Desktop/KU Career/6th Sem/DAP Lab/Hotel_Resource_Optimization/financial_data.csv")
inventory_data = pd.read_csv("C:/Users/borgo/Desktop/KU Career/6th Sem/DAP Lab/Hotel_Resource_Optimization/inventory_data.csv")
patient_data = pd.read_csv("C:/Users/borgo/Desktop/KU Career/6th Sem/DAP Lab/Hotel_Resource_Optimization/patient_data.csv")

# -----------------------
# Data Cleaning
# -----------------------
# Strip whitespace from column names
financial_data.columns = financial_data.columns.str.strip()
inventory_data.columns = inventory_data.columns.str.strip()
patient_data.columns = patient_data.columns.str.strip()

# Drop duplicate rows
financial_data = financial_data.drop_duplicates()
inventory_data = inventory_data.drop_duplicates()
patient_data = patient_data.drop_duplicates()
# -----------------------
# Analysis
# -----------------------

# 1. Total and average cost by category
cost_by_category = financial_data.groupby('Expense_Category')['Amount'].agg(['sum', 'mean']).reset_index()
print("Cost by Category:\n", cost_by_category)

# 2. Items below minimum stock
low_stock_items = inventory_data[inventory_data['Current_Stock'] < inventory_data['Min_Required']]
print("\nItems Below Minimum Stock:\n", low_stock_items[['Item_Name', 'Current_Stock', 'Min_Required']])

# 3. Average bed days by diagnosis
avg_bed_days_by_diagnosis = patient_data.groupby('Primary_Diagnosis')['Bed_Days'].mean().reset_index()
print("\nAverage Bed Days by Diagnosis:\n", avg_bed_days_by_diagnosis)

# 4. Top used supplies and equipment
def explode_and_count(column):
    all_items = patient_data[column].dropna().str.split(', ').explode()
    return Counter(all_items)

supply_counter = explode_and_count('Supplies_Used')
equipment_counter = explode_and_count('Equipment_Used')

top_supplies = pd.DataFrame(supply_counter.most_common(5), columns=['Supply', 'Count'])
top_equipment = pd.DataFrame(equipment_counter.most_common(5), columns=['Equipment', 'Count'])

print("\nTop 5 Supplies Used:\n", top_supplies)
print("\nTop 5 Equipment Used:\n", top_equipment)

# 5. Monthly expense trend by category
financial_data['Month'] = financial_data['Date']
monthly_expense_trend = financial_data.groupby(['Month', 'Expense_Category'])['Amount'].sum().unstack().fillna(0)

# Plotting
plt.figure(figsize=(12, 6))
monthly_expense_trend.plot(kind='line', marker='o')
plt.title("Monthly Expense Trend by Category")
plt.ylabel("Total Amount ($)")
plt.xlabel("Month")
plt.grid(True)
plt.tight_layout()
plt.show()
