# Bynry Backend Case Study – StockFlow

## 🚀 Overview
This project implements a simplified Inventory Management System backend for Bynry Inc., handling product creation, inventory tracking, and low-stock alerts.

## 🔧 Tech Stack
- Python
- Flask
- SQLAlchemy
- SQLite (for demonstration)

---

## ✅ Part 1: Code Review & Debugging
### Endpoint
POST `/api/products`

### Features:
- Input validation
- SKU uniqueness enforced
- Transaction-safe DB commit
- Inventory creation tied to product

---

## 🛠️ Part 2: Database Schema
### Tables:
- Company
- Warehouse
- Product
- Supplier
- Inventory
- ProductThreshold
- Sales

---

## 🔔 Part 3: Low Stock Alert API
GET `/api/companies/<company_id>/alerts/low-stock`

Returns list of products with low stock based on recent sales.

---

## 🧪 Setup Instructions

```bash
git clone https://github.com/yourusername/bynry-backend-case-study.git
cd bynry-backend-case-study
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python run.py
```

---

## 📦 Assumptions
- Thresholds are global per product
- Sales activity is within 30 days
