class Model:

    def __init__(self):
        self._name = ''
        self._phone = ''
        self._email = ''
        self._addr = ''

    @property
    def name(self) -> str: return self._name

    @name.setter
    def name(self, name): self._name = name

    @property
    def phone(self) -> str: return self._phone

    @phone.setter
    def name(self, phone): self._phone = phone

    @property
    def email(self) -> str: return self._email

    @name.setter
    def email(self, email): self._email = email

    @property
    def addr(self) -> str: return self._addr

    @addr.setter
    def addr(self, addr): self._addr = addr
