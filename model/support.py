from data import supportDAO


class Support:
    def __init__(self):
        self.support = supportDAO

    def most_useful_support(self, pid):
        product_support_list = self.support.get_product_support(pid)
        support_usage_list = []
        for support in product_support_list:
            support_usage_list.append(support[3])
        index = support_usage_list.index(max(support_usage_list))
        most_usage_support = product_support_list[index]
        return most_usage_support[2], most_usage_support[3]

    def get_support(self, pid, sid):
        support = self.support.read_service(pid, sid)
        return support

    def update_usage(self, support_id, usage):
        if self.support.update_support(usage, support_id):
            return True
        else:
            return False
