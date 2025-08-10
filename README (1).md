# 🏥 Hospital Resource Optimization

## 📌 Overview
This project analyzes **financial**, **inventory**, and **patient care** data to help hospitals make informed decisions about cost control, resource allocation, and operational efficiency. It provides insights into expenses, stock levels, patient bed usage, and resource utilization trends.

---

## 🔍 Features & Analysis

- **Data Cleaning:**
  - Strips extra spaces from column names.
  - Removes duplicate entries for clean, reliable data.

- **Financial Insights:**
  - Calculates total & average cost per expense category.
  - Tracks **monthly expense trends** across categories.

- **Inventory Management:**
  - Identifies items **below minimum stock** for timely restocking.

- **Patient Data Analysis:**
  - Finds **average bed days** by primary diagnosis.
  - Detects the **top used medical supplies & equipment**.

- **Visualization:**
  - **Line chart** of monthly expense trends by category for easy comparison.

---

## 🛠️ Tech Stack
- **Python** – Core programming language.
- **Pandas** – Data loading, cleaning, and analysis.
- **Matplotlib & Seaborn** – Data visualization.
- **Collections.Counter** – Counting and ranking frequently used items.

---

## 📊 Example Outputs

**1. Cost by Category:**
| Expense Category | Total Cost | Avg Cost |
|------------------|-----------:|---------:|
| Medical Supplies | $50,000    | $5,000   |

**2. Items Below Minimum Stock:**
| Item Name   | Current Stock | Min Required |
|-------------|--------------:|-------------:|
| Syringes    | 20            | 50           |

**3. Monthly Expense Trend Example:**
📈 *Line chart showing cost patterns per category over months.*

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Hospital_Resource_Optimization.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Hospital_Resource_Optimization
   ```
3. Install required packages:
   ```bash
   pip install pandas matplotlib seaborn
   ```
4. Run the script:
   ```bash
   python hospital_resource_optimization.py
   ```

---

## 📌 Future Improvements
- Add **predictive analytics** for stock needs.
- Build a **dashboard** for real-time monitoring.
- Integrate with hospital management systems for live data.
