from Animal_class import *

class Sheep(Animal):
    """A sheep simulation"""

    #constructor
    def __init__(self):
        super(). __init__(1,3,6)
        self._type = "Sheep"

        def grow(self, food, water):
            if food >= self._food_need and water >= self._water_need:
                if self._status == "Baby" and water > self._water_need:
                    self._weight += self._growth_rate *1.5
                elif self._status == "Newborn" and water > self._water_need:
                    self._weight += self._growth_rate *1.25
                else:
                    self._weight += self._growth_rate
            self._days_growing += 1
            self.update_status()

def main():
    new_sheep = Sheep()
    print(new_sheep.report())
    manual_grow(new_sheep)
    print(new_sheep.report())
    manual_grow(new_sheep)
    print(new_sheep.report())

if __name__ == "__main__":
    main()
