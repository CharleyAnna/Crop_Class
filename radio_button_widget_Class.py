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
        
        #create the radio buttons
        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))

        #set default checked item
        self.radio_bitton_list[0].setChecked(True)

        #create layout for radio buttons and add them
        self.radio_button_layout = QVBoxLayout()

            
        
