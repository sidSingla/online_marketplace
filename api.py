from flask import Flask, request
app = Flask(__name__)

import db

@app.route('/get')
def get_products():
    product = request.args.get('product')

    if product == 'all':
        query = "SELECT TITLE, PRICE from PRODUCTS WHERE INV_COUNT > 0"
    else:
        query = "SELECT TITLE, PRICE from PRODUCTS WHERE TITLE='%s' AND INV_COUNT > 0" %(product)

    inventory = db.select_from_table(query)

    if len(inventory) == 0:
        return "Product is not available\n"

    res = ""
    for row in inventory:
        res += "Product: %s, Price: %s\n" % (row[0], row[1])

    return res

cart = []
def add_cart(price, tot_cost):
    tot_cost += price
    return tot_cost

# Prints out all the items in the cart and empties it.
@app.route('/checkout')
def checkout_cart():
    global cart
    tot_cost = 0
    print("Cart", cart)
    for item in cart:
        tot_cost += item[1]
    cart_items = str(cart)
    cart = []
    return "Cart %s Checked out with total cost %d\n" % (cart_items, tot_cost)

@app.route('/checkcart')
def check_cart():
    return str(cart) + "\n"

@app.route('/purchase')
def purchase_products():
    product = request.args.get('product')
    query = "SELECT INV_COUNT, TITLE, PRICE from PRODUCTS WHERE TITLE='%s'" %(product)
    res = db.select_from_table(query)
    if res is None or len(res) == 0:
        return "Product not in inventory. Cannot be purchased\n"

    inv_count, title, price = res[0]
    if inv_count == 0:
        return "Product not in inventory. Cannot be purchased\n"

    global cart
    query = "UPDATE PRODUCTS SET INV_COUNT=%d WHERE TITLE='%s'" % (inv_count - 1, product)
    res = db.update_table(query)
    if res == "Success":
        cart.append((title, price))
        return "Product added to cart %s\n" % product
    else:
        return "Failure in adding product to cart\n"

if __name__ == '__main__':
    app.run()
