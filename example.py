from order import Order
from person import Person
from order_stub import OrderStub
from person_stub import PersonStub

if __name__ == '__main__':

    person = Person("123456", "mmatheus")

    person_name = Order(person, "123456").get_person_buyer().get_passport()

    stub_person = PersonStub("123456", "mmatheus")
    stub_person_name = OrderStub(stub_person, "123456").get_person_buyer().get_passport()
