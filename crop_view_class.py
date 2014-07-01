from PyQt4.Gui import *

import resources

class CropView(QGraphicsView):
    """This class provides a graphics view that has resources for displaying crop status visually"""

    #constructor
    def __init__(self):
        super().__init__()

    def resources(crop_type):
        #get the graphics
        seed = QPixmap(":/{0}_seed.png".format(crop_type))
        seedling = QPixmap(":/{0}_seedling.png".format(crop_type))
        young = QPixmap(":/{0}_young.png".format(crop_type))
        mature = QPixmap(":/{0}_mature.png".format(crop_type))
        old = QPixmap(":/{0}_old.png".format(crop_type))

        crop_pictures = [seed, seedling, young, mature, old]

        #add the graphics to scenes
        self.crop_Scenes = []
        for each in crop_pictures:
            self.crop_scenes.append(QGraphicsScene())
            self.crop_scenes[-1]
