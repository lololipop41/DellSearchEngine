from data import checkoutDOA

class Displaysupport:
    def __init__(self):
        self.displaysupport = checkoutDOA

    def show_order(self, customerid):
        order_list = self.displaysupport.get_order(customerid)
        return order_list

#s=Displaysupport()
#o=s.show_order(1)
#print(str(o))
