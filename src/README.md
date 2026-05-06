# 💰 Personal Expense Tracker (Python + Pandas)

## 📌 Overview

This project analyzes personal spending data using Python.
It performs data cleaning, aggregation, and visualization to uncover spending patterns across categories and time.

---

## ⚙️ Features

* Total and average spending calculation
* Category-wise spending analysis
* Monthly spending trends
* Top spending categories
* Data visualization dashboard

---

## 📊 Dashboard

![Dashboard](data/output/dashboard.png)

---

## 📈 Visualizations Used

* **Pie Chart** → Category-wise spending distribution
* **Line Chart** → Monthly spending trend
* **Histogram** → Distribution of expenses
* **Heatmap** → Correlation analysis

---

## 🧠 Key Insights

* Majority of spending comes from categories like bills and shopping
* Spending trends vary month-to-month
* Most expenses fall in mid-range values with some high outliers
* Data preprocessing is critical for accurate visualization

---

## 🛠️ Tech Stack

* Python
* Pandas
* Matplotlib
* Seaborn

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python src/main.py
```

---

## 📁 Project Structure

```
data/
  ├── personal_expense_tracker.csv
  └── output/dashboard.png

src/
  ├── loader.py
  ├── analysis.py
  ├── visualisation.py
  └── main.py
```

---

## 🔍 Challenges Faced

* Handling incorrect month ordering
* Fixing misleading visualizations due to missing months
* Resolving file path issues across modules
* Improving correlation analysis with limited numeric data

---

## 📌 Future Improvements

* Add interactive dashboard (Plotly / Power BI)
* Budget tracking and alerts
* Category-wise monthly trends
* Real-time expense input system

---

## ✅ Conclusion

This project demonstrates data cleaning, analysis, and visualization skills, along with problem-solving in handling real-world data issues.
