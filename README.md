# python-stubs

A simple way to create class Stubs in Python


Example
----


import requests


class Person(object):

    def __init__(self, identifier, name):
        self.name = name
        self.identifier = identifier

    def get_passport(self):
        return requests.post(url="http://foo.bar", data={"name": self.name})


class Order(object):

    def __init__(self, identifier, person_buyer):
        self.identifier = identifier
        self.person_buyer = person_buyer

    def get_person_buyer(self):
        return self.person_buyer


person = Person("123456", "mmatheus")

person_name = Order(person, "123456").get_person_buyer().get_passport()


class StubPerson(object):

    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name
        self.get_passport = lambda: "12345678790"


class StubOrder(object):

    def __init__(self, identifier, person_buyer):
        self.identifier = identifier
        self.person_buyer = person_buyer
        self.get_person_buyer = lambda: StubOrder(self.identifier, self.get_person_buyer)
        self.get_passport = lambda: "12345678790"


stub_person = StubPerson("123456", "mmatheus")
stub_person_name = StubOrder(stub_person, "123456").get_person_buyer().get_passport()
