from order import Order

person = Person("123456", "mmatheus")

person_name = Order(person, "123456").get_person_buyer().get_passport()


class PersonStub(object):

    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name
        self.get_passport = lambda: "12345678790"

stub_person = StubPerson("123456", "mmatheus")
stub_person_name = OrderStub(stub_person, "123456").get_person_buyer().get_passport()
