"""
name : Controllers.py
author : chickpiz
date : 2019/01
coding : UTF-8
"""
from PyQt5.QtWidgets import QApplication
from Views import TreeDialog, MainWindow
from xml.etree.ElementTree import Element, ElementTree
import xml.etree.ElementTree as ET
import re


# Functions for convenience
def connect_action(action, func):
    action.triggered.connect(func)


class MainController:

    def __init__(self):
        self.window = MainWindow()
        self.connect_actions()
        self.current_file = None

    def connect_actions(self):
        # Toggle tree
        connect_action(self.window.act_toggle_tree, self.toggle_tree)
        # Tree clicked
        self.window.scn_tree.tree.clicked.connect(self.tree_clicked)
        # Add new item to tree
        self.window.scn_tree.btn_add.clicked.connect(self.add_tree_item)
        # Change tab in editor
        connect_action(self.window.edit.act_change_tab, self.change_tab)
        # New file
        connect_action(self.window.act_new, self.new_file)
        # Open file
        connect_action(self.window.act_open, self.open_file)
        # Save file
        connect_action(self.window.act_save, self.save_file)
        # Change font
        connect_action(self.window.act_font, self.change_font)

    def toggle_tree(self):
        if self.window.scn_tree.isHidden():
            self.window.scn_tree.show()
        else:
            self.window.scn_tree.hide()

    def tree_clicked(self):
        pass

    def change_tab(self):
        if self.window.edit.tab.currentIndex() == 0:
            self.window.edit.tab.setCurrentIndex(1)
        else:
            self.window.edit.tab.setCurrentIndex(0)

    def add_tree_item(self):
        dialog = TreeDialog(self.window)
        dialog.show()
        dialog.setFixedSize(dialog.size())

    def new_file(self):
        pass

    def open_file(self):
        pass

    def save_file(self):
        pass

    def change_font(self):
        pass

    # Text controlling
    def lines_to_xml(self, text, index, return_type=0):
        """
        <<return type>>
        0 : XML string
        1 : ElementTree Object (with <scn> root)
        """
        char_pat = re.compile('[\n.+:]')

        lines = text.split('\n')
        for line in lines:
            char_mat = char_pat.match()
            if char_mat is None:
                des = Element('des')

    def xml_to_lines(self):
        pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_controller = MainController()
    main_controller.window.show()
    exit(app.exec_())


class FTController:

    def __init__(self):
        pass
