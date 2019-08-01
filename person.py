import requests


class Person(object):

    def __init__(self, identifier, name):
        self.name = name
        self.identifier = identifier

    def get_passport(self):
        return requests.post(url="http://foo.bar", data={"name": self.name})
