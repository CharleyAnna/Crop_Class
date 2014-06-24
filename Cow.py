from Animal_class import *

class Cow(Animal):
    """A cow simulation"""

    #constructor
    def __init__(self):
        super(). __init__(1,3,6)
        self._type = "Cow"

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
    new_cow = Cow()
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())

if __name__ == "__main__":
    main()
