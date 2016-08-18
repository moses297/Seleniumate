from PyQt4 import QtGui
from selenium import webdriver
from itertools import izip
from utils import ENTER_TEXT, FOCUS, ASSERT_HEADLINE, ASSERT_PAGE, CONNECT
from selenium.webdriver.common.keys import Keys
import json

class Window(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.json_arr = []
        self.connect_to_site = QtGui.QPushButton('Connect', self)
        self.connect_to_site.clicked.connect(self.connect_function)
        self.button3 = QtGui.QPushButton('Press Item', self)
        self.button3.clicked.connect(self.press_enter)
        self.button4 = QtGui.QPushButton('Enter Text', self)
        self.button4.clicked.connect(self.enter_text)
        self.save_json_button = QtGui.QPushButton('Save JSON', self)
        self.save_json_button.clicked.connect(self.save_json)
        self.assert_headline_button = QtGui.QPushButton('Assert Headline', self)
        self.assert_headline_button.clicked.connect(self.assert_headline)
        self.assert_in_page_button = QtGui.QPushButton('Assert Source', self)
        self.assert_in_page_button.clicked.connect(self.assert_in_page)


        self.dropdown = QtGui.QComboBox(self)
        self.textbox = QtGui.QLineEdit(self)
        self.url_textbox = QtGui.QLineEdit(self)

        box_list = [self.url_textbox, self.textbox, self.dropdown]
        button_list = [self.connect_to_site, self.button3, self.button4, self.assert_headline_button, self.assert_in_page_button, self.save_json_button]
        button_location = [20, 0]
        self.format_button_list(button_list, button_location)
        for box in box_list:
            box.resize(200, 24)

        button_location = [125, 1]
        self.format_button_list(box_list, button_location)

        layout = QtGui.QVBoxLayout(self)
        self.resize(540, 300)

    def fill_dropdown(self):
        self.dropdown.clear()
        ids = self.driver.find_elements_by_xpath('//*[@id]')
        for id_obj in ids:
            self.dropdown.addItem(id_obj.get_attribute('id'))

    def connect_function(self):
        self.driver = webdriver.Firefox()
        url = str(self.url_textbox.text())
        self.driver.get(url)
        self.fill_dropdown()
        self.json_arr.append({CONNECT: url})

    def press_enter(self):
        id = str(self.dropdown.currentText())
        self.elem = self.driver.find_element_by_name(id)
        self.json_arr.append({FOCUS: id})
        self.elem.send_keys(Keys.RETURN)

    def enter_text(self):
        id = str(self.dropdown.currentText())
        self.elem = self.driver.find_element_by_name(id)
        self.json_arr.append({FOCUS: id})
        text = str(self.textbox.text())
        self.elem.send_keys(text)
        self.json_arr.append({ENTER_TEXT: text})

    def assert_headline(self):
        text = str(self.textbox.text())
        if text in self.driver.title:
            print "Assert Pass"
        else:
            print "Assert Fail"
        self.json_arr.append({ASSERT_HEADLINE: text})

    def assert_in_page(self):
        text = str(self.textbox.text())
        if text in self.driver.page_source:
            print "Assert Pass"
        else:
            print "Assert Fail"
        self.json_arr.append({ASSERT_PAGE: text})

    def save_json(self):
        new_json = {}
        counter = 0
        for item in self.json_arr:
            new_json[counter] = item
            counter += 1
        with open('data.txt', 'w') as outfile:
            json.dump(new_json, outfile)

    @staticmethod
    def format_button_list(button_list, location):
        for button in button_list:
            location[1] += 30
            button.move(location[0], location[1])

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())