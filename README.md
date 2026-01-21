# Inventory & Order Management System

A full-stack web application to manage products and orders with real-time inventory validation.  
Built using **Python (Flask)** with a **top-company style UI (Apple / Stripe inspired)** and **Light & Dark mode** support.

This project is designed to be **resume-ready**, **interview-defendable**, and **recruiter-friendly**.

---

## 🚀 Features

- Add products with name, quantity, and price
- View all products in a clean, professional table
- Place orders with automatic stock validation
- Display **available quantity before placing an order**
- Prevent orders when stock is insufficient
- Automatic inventory updates after each order
- Modern **Apple-style UI**
- **Light / Dark mode toggle**
- Beginner-friendly and clean codebase

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Database:** SQLite  
- **Frontend:** HTML, CSS, JavaScript  
- **Version Control:** Git, GitHub  

---

## 📂 Project Structure

inventory-order-management/
│
├── app.py
├── requirements.txt
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── add_product.html
│ ├── place_order.html
│
└── static/
└── style.css

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/inventory-order-management.git
cd inventory-order-management
Install dependencies
python -m pip install flask

3️⃣ Run the application
python app.py

4️⃣ Open in browser
http://127.0.0.1:5000
```


🧪 How the Application Works
Products are stored in a SQLite database

Orders reduce available stock automatically

Backend API provides live inventory data

JavaScript fetches and displays available quantity dynamically

CSS variables enable smooth light/dark theme switching

UI follows modern enterprise design principles

🧠 What I Learned
Building full-stack applications using Flask

Designing backend APIs and integrating them with frontend JavaScript

Managing inventory logic and validations

Working with SQLite databases

Implementing modern UI/UX without frameworks

Using Git and GitHub for version control

🔮 Future Enhancements
Order history page

User authentication

Inventory analytics & charts

Product search and filtering

Cloud deployment (Render / Railway)

👤 Author
Mohammed Jazaa

GitHub: jazaa2012

LinkedIn: mohammed-jazaa

