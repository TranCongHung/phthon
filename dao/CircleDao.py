from abc import ABC,abstractmethod
from model.Circle import Circle

class CircleDao(ABC):
    @abstractmethod
    def importData():
        pass
    @abstractmethod
    def insertCircle(circle : Circle):
        pass
    @abstractmethod
    def updateCircle(circle : Circle):
        pass
    @abstractmethod
    def deleteCircle(circle : Circle):
        pass
    @abstractmethod
    def showList(circle : Circle):
        pass
