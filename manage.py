# This is controller
from flask import Flask, render_template, request
from model import user, product, services, order
from service import support_recommend, seek_support


app = Flask(__name__)


@app.route('/')
def default():
    pcart.clear()
    scart.clear()
    return render_template('home.html')


@app.route('/login', methods=['POST'])
def login_to_home():
    username = request.form['username']
    password = request.form['password']
    customer = user.User()
    result = customer.sign_in(username, password)
    token = result[0]
    msg = result[1]
    if token:
        print(msg)
        return render_template('home.html')
    else:
        print(msg)
        return render_template('login.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def go_to_register():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    customer = user.User()
    result = customer.sign_up(username, password)
    token = result[0]
    msg = result[1]
    if token:
        print(msg)
        return render_template('login.html')
    else:
        print(msg)
        return render_template('register.html')


@app.route('/product')
def go_to_view_products():
    product_list = product.Product().view_product()
    return render_template('products.html', product_list=product_list, product_count=len(product_list))


@app.route('/customize')
def customize():
    pid = request.args['product_id']
    most_useful = support_recommend.support_recommendation(pid)
    single_product = product.Product().select_product(pid)
    service_list = services.Service().view_service()
    return render_template('customize.html', record=single_product, service_list=service_list, most_useful=most_useful)


pcart = []
scart = []


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    service_id = request.form['sid']
    pid = request.form['pid']
    scart.append(service_id)
    pcart.append(pid)
    single_product = product.Product().select_product(pid)
    service_list = services.Service().view_service()
    return render_template('customize.html', record=single_product, service_list=service_list)


@app.route('/cart')
def go_to_cart():
    prod_list = []
    serv_list = []
    for item in pcart:
        single_product = product.Product().select_product(item)
        prod_list.append(single_product)

    for item in scart:
        single_service = services.Service().select_service(item)
        serv_list.append(single_service)

    prod_serv_list = zip(prod_list, serv_list)

    return render_template('cart.html', prod_serv_list=prod_serv_list)


@app.route('/support')
def go_to_support():
    uid = 1
    order_list = order.Order().show_order(uid)
    prod_list = []
    for item in order_list:
        prod_id = item[2]
        prod_list.append(product.Product().select_product(prod_id))
    prod_order_list = zip(order_list, prod_list)
    return render_template('support.html', prod_order_list=prod_order_list)


@app.route('/warranty')
def warranty():
    pid = request.args['product_id']
    sid = request.args['service_id']
    seek_support.seeking_for_support(pid, sid)
    single_product = product.Product().select_product(pid)
    service_list = services.Service().view_service()
    return render_template('warranty.html', record=single_product, service_list=service_list)


if __name__ == '__main__':
    app.run(debug=True)
