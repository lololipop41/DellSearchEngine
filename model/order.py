from data import checkoutDOA
from datetime import date


class Order:
    def __init__(self):
        self.order = checkoutDOA

    def save_order(self, customerid, productid, serviceid, finalperiod, finalprice):
        origindate = date.today().strftime('%Y-%m-%d');
        data = (customerid, productid, serviceid,origindate,finalperiod,finalprice)
        if self.order.add_order(data):
            return True, "Order has been created Successfully!"
        else:
            return False, "Order has not been created!"


#o = Order()
#r = o.save_order(3, 1, 2, 4, 7000.00)
#print(str(r))