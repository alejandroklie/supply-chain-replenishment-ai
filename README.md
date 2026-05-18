# Supply Chain Replenishment AI 📊

An automated data-driven operations and inventory optimization tool designed for fast-growing e-commerce brands sourcing globally (US, China, Vietnam). 

This project demonstrates how a **Business Administrator** leverages **Python** and predictive logistics to prevent stockouts, control safety stock, and optimize cash flow without manual intervention.

## 🚀 Key Features
* **Dynamic Reorder Point (ROP) Calculation:** Automatically computes the exact stock level required to trigger a new supplier order based on real-time sales velocity.
* **Lead Time & Safety Stock Integration:** Factors in overseas manufacturing/shipping transit days and safety cushions to eliminate supply chain disruptions.
* **Automated Stockout Forecasting:** Predicts exactly how many days of inventory are left for each product identifier.
* **Executive Operational Reporting:** Generates clean, structured terminal summaries and exports an automated administrative `.csv` report for stakeholder review.

## 🛠️ Tech Stack & Concepts
* **Language:** Python 3
* **Data Libraries:** Pandas (DataFrames & Data Manipulation)
* **Mathematical Modeling:** Math (Ceiling rounding for precise unit counts)
* **Core Concepts:** Supply Chain Logistics, Inventory Turnover, Operations Automation, Capital Efficiency.

## 📊 Sample Output Representation
When executed, the script processes current warehouse metrics and instantly outputs operational directives:

```text
Operational Replenishment Report:
  Product_ID         Product_Name  Current_Stock  Reorder_Point  Days_Until_Stockout Action_Required
0     BND-01  High-Waist Leggings            120            273                 14.1    ⚠️ ORDER NOW
1     BND-02       Sports Bra Pro             45            135                 10.7    ⚠️ ORDER NOW
2     GK-01     Oversized Hoodie             15            124                  4.8    ⚠️ ORDER NOW
3     GK-02       Running Shorts            210            300                 17.5    ⚠️ ORDER NOW
