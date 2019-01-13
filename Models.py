"""
name : Models.py
author : chickpiz
date : 2019/01
coding : UTF-8
"""
from PyQt5.QtWidgets import QTreeWidgetItem


class TreeItem(QTreeWidgetItem):
    # TODO : Implement Tree Item
    def __init__(self, chapter_number, scene_number, description, parent=None):
        super(TreeItem, self).__init__(parent)
        self.index = (chapter_number, scene_number)
        self.description = description

