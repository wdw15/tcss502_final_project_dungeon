from abc import ABC, abstractmethod
from Items import *

class Room:
    def __init__(self):
        self._items = None
        self._doors = None

        self._north = None
        self._south = None
        self._east = None
        self._west = None


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

    def __link_rooms__(self):
        pass

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


