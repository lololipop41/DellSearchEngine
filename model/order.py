from data import orderDAO
from datetime import date


class Order:
    def __init__(self):
        self.order = orderDAO

    def save_order(self, customerid, productid, serviceid, finalperiod, finalprice):
        origindate = date.today().strftime('%Y-%m-%d');
        data = (customerid, productid, serviceid, origindate, finalperiod, finalprice)
        if self.order.add_order(data):
            return True, "Order has been created Successfully!"
        else:
            return False, "Order has not been created!"

    def show_order(self, customerid):
        order_list = self.order.get_order(customerid)
        return order_list
