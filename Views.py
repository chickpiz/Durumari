"""
name : Views.py
author : chickpiz
date : 2019/01
coding : UTF-8
"""
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QTreeWidget
from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtWidgets import QHBoxLayout, QBoxLayout
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize


# Functions for convenience
def set_action(name, icon=None,shortcut=None):
    if icon is None:
        action = QAction(name)
        action.setShortcut(shortcut)
    else:
        action = QAction(icon, name)
        action.setShortcut(shortcut)
    return action


class ScriptEdit(QWidget):

    def __init__(self, parent=None):
        super(ScriptEdit, self).__init__(parent=parent)

        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)

        self.script_text = QTextEdit()
        self.source_text = QTextEdit()

        self.tab = QTabWidget()
        self.tab.addTab(self.script_text, 'Text')
        self.tab.addTab(self.source_text, 'Xml')

        self.act_change_tab = QAction(self)
        self.act_change_tab.setShortcut('Shift+Tab')
        self.addAction(self.act_change_tab)

        self.layout.addWidget(self.tab)


class SceneTree(QDockWidget):

    def __init__(self, parent=None):
        super(SceneTree, self).__init__(parent)

        self.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)

        self.centralwidget = QWidget(self)
        self.setWidget(self.centralwidget)

        self.layout = QBoxLayout(QBoxLayout.TopToBottom, self.centralwidget)

        self.tree = QTreeWidget()
        self.layout.addWidget(self.tree)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.btn_add = QPushButton('Add ..')
        self.layout.addWidget(self.btn_add)


class TreeDialog(QDialog):

    def __init__(self, parent=None):
        super(TreeDialog, self).__init__(parent)

        # Initialize dialog UI
        self.layout = QBoxLayout(QBoxLayout.TopToBottom)
        self.setLayout(self.layout)

        self.btn = QTextEdit()
        self.layout.addWidget(self.btn)


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)

        # Initialize UI
        self.setWindowTitle('Durumari')
        self.resize(800, 600)
        self.status_bar = self.statusBar()
        self.setStatusBar(self.status_bar)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout(self.central_widget)

        # Editor
        self.edit = ScriptEdit()
        self.layout.addWidget(self.edit)

        '''
        self.central_tab = QTabWidget()
        self.central_tab.addTab(ScriptEdit(), 'File 1')
        self.layout.addWidget(self.central_tab)
        '''

        # Scene Tree
        self.scn_tree = SceneTree(self)
        self.scn_tree.setMaximumSize(10000, 10000)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.scn_tree)

        # Tool Bar
        self.tool_bar = QToolBar()
        self.tool_bar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.addToolBar(Qt.LeftToolBarArea, self.tool_bar)

        self.act_toggle_tree = set_action('Toggle Tree', QIcon('toggle_tree.png'), 'Ctrl+T')
        self.tool_bar.addAction(self.act_toggle_tree)
        self.tool_bar.setIconSize(QSize(24, 24))
        self.addToolBarBreak()

        # Menu Bar
        self.main_menu = self.menuBar()

        # <-*- File Menu
        self.file_menu = self.main_menu.addMenu('&File')

        self.act_new = set_action('&New ..', shortcut='Ctrl+N')
        self.act_open = set_action('&Open', shortcut='Ctrl+O')
        self.act_save = set_action('&Save', shortcut='Ctrl+S')

        self.file_menu.addAction(self.act_new)
        self.file_menu.addAction(self.act_open)
        self.file_menu.addAction(self.act_save)
        self.file_menu.addSeparator()
        # File Menu -*->

        # <-*- Text Menu
        self.text_menu = self.main_menu.addMenu('&Text')

        self.act_font = set_action('Font', shortcut='Ctrl+Alt+F')

        self.text_menu.addAction(self.act_font)
        self.text_menu.addSeparator()
        # Text Menu -*->



