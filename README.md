## Python Stubs

A simple way to create class Stubs in Python. The technique is to use Python lambda functions to simulate the behavior of the original class when using instantiated functions. With this technique, the amount of code is greatly reduced.

Stubs are useful when building unit tests where libraries eventually do not provide utility classes to facilitate the creation of unit tests.


### Example

Example of a class Person who has a method that makes an Http call. In unit tests, it is not of interest to evaluate external calls to the method, so we use a Stub to simulate this behavior.

```python

import requests

class Person(object):

    def __init__(self, identifier, name):
        self.name = name
        self.identifier = identifier

    def get_passport(self):
        return requests.post(url="http://foo.bar", data={"name": self.name})

```

We have an Order class that uses a Person method indirectly.

```python

class Order(object):

    def __init__(self, identifier, person_buyer):
        self.identifier = identifier
        self.person_buyer = person_buyer

    def get_person_buyer(self):
        return self.person_buyer

```

The excerpt below, instantiates the two classes previously demonstrated and uses a method that via HTTP gets information from the server.

```python

person = Person("123456", "mmatheus")

person_name = Order(person, "123456").get_person_buyer().get_passport()

```

Now we have an example of the StubPerson class, where we simulate the same method call behavior as the original class.

```python

class PersonStub(object):

    def __init__(self, identifier, name):
        self.identifier = identifier
        self.name = name
        self.get_passport = lambda: "12345678790"

```

Now we have an example of the StubOrder class, where we simulate the same method call behavior as the original class.

```python

class OrderStub(object):

    def __init__(self, identifier, person_buyer):
        self.identifier = identifier
        self.person_buyer = person_buyer
        self.get_person_buyer = lambda: OrderStub(self.identifier, self.get_person_buyer)
        self.get_passport = lambda: "12345678790"

```

The code below demonstrates that the stub has the same call syntax and has the same return and parameterization types as the original classes, but this time without making external calls to the server, making it possible to create unit tests.

```python

stub_person = PersonStub("123456", "mmatheus")
stub_person_name = OrderStub(stub_person, "123456").get_person_buyer().get_passport()

```

### TODO

- Create more examples
- Create example using pytest