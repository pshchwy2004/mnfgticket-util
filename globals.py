service_list = []
ticket_list = []
ticket_id_counter = 0

# Looks up the service by name and returns the Service object instance and None if unable to lookup
def service_lookup(name):
    for service in service_list:
        if (name == service.name):
            return service
    return None

# Ticket Lookup
def ticket_lookup(id):
    for ticket in ticket_list:
        if (id == ticket.id):
            return ticket
    return None