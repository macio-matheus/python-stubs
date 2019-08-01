class Order(object):

    def __init__(self, identifier, person_buyer):
        self.identifier = identifier
        self.person_buyer = person_buyer

    def get_person_buyer(self):
        return self.person_buyer
