import os
from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for the menu page
@app.route('/menu')
def menu():
    return render_template('menu.html')

# Route for the cart page
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Route for the order confirmation page
@app.route('/order_confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
