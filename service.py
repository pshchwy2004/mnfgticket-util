class Service:
    def __init__(self, id, name, n_price, c_price, tags):
        self.id = id
        self.name = name
        self.n = n_price
        self.c = c_price
        self.tags = tags
        
class Ticket:
    def __init__(self, techs, services):
        self.tech_list = techs
        self.services = services
    
    def add_to_services(self, service):
        self.services.append(service)
    
    def remove_service(self, service_name):
        for service in self.services:
            if (service.name == service_name):
                self.services.remove(service)
                break
    
    