class Model:

    def __init__(self):
        self._PassengerId = ''
        self._Survived = ''
        self._Pclass = ''
        self._Name = ''
        self._Sex = ''
        self._Age = ''
        self._SibSp = ''
        self._Parch = 0
        self._Ticket = 0
        self._Fare = 0
        self._Cabin = 0
        self._Embarked = 0


class Entity:
    context: str
    fname: str
    train: object
    test: object
    id: str
    label: str

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test

    @train.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @train.setter
    def id(self, train): self._id = id

    @property
    def label(self) -> str: return self._label

    @train.setter
    def label(self, label): self._label = label
# context (str), fname (str), train (object), test(object), id (str), label(str)


class Service:
    def __init__(self):
        self.entity = Entity() # 보안객체가 아닐떄는 _ 사용하지 않는다.

    def new_entity(self, payload):
        this = self.entity
        this.context = './data/'
        this.fname = payload


class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this

    def preprocess(self, train, test):
        pass


def print_menu():
    print('0. Exit')
    print('1. Start')
    return input('Menu\n')


while 1:
    menu = print_menu()
    if menu == '0': break
    if menu == '1':
        app = Controller()
        print('start')