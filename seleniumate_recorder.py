from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.button = QtGui.QPushButton('Test', self)
        self.button.clicked.connect(self.handleButton)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.button)

    def handleButton(self):
        print ('Hello World')

    def fill_dropdown(self, list):
        pass
        # Here the list is added to dropdown

    def focus_on_object(self):
        pass
        # self.chosen_from_dropdown -> focus on button like
        # self.elem = driver.find_element_by_name(        self.chosen_from_dropdown)
        # self.json.append(FOCUS, self.chosen_from_dropdown)

    def press_enter(self):
        pass
        # self.elem.send_keys(Keys.RETURN)
        # self.json.append(ENTER)

    def enter_text(self):
        pass
        # text = self.get_from_textbox
        # elem.send_keys(text)
        # self.json.append(ENTER_TEXT, text)

    def assert_headline(self):
        pass
        # text = self.get_from_textbox
        # self.assertIn(text, driver.title)
        # self.json.append(ASSERT_HEADLINE, text)

    def assert_in_page(self):
        pass
        # text = self.get_from_textbox
        # assert text not in driver.page_source
        # self.json.append(ASSERT_SOURCE, text)

    def save_json(self):
        pass
        # save to file list in self.json

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())