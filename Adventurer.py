import random


class Adventurer:
    def __init__(self, name=None, min_range=75, max_range=100):
        self._name = name
        self._hit_points = random.randint(min_range, max_range)
        self._healing_potions = []
        self._vision_potions = []
        self._pillars_found = []


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def hit_points(self):
        return self._hit_points

    @hit_points.setter
    def hit_points(self, hit_points):
        self._hit_points += hit_points if (hit_points+self._hit_points) < 100 else 100

    @property
    def healing_potions(self):
        return len(self._healing_potions)

    @healing_potions.setter
    def healing_potions(self, healing_potions):
        self._healing_potions.append(healing_potions)

    @property
    def vision_potions(self):
        return len(self._vision_potions)

    @vision_potions.setter
    def vision_potions(self, vision_potions):
        self._vision_potions.append(vision_potions)

    @property
    def pillars_found(self):
        return len(self._pillars_found)

    @pillars_found.setter
    def pillars_found(self, pillars_found):
        self._pillars_found.append(pillars_found)