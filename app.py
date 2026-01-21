from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

# ---------- DATABASE ----------
def get_connection():
    return sqlite3.connect("inventory.db")

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            order_quantity INTEGER,
            total_price REAL
        )
    """)

    conn.commit()
    conn.close()

create_tables()

# ---------- ROUTES ----------
@app.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return render_template("index.html", products=products)

@app.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form["name"]
        quantity = int(request.form["quantity"])
        price = float(request.form["price"])

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)",
            (name, quantity, price)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    return render_template("add_product.html")

@app.route("/order", methods=["GET", "POST"])
def place_order():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    message = ""

    if request.method == "POST":
        product_id = int(request.form["product_id"])
        order_qty = int(request.form["quantity"])

        cursor.execute("SELECT quantity, price FROM products WHERE id=?", (product_id,))
        product = cursor.fetchone()

        if product and product[0] >= order_qty:
            new_qty = product[0] - order_qty
            total_price = order_qty * product[1]

            cursor.execute("UPDATE products SET quantity=? WHERE id=?", (new_qty, product_id))
            cursor.execute(
                "INSERT INTO orders (product_id, order_quantity, total_price) VALUES (?, ?, ?)",
                (product_id, order_qty, total_price)
            )
            conn.commit()
            message = "Order placed successfully"
        else:
            message = "Insufficient stock"

    conn.close()
    return render_template("place_order.html", products=products, message=message)

# ---------- API ----------
@app.route("/product/<int:product_id>")
def get_product_quantity(product_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT quantity FROM products WHERE id=?", (product_id,))
    product = cursor.fetchone()
    conn.close()

    return jsonify({"quantity": product[0] if product else 0})

if __name__ == "__main__":
    app.run(debug=True)
