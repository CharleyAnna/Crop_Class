class Crop:
    """ A generic food crop"""

    #Constructor
    def __init__(self, growth_rate, light_need, water_need):
        #Set the attributes with an initial value
        
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def needs(self):
        #return a dictionary containing the light and water needs
        return{'Light Need':self._light_need, 'Water Need':self._water_need}

    #method to report the information about the current state of crop
    def report(self):
        #return a dictionary containing the type, status, growth and days growing
        return{'Type':self._type, 'Status':self._status, 'Growth':self._growth, 'Days Growing':self._days_growing}

    def update_status(self):
        pass

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += sellf._growth_rate
            
        
        
def main():
    #instantiate the class
    new_crop = Crop(1, 4, 3)
    print(new_crop.needs())
    print(new_crop.report())
    

if __name__ == "__main__":
    main()
