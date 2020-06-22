from calculator.model import Model
from calculator.service import Service


class Controller:
    # __init__ 을 사용하지 않으면
    # 생략이 가능하다.
    def calc(self, num1, num2, opcode):
        model = Model()
        # set 문법
        model.num1 = num1
        model.num2 = num2
        model.opcode = opcode
        service = Service(model)
        if opcode == '+': result = service.add()
        if opcode == '-': result = service.minus()
        if opcode == '*': result = service.multi()
        if opcode == '/': result = service.divide()
        return result
