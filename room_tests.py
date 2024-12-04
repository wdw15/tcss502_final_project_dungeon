import unittest
from Room import *

class RoomTests(unittest.TestCase):
    """unit tester for Room class"""

    def test_building_doors(self):
        room = Room()
        room.doors = ['north', 'south', 'east', 'west']

        self.assertEqual(room.doors, ['north', 'south', 'east', 'west'])

    def test_items(self):
        room = Room()
        room.items = ['healing potion', 'vision potion']

        self.assertEqual(room.items, ['healing potion', 'vision potion'])


    def test_drawing_room(self):
        room = Room()
        room.doors = ['north', 'south', 'east', 'west']
        room.items = ['healing potion', 'vision potion']

        room.__str__()

        room = Room()
        room.doors = ['north', 'east', 'west']
        pit = Pit()
        room.items = [pit]

        room.__str__()

        room = Room()
        room.doors = ['south', 'west']
        escape = Exit()
        room.items = [escape]

        room.__str__()

        room = Room()
        room.doors = ['south', 'north']
        item = HealingPotion()
        room.items = [item]

        room.__str__()


