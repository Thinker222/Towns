import os
import json


class Good:
    # A dictionary containing every type of good
    goods = {}

    # Initializes the function
    def __init__(self, name, kg_per_unit, value, decay_rate):
        self.__name = name
        self.__kg_per_unit = kg_per_unit
        self.__value = value
        self.__decay_rate = decay_rate
        Good.goods[self.__name] = self

    # Gets the decay for an individual day
    # Use the formula A = A0*e^kt where t is a day and k is the decay rate plus the mod.
    # Return the outcome
    def calulateDecay(self, mod):
        return None

    def getValue(self):
        return self.__value

    def getKgPerUnit(self):
        return self.__kg_per_unit


class GoodInstance:
    def __init__(self, name, decayVal=1):
        self.name = name
        self.__good = Good.goods[name]
        self.__decayVal = decayVal

    # Should update the decay valu using the calculate decay function
    # of the good and return 
    def updateDecay(self, mode):
        return None

    def getGood(self):
        return self.__good


class CMDModifyGood:

    # For creating the goods 
    @staticmethod
    def addGood():
        print("Input Name\n")
        name = input()
        print("Input kg per unit\n")
        kg_per_unit = int(input())
        print("Value\n")
        value = float(input())
        print("Decay Rate")
        decayRate = float(input())
        g = Good(name, kg_per_unit, value, decay_rate)

    # For storing information about the goods
    @staticmethod
    def storeGoods():
        file = open("Goods.json", 'w')
        json.dump(Good.goods, file)
        file.close()

    # For loading information about the goods 
    @staticmethod
    def readInGoods():
        if os.path.exists("Goods.json"):
            file = open("Goods.json", 'r')
            Good.goods = json.load(file)
