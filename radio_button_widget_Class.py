from pyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """This class creates a group of radio buttons from a given list of labels"""

    #constructor
    def __init__(self, label, instruction, button_list):
        super().__init__()

        #create widgets
        self.title_label = QLable(label)
        self.radio_grou_box = QGroupBox(instruction)
        self.radio_button_group = QButtonGroup()
        
