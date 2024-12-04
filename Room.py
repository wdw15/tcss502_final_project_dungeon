from abc import ABC, abstractmethod
import random

class Room:
    def __init__(self):
        self._items = None
        self._doors = None

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, values):
        self._items = values

    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, values):
        """
        :param values: list of directions to place doors - north,south,east,west
        :return:
        """
        self._doors = [door.lower() for door in values]

    def display(self):
        return self.__str__()

    def draw(self):
        return self.__str__()

    def __str__(self):
        string = ''

        if self._items is not None and len(self._items)==1:
            obj = self._items[0].__repr__()
        elif self._items is not None and len(self._items)>1:
            obj = 'M'
        else:
            obj = ''

        if 'north' in (door.lower() for door in self.doors):
            string += '\n***___***'
        else:
            string += '\n*********'

        if 'east' in (door.lower() for door in self.doors) and 'west' in (door.lower() for door in self.doors):
            string += '\n*       *' + '\n|{:^7s}|'.format(obj) + '\n*       *'

        elif 'east' in (door.lower() for door in self.doors) and 'west' not in (door.lower() for door in self.doors):
            string += '\n*       *' + '\n*{:^7s}|'.format(obj) + '\n*       *'

        elif 'east' not in (door.lower() for door in self.doors) and 'west' in (door.lower() for door in self.doors):
            string += '\n*       *' + '\n|{:^7s}*'.format(obj) + '\n*       *'

        else:
            string += '\n*       *' + '\n*{:^7s}*'.format(obj) + '\n*       *'

        if 'south' in (door.lower() for door in self.doors):
            string += '\n***___***'
        else:
            string += '\n*********'

        print(string)
        return string


class HealingPotion:
    def __init__(self, min=5, max=15):
        self._hit_points = random.randint(min, max)
        self._name = 'Healing Potion'
        self._id = 'H'
    def __str__(self):
        return self._name
    def __repr__(self):
        return self._id


class VisionPotion:
    def __init__(self, min=6, max=10):
        self._vision_range = random.randint(min, max)
        self._name = 'Vision Potion'
        self._id = 'V'
    def __str__(self):
        return self._name
    def __repr__(self):
        return self._id


class Pit:
    def __init__(self, min=1, max=20):
        self._hit_points = random.randint(min, max)
        self._name = 'Pit'
        self._id = 'X'
    def __str__(self):
        return self._name
    def __repr__(self):
        return self._id


class Pillar:
    def __init__(self, pillar_name=None):
        if pillar_name is None:
            exit('Must Specify the Pillar Name: Abstraction, Encapsulation, Inheritance, or Polymorphism')
        self._name = str(pillar_name)
    def __str__(self):
        return self._name
    def __repr__(self):
        return self._name[0]


class Entrance:
    def __init__(self):
        pass
        self._name = 'Entrance'
        self._id = 'i'
    def __str__(self):
        return self._name
    def __repr__(self):
        return self._id


class Exit:
    def __init__(self):
        pass
        self._name = 'Exit'
        self._id = 'O'
    def __str__(self):
        return self._name
    def __repr__(self):
        return self._id


