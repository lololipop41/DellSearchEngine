from data import serviceDAO


class Service:
    def __init__(self):
        self.service = serviceDAO

    def view_service(self):
        service_list = self.service.get_service()
        return service_list

    def get_service(self):
        service = self.service.get_default_service()
        return service

    def select_service(self, sid):
        single_service = self.service.get_single_service(sid)
        return single_service
