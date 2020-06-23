from contacts.model import Model
from contacts.service import Service


class Controller:

    def __init__(self):
        self._service = Service()

    def register(self, name, phone, email, addr):
        model = Model()
        model.name = name
        model.phone = phone
        model.email = email
        model.addr = addr
        self._service.add_contact(model)
        print('등록완료')

    def search(self, payload):
        model = Model()

    def list(self):
        pass

    def remove(self):
        pass