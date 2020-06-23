class Service:

    def __init__(self):
        self._contacts = []

    def add_contact(self, payload):
        self._contacts.append(payload)
        print(self._contacts)

    def get_contact(self, payload):  # name
        #for i in payload:
         #   if i
          #      break
        pass

    def get_contacts(self):
        pass

    def del_contact(self, payload):  # name
        pass
