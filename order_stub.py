class OrderStub(object):

    def __init__(self, identifier, person_buyer):
        self.identifier = identifier
        self.person_buyer = person_buyer
        self.get_person_buyer = lambda: OrderStub(self.identifier, self.get_person_buyer)
        self.get_passport = lambda: "12345678790"
