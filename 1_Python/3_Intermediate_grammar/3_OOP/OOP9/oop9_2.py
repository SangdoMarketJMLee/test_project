from abc import ABCMeta
from abc import abstractmethod

class AirPlane(metaclass=ABCMeta):
    @abstractmethod
    def flight(self):
        pass
    def forward(self):
        print('전진!!')
    def backward(self):
        print('후진')

class Airliner(AirPlane):
    def __init__(self,c):
        self.color = c
    def flight(self):
        print('시속 400km/h 비행')

al = Airliner('red')
al.flight()
al.forward()
al.backward()

class fighterPlane(AirPlane):
    def __init__(self,c):
        self.color = c
    def flight(self):
        print('시속 700km/h 비행')


fl = fighterPlane('red')
fl.flight()
fl.forward()
fl.backward()