import os
import random
import sys
import platform
import subprocess
import win32gui
import win32con
import time
import random
import PyQt5
import pyautogui
import tkinter as tk

from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, QPushButton, 
                           QVBoxLayout, QWidget, QLabel, QTextEdit, QLineEdit,
                           QHBoxLayout, QTreeView, QFileSystemModel, QListView,
                           QSplitter, QStatusBar, QAction, QComboBox, QMessageBox,
                           QInputDialog, QFileDialog, QScrollArea, QProgressBar, QFrame,
                           QSizePolicy, QPushButton, QGridLayout)

from PyQt5.QtGui import (QIcon, QPixmap, QTextCursor, QColor, QFont, 
                       QTextCharFormat, QPainter, QPen, QImage, QPalette)
from PyQt5.QtCore import (Qt, QSize, QDir, QTimer, QPoint, QRect, 
                         QProcess, QProcessEnvironment, QEvent, QObject, QUrl)

from colorama import Fore, Back, init

init()

with open(f'cache-{random.randint(100000, 150000)}-{random.randint(100000, 150000)}-{random.randint(100000, 150000)}-{random.randint(100000, 150000)}-{random.randint(100000, 150000)}-{random.randint(100000, 150000)}', 'w', encoding='utf-8') as file:    
    file.write("{temp}\n")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}\n\n")
    file.write(f"THE NUMBER OF CACHE: {random.randint(100, 1000000)}\n")
    file.write("----------------------------------------------------\n\n")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")
    file.write(f"{random.randint(1000, 2000)}")



print(Fore.GREEN + "                     Delix BOOT Configurator" + Fore.RESET)

print(Fore.GREEN + "-----------------------------------------------------------------" + Fore.RESET)

print("Classic BOOT Theory     :                            Classic BOOT")

print("Ninja localhost BOOT    :                            Classic BOOT")

print("localhost theory        :                            Classic BOOT")

print("neoftech bash theory    :                            Classic BOOT")

print("Ninja server BOOT       :                            Classic BOOT")

print(Fore.GREEN + "-----------------------------------------------------------------" + Fore.RESET)

print(Fore.BLACK + Back.GREEN + "start classic" + Fore.RESET + Back.RESET + ": continue")

print(Fore.BLACK + Back.GREEN + "boot .show v2" + Fore.RESET + Back.RESET + ": view not classic boot")

print(Fore.BLACK + Back.GREEN + ".recovery .sh" + Fore.RESET + Back.RESET + ": delix recovery [ALPHA]")

print(Fore.BLACK + Back.GREEN + "any command  " + Fore.RESET + Back.RESET + ": continue")

print(Fore.GREEN + "-----------------------------------------------------------------" + Fore.RESET)



command = input("> ")



def check_required_files():

    required_files = [

        "main.py",

        "bin/",

        "bin/handlers/",

        "bin/handlers/CrashHandler.hand",

        "bin/handlers/error_handler.delixapp",

        "bin/handlers/Classic/",

        "bin/handlers/Classic/Handler.hand",

        "bin/packages/shlib3-build.pack",

        "bin/packages/shlib3-config.pack",

        "bin/xns31.dll",

        "mnt/",

        "mnt/delix/",

        "mnt/delix/launch/",

        "mnt/delix/launch/build",

        "mnt/delix/launch/build/delix.build-pack",

        "mnt/delix/launch/packages",

        "mnt/delix/launch/packages/python3.11.pack",

        "usr/",

        "usr/lib/",

        "usr/lib/systemd/",

        "usr/lib/systemd/usralt.dev.3",

        "usr/lib/systemd/passwd.0",

        "usr/lib/systemd/profile.1",

        "usr/share/",

        "usr/share/doc/",

        "usr/share/doc/profile.x",

        "usr/share/doc/passwd.2",

        "usr/share/doc/syslog.3",

    ]

    

    missing_files = []

    

    for file_path in required_files:

        if not os.path.exists(file_path):

            missing_files.append(file_path)

    

    return missing_files



if command == ".recovery .sh":

    print(Fore.BLUE + "> recovery mode" + Fore.RESET)

    yesorno = input("Continue? (y/n) ")

    if yesorno == "y" or "Y":

        os.system('cls')

        print("starting recovery")

        time.sleep(3)

        os.system('cls')



        root = tk.Tk()

        root.geometry("400x200")

        root.title("Recovery System")



        label = tk.Label(root, text="Ready for recovery", font=("Arial", 14))

        label.pack(pady=20)



        button = tk.Button(root, text="Start", font=("Arial", 12))

        button.pack(pady=10)



        stages = [

            "Diagnostic...",

            "Files Check-Up...",

            "Trying DelisxFiles in Emulator...",

            "Fixing Errors...",

            "Finishing..."

        ]



        def start_recovery():

            button.pack_forget()

            run_stage(0)



        def run_stage(index):

            if index < len(stages):

                label.config(text=stages[index])

                root.after(9000, lambda: run_stage(index + 1))

            else:

                label.config(text="Finished!\nStarting Delix...")

                root.after(2000, root.destroy)



        button.config(command=start_recovery)



        root.mainloop()





    else:

        print("")



if command == "boot .show v2":

    os.system('cls')

    print("[error] cannot found boot_variant_2.sh")

    time.sleep(2)

    print("[msg] starting classic")

    time.sleep(4)



if command == "start classic":

    os.system('cls')

    print("[SYSTEM] Checking required files...")

    time.sleep(1)

    

    missing_files = check_required_files()

    

    if missing_files:

        print("[ERROR] Missing critical files:")

        for file in missing_files:

            print(f" - {file}")

        print("\n" + Fore.RED + "Delix is crashed" + Fore.RESET)

        while True:  

            time.sleep(1)

    else:

        print("[SYSTEM] All required files found")

        print("[SYSTEM] connecting...")

        time.sleep(0.07)

        print("[SYSTEM] delisx.sh")

        time.sleep(0.07)

        print("[SYSTEM] boot.sh")

        time.sleep(0.07)

        print("[SYSTEM] main.py")

        time.sleep(0.07)

        print("[SYSTEM] os.py")

        time.sleep(0.07)

        print("[SYSTEM] emulator.exe")

        time.sleep(0.07)

        print("[SYSTEM] emulator.com")

        time.sleep(0.07)

        print("[SYSTEM] usr/")

        time.sleep(0.07)

        print("[SYSTEM] src/")

        time.sleep(0.07)

        print("[SYSTEM] bin/")

        time.sleep(0.07)

        print("[SYSTEM] sys/")

        time.sleep(0.07)

        print("[SYSTEM] usr/emulator.com")

        time.sleep(0.07)

        print("[SYSTEM] src/source.py")

        time.sleep(0.07)

        print("[SYSTEM] src/main.iso")

        time.sleep(0.07)

        print("[SYSTEM] bin/delix.iso")

        time.sleep(0.07)

        print("[SYSTEM] sys/system.iso")

        time.sleep(0.07)

        print("[SYSTEM] sys/system.py")

        time.sleep(0.07)

        print("[MESSAGE] Starting...")

        time.sleep(9)





class SplashScreen(QWidget):

    def __init__(self, on_loaded_callback):

        super().__init__()

        self.on_loaded_callback = on_loaded_callback

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setFixedSize(400, 300)

        self.setStyleSheet("background-color: #121212;")

        

        # Logo

        self.logo = QLabel(self)

        self.logo.setAlignment(Qt.AlignCenter)

        

        # Create simple logo

        pixmap = QPixmap(200, 200)

        pixmap.fill(Qt.transparent)

        painter = QPainter(pixmap)

        painter.setPen(QPen(QColor(0, 150, 255), 4))

        painter.drawEllipse(10, 10, 180, 180)

        painter.setFont(QFont("Arial", 24))

        painter.setPen(QColor(255, 255, 255))

        painter.drawText(QRect(10, 10, 180, 180), Qt.AlignCenter, "Delix")

        painter.end()

        

        self.logo.setPixmap(pixmap)

        

        # Progress bar

        self.progress = QProgressBar(self)

        self.progress.setRange(0, 100)

        self.progress.setTextVisible(False)

        self.progress.setStyleSheet("""

            QProgressBar {

                border: 2px solid #333;

                border-radius: 5px;

                background-color: #222;

                height: 10px;

            }

            QProgressBar::chunk {

                background-color: #0a84ff;

                border-radius: 3px;

            }

        """)

        

        # Version

        self.version = QLabel("Delix OS v0.1", self)

        self.version.setAlignment(Qt.AlignCenter)

        self.version.setStyleSheet("color: #666; font-size: 12px;")

        

        # Layout

        layout = QVBoxLayout()

        layout.addWidget(self.logo)

        layout.addWidget(self.progress)

        layout.addWidget(self.version)

        layout.setAlignment(self.logo, Qt.AlignCenter)

        layout.setAlignment(self.progress, Qt.AlignCenter)

        layout.setAlignment(self.version, Qt.AlignCenter)

        layout.setContentsMargins(40, 40, 40, 40)

        layout.setSpacing(20)

        self.setLayout(layout)

        

        # Center on screen

        screen = QApplication.primaryScreen().geometry()

        self.move(screen.center() - self.rect().center())

        

        # Timer for loading simulation

        self.timer = QTimer(self)

        self.timer.timeout.connect(self.update_progress)

        self.progress_value = 0

        self.timer.start(30)

    

    def update_progress(self):

        self.progress_value += 1

        self.progress.setValue(self.progress_value)

        

        if self.progress_value >= 100:

            self.timer.stop()

            QTimer.singleShot(300, self.finish_loading)

    

    def finish_loading(self):

        if self.on_loaded_callback:

            self.on_loaded_callback()

        self.close()



class TitleBar(QWidget):

    def __init__(self, parent):

        super().__init__(parent)

        self.parent = parent

        self.setFixedHeight(32)

        self.setStyleSheet("""

            background-color: #1e1e1e;

            border-radius: 8px 8px 0 0;

            border-bottom: 1px solid #0a0a0a;

        """)

        

        # Control buttons

        self.close_btn = QPushButton("×")

        self.min_btn = QPushButton("-")

        self.max_btn = QPushButton("□")

        

        btn_style = """

            QPushButton {

                color: #aaa;

                background-color: #333;

                border-radius: 4px;

                border: 1px solid #222;

                font-size: 14px;

                min-width: 16px;

                max-width: 16px;

                min-height: 16px;

                max-height: 16px;

                padding: 0px;

                margin-right: 8px;

            }

            QPushButton:hover {

                color: white;

            }

        """

        

        self.close_btn.setStyleSheet(btn_style + """

            QPushButton:hover { background-color: #e81123; border-color: #e81123; }

        """)

        self.min_btn.setStyleSheet(btn_style + """

            QPushButton:hover { background-color: #555; border-color: #444; }

        """)

        self.max_btn.setStyleSheet(btn_style + """

            QPushButton:hover { background-color: #555; border-color: #444; }

        """)

        

        # Window title

        self.title = QLabel(self.parent.windowTitle())

        self.title.setStyleSheet("""

            color: #ddd;

            font-family: Segoe UI;

            font-size: 12px;

            qproperty-alignment: AlignCenter;

        """)

        

        # Layout

        layout = QHBoxLayout()

        layout.addSpacing(10)

        layout.addWidget(self.close_btn)

        layout.addWidget(self.min_btn)

        layout.addWidget(self.max_btn)

        layout.addSpacing(10)

        layout.addWidget(self.title, 1)

        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)

        

        # Button events

        self.close_btn.clicked.connect(self.parent.close)

        self.min_btn.clicked.connect(self.parent.showMinimized)

        self.max_btn.clicked.connect(self.toggle_maximize)

        

        # For window moving

        self.old_pos = None

    

    def toggle_maximize(self):

        if self.parent.isMaximized():

            self.parent.showNormal()

        else:

            self.parent.showMaximized()

    

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.old_pos = event.globalPos()

    

    def mouseMoveEvent(self, event):

        if self.old_pos and not self.parent.isMaximized():

            delta = QPoint(event.globalPos() - self.old_pos)

            self.parent.move(self.parent.pos() + delta)

            self.old_pos = event.globalPos()

    

    def mouseReleaseEvent(self, event):

        self.old_pos = None



class BaseWindow(QMainWindow):

    def __init__(self, title):

        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowMinimizeButtonHint)

        self.setWindowTitle(title)

        self.setMinimumSize(400, 300)

        

        # Custom title bar

        self.title_bar = TitleBar(self)

        

        # Main content

        self.content_widget = QWidget()

        self.content_widget.setStyleSheet("""

            background-color: #252525;

            border-radius: 0 0 8px 8px;

        """)

        

        # Main layout

        main_layout = QVBoxLayout()

        main_layout.addWidget(self.title_bar)

        main_layout.addWidget(self.content_widget)

        main_layout.setSpacing(0)

        main_layout.setContentsMargins(0, 0, 0, 0)

        

        container = QWidget()

        container.setLayout(main_layout)

        self.setCentralWidget(container)

    

    def paintEvent(self, event):

        # Window shadow

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(QPen(QColor(0, 0, 0, 50), 8))

        painter.setBrush(Qt.NoBrush)

        painter.drawRoundedRect(QRect(4, 4, self.width()-8, self.height()-8), 8, 8)



class WindowEmbedder(QObject):

    def __init__(self, hwnd, parent):

        super().__init__(parent)

        self.hwnd = hwnd

        self.parent = parent

        

    def embed_window(self):

        try:

            style = win32gui.GetWindowLong(self.hwnd, win32con.GWL_STYLE)

            style &= ~(win32con.WS_CAPTION | win32con.WS_THICKFRAME | win32con.WS_MINIMIZEBOX | win32con.WS_MAXIMIZEBOX | win32con.WS_SYSMENU)

            win32gui.SetWindowLong(self.hwnd, win32con.GWL_STYLE, style)

            

            win32gui.SetParent(self.hwnd, int(self.parent.winId()))

            

            win32gui.MoveWindow(self.hwnd, 0, 32, self.parent.width(), self.parent.height()-32, True)

            return True

        except Exception as e:

            print(f"Failed to embed window: {e}")

            return False



class ExternalAppWrapper(BaseWindow):

    def __init__(self, file_path):

        super().__init__(os.path.basename(file_path))

        self.file_path = file_path

        self.process = None

        self.embedder = None

        self.target_hwnd = None

        self.resize_timer = None

        self.init_ui()

        

    def init_ui(self):

        self.container = QWidget()

        layout = QVBoxLayout()

        self.container.setLayout(layout)

        

        if self.is_internal_app(self.file_path):

            self.open_internal_app()

            return

        elif platform.system() == 'Windows' and self.file_path.lower().endswith('.exe'):

            self.launch_and_embed_exe()

        elif self.is_supported_image():

            self.show_image()

        elif self.is_supported_text():

            self.show_text()

        else:

            self.launch_external_app()

        

        self.content_widget.setLayout(QVBoxLayout())

        self.content_widget.layout().addWidget(self.container)

    

    def is_internal_app(self, file_path):

        internal_apps = {

            "Notes": NotesApp,

            "Finder": FinderApp,

            "Terminal": TerminalApp

        }

        app_name = os.path.basename(file_path)

        return app_name in internal_apps

    

    def open_internal_app(self):

        internal_apps = {

            "Notes": NotesApp,

            "Finder": FinderApp,

            "Terminal": TerminalApp

        }

        app_name = os.path.basename(self.file_path)

        app_class = internal_apps.get(app_name)

        

        if app_class:

            self.close()

            app_window = app_class()

            app_window.show()

    

    def is_supported_image(self):

        return self.file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))

    

    def is_supported_text(self):

        return self.file_path.lower().endswith(('.txt', '.log', '.md', '.csv', '.json'))

    

    def show_image(self):

        try:

            scroll = QScrollArea()

            label = QLabel()

            pixmap = QPixmap(self.file_path)

            if not pixmap.isNull():

                label.setPixmap(pixmap.scaledToWidth(800, Qt.SmoothTransformation))

                scroll.setWidget(label)

                self.container.layout().addWidget(scroll)

        except Exception as e:

            QMessageBox.warning(self, "Error", f"Failed to load image: {str(e)}")

    

    def show_text(self):

        try:

            text_edit = QTextEdit()

            text_edit.setStyleSheet("""

                QTextEdit {

                    background-color: #1e1e1e;

                    color: #e0e0e0;

                    border: none;

                    padding: 10px;

                    font-family: Consolas;

                    font-size: 12px;

                }

            """)

            with open(self.file_path, 'r', encoding='utf-8') as f:

                text_edit.setText(f.read())

            self.container.layout().addWidget(text_edit)

        except Exception as e:

            QMessageBox.warning(self, "Error", f"Failed to read file: {str(e)}")

    

    def launch_and_embed_exe(self):

        try:

            info_label = QLabel(f"Launching {os.path.basename(self.file_path)}...")

            info_label.setStyleSheet("color: #e0e0e0;")

            info_label.setAlignment(Qt.AlignCenter)

            self.container.layout().addWidget(info_label)

            

            self.process = QProcess(self)

            self.process.setProgram(self.file_path)

            self.process.startDetached()

            

            QTimer.singleShot(1000, self.find_and_embed_window)

            

        except Exception as e:

            QMessageBox.warning(self, "Error", f"Failed to launch EXE: {str(e)}")

    

    def find_and_embed_window(self):

        try:

            window_title = os.path.basename(self.file_path)

            self.target_hwnd = win32gui.FindWindow(None, window_title)

            

            if not self.target_hwnd:

                def callback(hwnd, hwnds):

                    if win32gui.IsWindowVisible(hwnd):

                        hwnds.append(hwnd)

                    return True

                

                hwnds = []

                win32gui.EnumWindows(callback, hwnds)

                if hwnds:

                    self.target_hwnd = hwnds[0]

            

            if self.target_hwnd:

                self.embedder = WindowEmbedder(self.target_hwnd, self)

                if self.embedder.embed_window():

                    self.resize_timer = QTimer(self)

                    self.resize_timer.timeout.connect(self.update_embedded_size)

                    self.resize_timer.start(100)

                    

                    for i in reversed(range(self.container.layout().count())): 

                        self.container.layout().itemAt(i).widget().setParent(None)

                else:

                    QTimer.singleShot(1000, self.find_and_embed_window)

            else:

                QTimer.singleShot(1000, self.find_and_embed_window)

                

        except Exception as e:

            print(f"Window embedding error: {e}")

            QTimer.singleShot(1000, self.find_and_embed_window)

    

    def update_embedded_size(self):

        if self.target_hwnd and win32gui.IsWindow(self.target_hwnd):

            try:

                win32gui.MoveWindow(self.target_hwnd, 0, 32, 

                                  self.width(), self.height()-32, True)

            except Exception as e:

                print(f"Resize error: {e}")

                self.resize_timer.stop()

        else:

            self.resize_timer.stop()

    

    def launch_external_app(self):

        if self.is_internal_app(self.file_path):

            self.open_internal_app()

            return

            

        try:

            if platform.system() == 'Windows':

                os.startfile(self.file_path)

            elif platform.system() == 'Darwin':

                subprocess.run(['open', self.file_path])

            else:

                subprocess.run(['xdg-open', self.file_path])

            self.close()

        except Exception as e:

            QMessageBox.warning(self, "Error", f"Failed to open file: {str(e)}")

    

    def closeEvent(self, event):

        if self.process and self.process.state() == QProcess.Running:

            self.process.terminate()

        if self.resize_timer and self.resize_timer.isActive():

            self.resize_timer.stop()

        super().closeEvent(event)



class NotesApp(BaseWindow):

    def __init__(self):

        super().__init__("Notes")

        self.setGeometry(300, 300, 600, 500)

        self.current_file = None

        self.init_ui()

    

    def init_ui(self):

        # Main text editor

        self.text_edit = QTextEdit()

        self.text_edit.setStyleSheet("""

            QTextEdit {

                background-color: #1e1e1e;

                color: #e0e0e0;

                border: none;

                padding: 15px;

                font-family: Consolas;

                font-size: 14px;

            }

        """)

        self.text_edit.setPlaceholderText("Type your notes here...")

        

        # Toolbar

        toolbar = QToolBar()

        toolbar.setStyleSheet("""

            QToolBar {

                background-color: #252525;

                border: none;

                border-bottom: 1px solid #0a0a0a;

                padding: 5px;

            }

            QPushButton {

                background-color: #333;

                color: #e0e0e0;

                border-radius: 4px;

                padding: 5px 10px;

                font-family: Segoe UI;

                font-size: 12px;

                border: 1px solid #222;

            }

            QPushButton:hover {

                background-color: #444;

            }

        """)

        

        # Buttons

        new_btn = QPushButton("New")

        new_btn.clicked.connect(self.new_file)

        

        open_btn = QPushButton("Open")

        open_btn.clicked.connect(self.open_file_dialog)

        

        save_btn = QPushButton("Save")

        save_btn.clicked.connect(self.save_file)

        

        save_as_btn = QPushButton("Save As")

        save_as_btn.clicked.connect(self.save_file_as)

        

        toolbar.addWidget(new_btn)

        toolbar.addWidget(open_btn)

        toolbar.addWidget(save_btn)

        toolbar.addWidget(save_as_btn)

        

        # Main layout

        layout = QVBoxLayout()

        layout.addWidget(toolbar)

        layout.addWidget(self.text_edit)

        layout.setSpacing(0)

        layout.setContentsMargins(0, 0, 0, 0)

        

        self.content_widget.setLayout(layout)

    

    def new_file(self):

        self.text_edit.clear()

        self.current_file = None

        self.title_bar.title.setText("Notes - Untitled")

    

    def open_file_dialog(self):

        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")

        if path:

            self.open_file(path)

    

    def open_file(self, path):

        try:

            with open(path, 'r', encoding='utf-8') as f:

                self.text_edit.setText(f.read())

            self.current_file = path

            self.title_bar.title.setText(f"Notes - {os.path.basename(path)}")

        except Exception as e:

            QMessageBox.warning(self, "Error", f"Failed to open file: {str(e)}")

    

    def save_file(self):

        if self.current_file:

            self._save_to_file(self.current_file)

        else:

            self.save_file_as()

    

    def save_file_as(self):

        path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")

        if path:

            self._save_to_file(path)

            self.current_file = path

            self.title_bar.title.setText(f"Notes - {os.path.basename(path)}")

    

    def _save_to_file(self, path):

        try:

            with open(path, 'w', encoding='utf-8') as f:

                f.write(self.text_edit.toPlainText())

            QMessageBox.information(self, "Success", "File saved successfully")

        except Exception as e:

            QMessageBox.warning(self, "Error", f"Failed to save file: {str(e)}")



class FinderApp(BaseWindow):

    def __init__(self):

        super().__init__("Finder")

        self.setGeometry(200, 200, 900, 600)

        self.init_ui()

    

    def init_ui(self):

        # File system model

        self.model = QFileSystemModel()

        self.model.setRootPath("")

        self.model.setFilter(QDir.AllEntries | QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)

        

        # Side panel (TreeView)

        self.tree_view = QTreeView()

        self.tree_view.setModel(self.model)

        self.tree_view.setHeaderHidden(True)

        self.tree_view.setAnimated(True)

        self.tree_view.setIndentation(15)

        self.tree_view.doubleClicked.connect(self.on_item_double_clicked)

        self.tree_view.setStyleSheet("""

            QTreeView {

                border-right: 1px solid #0a0a0a;

                background-color: #252525;

                color: #e0e0e0;

            }

            QTreeView::item {

                padding: 5px;

            }

            QTreeView::item:hover {

                background-color: #333;

            }

            QTreeView::item:selected {

                background-color: #0a84ff;

                color: white;

            }

        """)

        

        # Main panel (ListView)

        self.list_view = QListView()

        self.list_view.setModel(self.model)

        self.list_view.setViewMode(QListView.IconMode)

        self.list_view.setGridSize(QSize(100, 90))

        self.list_view.setIconSize(QSize(64, 64))

        self.list_view.doubleClicked.connect(self.on_item_double_clicked)

        self.list_view.setStyleSheet("""

            QListView {

                background-color: #1e1e1e;

                color: #e0e0e0;

            }

            QListView::item {

                color: #e0e0e0;

            }

            QListView::item:hover {

                background-color: #333;

            }

            QListView::item:selected {

                background-color: #0a84ff;

                color: white;

            }

        """)

        

        # Splitter

        splitter = QSplitter()

        splitter.addWidget(self.tree_view)

        splitter.addWidget(self.list_view)

        splitter.setSizes([200, 700])

        

        # Toolbar

        toolbar = QToolBar()

        toolbar.setIconSize(QSize(16, 16))

        toolbar.setStyleSheet("""

            QToolBar {

                background-color: #252525;

                border: none;

                border-bottom: 1px solid #0a0a0a;

                padding: 5px;

            }

            QToolButton {

                color: #e0e0e0;

                background: transparent;

                border: none;

            }

            QToolButton:hover {

                background-color: #333;

            }

        """)

        

        # Navigation buttons

        back_btn = QAction(QIcon.fromTheme("go-previous"), "Back", self)

        forward_btn = QAction(QIcon.fromTheme("go-next"), "Forward", self)

        toolbar.addAction(back_btn)

        toolbar.addAction(forward_btn)

        toolbar.addSeparator()

        

        # View button

        view_btn = QAction(QIcon.fromTheme("view-list-icons"), "View", self)

        toolbar.addAction(view_btn)

        

        # Path edit

        self.path_edit = QLineEdit()

        self.path_edit.setStyleSheet("""

            QLineEdit {

                background-color: #333;

                color: #e0e0e0;

                border: 1px solid #222;

                border-radius: 4px;

                padding: 5px;

            }

        """)

        self.path_edit.setPlaceholderText("Path...")

        self.path_edit.returnPressed.connect(self.navigate_to_path)

        toolbar.addWidget(self.path_edit)

        

        # Status bar

        self.status_bar = QStatusBar()

        self.status_bar.setStyleSheet("""

            QStatusBar {

                background-color: #252525;

                border-top: 1px solid #0a0a0a;

                padding: 3px;

                color: #aaa;

                font-size: 11px;

            }

        """)

        

        # Main layout

        layout = QVBoxLayout()

        layout.addWidget(toolbar)

        layout.addWidget(splitter)

        layout.addWidget(self.status_bar)

        layout.setSpacing(0)

        layout.setContentsMargins(0, 0, 0, 0)

        

        self.content_widget.setLayout(layout)

        

        # Set root path

        home_path = QDir.homePath()

        self.tree_view.setRootIndex(self.model.index(home_path))

        self.list_view.setRootIndex(self.model.index(home_path))

        self.path_edit.setText(home_path)

        self.status_bar.showMessage(f"Selected: {home_path}")

    

    def on_item_double_clicked(self, index):

        path = self.model.filePath(index)

        if os.path.isdir(path):

            self.list_view.setRootIndex(index)

            self.path_edit.setText(path)

            self.status_bar.showMessage(f"Selected: {path}")

        else:

            self.open_file(path)

    

    def navigate_to_path(self):

        path = self.path_edit.text()

        if os.path.exists(path):

            index = self.model.index(path)

            self.list_view.setRootIndex(index)

            self.tree_view.setExpanded(index, True)

            self.tree_view.setCurrentIndex(index)

            self.status_bar.showMessage(f"Selected: {path}")

        else:

            QMessageBox.warning(self, "Error", "Path does not exist")

    

    def open_file(self, file_path):

        if os.path.basename(file_path) in ["Notes", "Finder", "Terminal"]:

            app = ExternalAppWrapper(file_path)

            app.show()

        else:

            try:

                if platform.system() == 'Windows':

                    os.startfile(file_path)

                elif platform.system() == 'Darwin':

                    subprocess.run(['open', file_path])

                else:

                    subprocess.run(['xdg-open', file_path])

            except Exception as e:

                QMessageBox.warning(self, "Error", f"Failed to open file: {str(e)}")



class DelixBrowserApp(BaseWindow):

    def __init__(self):

        super().__init__("Delix Browser")

        self.setGeometry(200, 200, 1000, 700)

        self.init_ui()



    def init_ui(self):

        self.browser = QWebEngineView()

        self.browser.setUrl(QUrl("https://www.google.com"))



        self.url_bar = QLineEdit()

        self.url_bar.setPlaceholderText("Enter URL...")

        self.url_bar.returnPressed.connect(self.navigate_to_url)



        back_button = QPushButton("←")

        back_button.clicked.connect(self.browser.back)



        reload_button = QPushButton("⟳")

        reload_button.clicked.connect(self.browser.reload)



        top_bar = QHBoxLayout()

        top_bar.addWidget(back_button)

        top_bar.addWidget(reload_button)

        top_bar.addWidget(self.url_bar)



        layout = QVBoxLayout()

        layout.addLayout(top_bar)

        layout.addWidget(self.browser)

        layout.setContentsMargins(0, 0, 0, 0)



        self.content_widget.setLayout(layout)



    def navigate_to_url(self):

        url = self.url_bar.text()

        if not url.startswith("http"):

            url = "https://" + url

        self.browser.setUrl(QUrl(url))





class Slither(BaseWindow):

    def __init__(self):

        super().__init__("Delix Browser - Slither")

        self.setGeometry(200, 200, 1000, 700)

        self.init_ui()



    def init_ui(self):

        self.browser = QWebEngineView()

        self.browser.setUrl(QUrl("https://slither.io"))



        self.url_bar = QLineEdit()

        self.url_bar.setPlaceholderText("Enter URL...")

        self.url_bar.returnPressed.connect(self.navigate_to_url)



        back_button = QPushButton("←")

        back_button.clicked.connect(self.browser.back)



        reload_button = QPushButton("⟳")

        reload_button.clicked.connect(self.browser.reload)



        top_bar = QHBoxLayout()

        top_bar.addWidget(back_button)

        top_bar.addWidget(reload_button)

        top_bar.addWidget(self.url_bar)



        layout = QVBoxLayout()

        layout.addLayout(top_bar)

        layout.addWidget(self.browser)

        layout.setContentsMargins(0, 0, 0, 0)



        self.content_widget.setLayout(layout)



    def navigate_to_url(self):

        url = self.url_bar.text()

        if not url.startswith("http"):

            url = "https://" + url

        self.browser.setUrl(QUrl(url))



class CalculatorApp(BaseWindow):

    def __init__(self):

        super().__init__("Calculator")

        self.setGeometry(400, 400, 300, 400)

        self.init_ui()

    

    def init_ui(self):

        # Display

        self.display = QLineEdit()

        self.display.setReadOnly(True)

        self.display.setAlignment(Qt.AlignRight)

        self.display.setStyleSheet("""

            QLineEdit {

                background-color: #252525;

                color: #e0e0e0;

                border: 1px solid #333;

                border-radius: 5px;

                padding: 10px;

                font-size: 24px;

                margin-bottom: 10px;

            }

        """)

        

        # Buttons

        buttons = [

            '7', '8', '9', '/',

            '4', '5', '6', '*',

            '1', '2', '3', '-',

            '0', '.', '=', '+',

            'C', '⌫'

        ]

        

        # Create grid layout

        grid = QGridLayout()

        grid.setSpacing(10)

        

        # Add buttons to grid

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, button_text in zip(positions, buttons):

            btn = QPushButton(button_text)

            btn.setStyleSheet("""

                QPushButton {

                    background-color: #333;

                    color: #e0e0e0;

                    border-radius: 5px;

                    font-size: 18px;

                    padding: 10px;

                    border: 1px solid #222;

                }

                QPushButton:hover {

                    background-color: #444;

                }

                QPushButton:pressed {

                    background-color: #555;

                }

            """)

            btn.clicked.connect(self.on_button_click)

            grid.addWidget(btn, *position)

        

        # Main layout

        layout = QVBoxLayout()

        layout.addWidget(self.display)

        layout.addLayout(grid)

        layout.setContentsMargins(15, 15, 15, 15)

        

        self.content_widget.setLayout(layout)

    

    def on_button_click(self):

        sender = self.sender()

        text = sender.text()

        current_text = self.display.text()

        

        if text == 'C':

            self.display.clear()

        elif text == '⌫':

            self.display.setText(current_text[:-1])

        elif text == '=':

            try:

                result = eval(current_text)

                self.display.setText(str(result))

            except Exception:

                self.display.setText("Error")

        else:

            self.display.setText(current_text + text)



class TerminalApp(BaseWindow):

    def __init__(self):

        super().__init__("Delix Terminal")

        self.setGeometry(300, 300, 800, 600)

        self.username = "user"

        self.password = "4mdxi81nx"

        self.init_ui()

    

    def init_ui(self):

        # Font settings

        font = QFont("Fixedsys Excelsior 3.01", 12)

        

        # Output widget

        self.output = QTextEdit()

        self.output.setReadOnly(True)

        self.output.setFont(font)

        self.output.setStyleSheet("""

            QTextEdit {

                background-color: #282C35;

                color: #e0e0e0;

                border: none;

                padding: 26px;

                font-family: Fixedsys Excelsior 3.01;

            }

        """)

        

        # Input field

        self.input = QLineEdit()

        self.input.setFont(font)

        self.input.setStyleSheet("""

            QLineEdit {

                background-color: #1a1a1a;

                color: #e0e0e0;

                border: 1px solid #333;

                padding: 5px;

                font-family: Fixedsys Excelsior 3.01;

            }

        """)

        self.input.returnPressed.connect(self.execute_command)

        

        # Text formats

        self.red_format = QTextCharFormat()

        self.red_format.setForeground(QColor(255, 80, 80))

        

        self.white_format = QTextCharFormat()

        self.white_format.setForeground(QColor(230, 230, 230))

        

        self.green_format = QTextCharFormat()

        self.green_format.setForeground(QColor(80, 255, 80))

        

        # Main layout

        layout = QVBoxLayout()

        layout.addWidget(self.output)

        layout.addWidget(self.input)

        layout.setSpacing(0)

        layout.setContentsMargins(0, 0, 0, 0)

        

        self.content_widget.setLayout(layout)

        

        # Terminal initialization

        self.append_text("Delix Terminal\n", self.red_format)

        self.append_text("DaviSharp Corporation Copyritght\n", self.red_format)

        self.append_text("\n", self.white_format)

        self.append_text("[delix localhost ~] $ ", self.green_format)

    

    def execute_command(self):

        cmd = self.input.text()

        self.input.clear()

        

        self.append_text(f"{cmd}\n", self.white_format)

        

        if cmd == "neofetch":

            self.append_text("\n", self.white_format)

            self.append_text("\n", self.red_format)

            

            QTimer.singleShot(3000, lambda: [

                self.clear_screen(),

                self.append_text("neofetch\n", self.red_format),

                QTimer.singleShot(2000, lambda: [

                    self.clear_screen(),

                    self.show_kernel_info()

                ])

            ])

        elif cmd == "bash render .login":

            self.append_text("[bash] username: @user\n", self.white_format)

            self.append_text("[bash] password: 4mdxi81nx\n", self.white_format)

            self.append_text("[delix localhost ~] $ ", self.green_format)

        elif cmd.startswith("pkg install"):

            self.append_text("[pkg] error: 0000000x1\n", self.red_format)

            self.append_text("[delix localhost ~] $ ", self.green_format)

        elif cmd == "view-source .bt [ sh -c /s ]":

            self.append_text("""
$init codetype
codetype = 'SystemCode'

vol Str()
{
    setup(vol({
        RunningFunction boot(sys)
        {
            goto({
                DON D:/Delix/Managers/SystemManager %SysManFold% 
                RET D:/Delix/System10/Boot/dlxload.exe
                RET D:/Delix/System/RootBoot/loading.exe > D:/Delix/System10/Boot/dlxload.exe
                KAT D:/Delix/System/RootBoot/UEFI/ > D:/Delix/Boot/UEFI
                KAT D:/Delix/Root/ > .~/dev/env/
                KAT D:/Delix/Root/ > .~/bin/src/
                OBN D:/Delix/Root/Boot/xnws31.dll > sys.tp['Boot', 'BootLoader']
                OBN D:/Delix/Root/Packages/BootPackage.pak > .~/bootloader.exe
                OBN D:/Delix/Managers/ > l#env/trop/1.0/upd/esac.exe
                DON D:/Delix/Managers/BootManager/BootManager.exe
                DON %SysManFold%/RootPack/Runner/Boot/ [ dfg >> %SysManFold%0/control/bin/ ]
                DON %SysManFold%/BootConfig/UEFI_config
                DON %SysManFold%/BootConfig/UEFI.efi
                DON %SysManFold%/Boot/[BOOT_CONFIG].ini
                DON %SysManFold%/Boot/config/BOOT-BUILD.json
                DON %SysManFold%/Boot/dlxloader.exe
                DON %SysManFold%/Boot/dlxloader.dll
                DON %SysManFold%/Boot/dlxloader.ini
                DON %SysManFold%/Boot/loader.dll
                DON %SysManFold%/Boot/loader.ini
                DON %SysManFold%/Boot/dlxresume.exe
                DON %SysManFold%/Boot/dlxresume.dll
                DON %SysManFold%/Boot/dlxresume.inu
                DON %SysManFold%/Boot/resume.dll
                DON %SysManFold%/Boot/resume.ini
            })
        }
    }))
    $upload bash
    $start bash
    bash.code({
        echo ================
        echo  LOADING SCRIPT
        echo ================
        RET D:/Delix/System10/dlxload.exe
        RET D:/Delix/System10/dlxconf.dll > D:/Delix/System10/dlxload.exe
        lin D:/Delix/System10/dlxload.exe > bsh.g #gpp
        lin D:/Delix/System10/dlxload.exe /p 
        lin D:/Delix/System10/dlxresume.exe /p > bsh.g #gpp
    })
}\n\n""")

            self.append_text("[delix localhost ~] $ ", self.green_format)

        elif cmd == "clear":

            self.clear_screen()

            self.append_text("[delix localhost ~] $ ", self.green_format)

        elif cmd == "kr /i mdm sud optk -ilt":

            self.append_text("[PROMPT] If you add number to symbol app will quit: \n", self.white_format)

            self.append_text("[delix localhost ~] $ ", self.green_format)

            self.append_text("[delix localhost ~] $ ", self.green_format)

        elif cmd == "prct ninja":

            self.append_text("host: localhost\n", self.white_format)

            self.append_text("configurator: configuration_for_dlxrnl\n", self.white_format)

            self.append_text("root: [localhost ~]\n", self.white_format)

            self.append_text("kernel: delix kernel\n", self.white_format)

            self.append_text("self: java, ninja (maded in python), python\n", self.white_format)

            self.append_text("[delix localhost ~] $ ", self.green_format)

        elif cmd == "host ninja.localhost //localhost:00":

            self.append_text("\nhost: localhost\n", self.white_format)

            self.append_text("server: ninja\n", self.white_format)

            self.append_text("com1: com.ninja.pi/localhost/\n", self.white_format)

            self.append_text("igt: Java\n", self.white_format)

            self.append_text("sfv: Python\n", self.white_format)

            self.append_text("[delix localhost ~] $ ", self.green_format)

        elif cmd == "host ninja.localhost //localhost:00 .view_log:java_1:01.betafrt":

            self.append_text("""

public class main()

{

    Function var_lin_(clock) {

        var lin = clock;

        var con = clock;

        var linux = clock;

        var server = clock
    
    }

    var ninja = true;

    continue;

    var cins = true;

    public class avoid()

    {

        return main;

        return cins;

        public class injector_();

        {

            var i = false;

            var running = false;

            var ninja = true;

            return true;

            continue;

            public class davaS_trct()

            {

                var index = 1;

                var rootindex = 2;

                var linxcns = true;

                var cnst = true;

                var lib = true;

                var constraint = true;

                var build = true;\n

                var rejection = true;\n

                var osinn = true;\n

                var altk = true;\n

                var RunInNinja = true;\n

                var attack = false;\n

                var virus = false;\n

                var console_type_of_python_os = null;\n

                var security = true;\n

                var user = true;\n

                var uiApp = true;\n

                var consoleOS = false;\n

                var isThisPythonApp = true;\n

                var isThisNotSystem = true;\n

                var apps = true;\n

                var from_linux_base = false;\n

                var aprt = index + rootindex;\n

                var selection = true;\n

                var configuration = true;\n

                public class rig()\n

                {\n

                    Function post_kernel_status(attr) {\n

                        public static void main(String[] args) {\n

                            System.out.printIn(attr);\n

                        }\n

                    }\n

                    var path = "@root/%%"\n

                    var inRun = null;\n

                    var isThisSystem = false;\n

                    var posirfc = true;\n

                    var postfix = true;\n

                    var ninjaexe = true;\n

                    var model = true;\n

                    var for_rig = index + rootindex * 1 + 1 + 1 * 2 + 2 + 2 + 2\n

                    var root = path;\n

                    var host = "localhost";\n

                    var terminal = "Delix Terminal";\n

                    var cls_tabs = {\n

                        "Close": "$close",\n

                        "Remove": "$resize_for_remove",\n

                        "FullScreen": "$resize_for_full"\n

                    };\n

                    var letemfunction = true;\n

                    var letcmdfunctions = terminal, 1, 1, 0, 0, 1;\n

                    var pkginstallation = false;\n

                    var installation = false;\n

                    var linux = false;\n

                    var lin = true;\n

                    var lin_arg = true;\n

                    var syntax = true;\n

                    var syntaxInDelix = true;\n

                    var system_optimized_kernel = false;\n

                    var kernel_pl = "Python";\n

                    var kernel_status = "Not System";\n

                    post_kernel_status("kernel is NOT a optimized for launch system.")\n

                    SafeVarargs()\n

                }\n

            }\n

        }\n

        var_lin_(true)\n

    }\n

}\n



Class nktr(gt, irt) {\n

    post_kernel_status(gt="gogo")\n

    continue;\n

    return min {\n

        "min": gt;\n

        "class": irt;\n

    }\n

}\n



Function rig_main_ubd() {\n

    System.out.printIn("[CLASS]")\n

    rig.nktr(true, "main") {\n

        continue;\n

        return true;\n

    }\n

}\n



Class mjktr() {\n

    public class serjava(String, []) \n

    {\n

        var cmd_server = "localhost";\n

        var classic_server = 1\n

        public class ninja_ktr(main, [])\n

        {\n

            Function reserve() {\n

                System.out.printIn("reserved")\n

            }\n

            var dll = "*.dll: { The library file of executable program }"\n

        }\n

    }\n

}\n

                """, self.white_format)

            self.append_text("[delix localhost ~] $ ", self.green_format)

        elif cmd == "cnst (lib) dlxrnl.ef":

            self.append_text("\ndlxrnl.ef\n", self.white_format)

            self.append_text("     1. ef = 'Executable File'\n", self.white_format)

            self.append_text("     2. type = none\n", self.white_format)

            self.append_text("     3. self\n", self.white_format)

            self.append_text("          path.ef\n", self.white_format)

            self.append_text("          path.exe\n", self.white_format)

            self.append_text("          java.exe\n", self.white_format)

            self.append_text("          sublime.exe\n", self.white_format)

            self.append_text("          delix.py\n", self.white_format)

            self.append_text("          cnsletp\n", self.white_format)

            self.append_text("          dsvchthost.exe\n", self.white_format)

            self.append_text("     4. python\n", self.white_format)

            self.append_text("     5. dms code\n", self.white_format)

            self.append_text("[delix localhost ~] $ ", self.green_format)

        else:

            self.append_text("command not found\n", self.red_format)

            self.append_text("[delix localhost ~] $ ", self.green_format)

    

    def show_kernel_info(self):

        kernel_art = f"""
                            .#+                         root@{self.username}-irt-{self.password}                       
                            #:*=                        KERNEL: Delix Python Kernel                       
                           #**=%-                       DEV: Davi Sharp                       
                          *%-@#=@:                      Delux Public Python Kernel    
                         =@=#@@=%%.                     OS: Delix Python
                        =@#+@@@%-@%                     VERSION: 0.0.1              
                       :@@-%@@@@+*@#                    Console Version    
                      .@@*+@@@@@@-@@*                      
                     .%@%-@@@@@@@*=@@+                      
                     #@@=*@@@@@@@@=%@@-                     
                    #@@%=@@@@@@@@@%=@@@-                    
                   +@@@-%@@@@@@@@@@=#@@@:                   
                  =@@@#+@@@@@@@@@@@@=@@@%.                  
                 -@@@@-@@@@@@%%@@@@@++@@@%                  
                :@@@@++@@@@@# .%@@@@@-@@@@*                 
"""

        self.append_text(kernel_art, self.red_format)

        self.append_text("[delix localhost ~] $ ", self.green_format)

    

    def append_text(self, text, format=None):

        cursor = self.output.textCursor()

        cursor.movePosition(QTextCursor.End)

        

        if format:

            cursor.setCharFormat(format)

        

        cursor.insertText(text)

        self.output.setTextCursor(cursor)

        self.output.ensureCursorVisible()

    

    def clear_screen(self):

        self.output.clear()



class MacOSWindow(BaseWindow):

    def __init__(self):

        super().__init__("Delix Toshh")

        self.setGeometry(100, 100, 1200, 800)

        self.init_ui()

    

    def init_ui(self):

        # Dock panel

        self.dock = QToolBar("Dock")

        self.dock.setMovable(False)

        self.addToolBar(Qt.BottomToolBarArea, self.dock)

        self.dock.setStyleSheet("""

            QToolBar {

                background-color: rgba(30, 30, 30, 200);

                border-radius: 15px;

                padding: 10px;

                border: 1px solid rgba(0, 0, 0, 0.5);

                margin: 10px;

            }

            QToolButton {

                background: transparent;

                border: none;

            }

        """)

        

        # Create app icons

        apps = [

            {"name": "Finder", "icon": "bin/web/finder.png", "app": FinderApp},

            {"name": "Notes", "icon": "bin/web/notes.png", "app": NotesApp},

            {"name": "Calculator", "icon": "bin/web/calculator-icon-8175.png", "app": CalculatorApp},

            {"name": "Terminal", "icon": "bin/web/terminal.png", "app": TerminalApp},

            {"name": "Browser", "icon": "bin/web/browser.png", "app": DelixBrowserApp},

            {"name": "Slither", "icon": "bin/web/slither.jpg", "app": Slither},

        ]



        for app in apps:

            btn = QPushButton()

            if os.path.exists(app["icon"]):

                btn.setIcon(QIcon(app["icon"]))

            else:

                btn.setText(app["name"])

            btn.setIconSize(QSize(48, 48))

            btn.setFixedSize(60, 60)

            btn.setStyleSheet("""

                QPushButton {

                    border-radius: 10px;

                    padding: 5px;

                    background-color: rgba(60, 60, 60, 100);

                }

                QPushButton:hover {

                    background-color: rgba(80, 80, 80, 150);
                    border: rgba(255, 255, 255, 0)

                }

            """)

            btn.clicked.connect(lambda checked, a=app["app"]: self.open_app(a))

            self.dock.addWidget(btn)



        # Wallpaper label

        self.wallpaper_label = QLabel(self.content_widget)

        self.wallpaper_label.setAlignment(Qt.AlignCenter)

        self.wallpaper_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        

        # Set wallpaper

        self.set_wallpaper("bin/web/wallpaper.png")

        

        # Main layout

        layout = QVBoxLayout()

        layout.addWidget(self.wallpaper_label)

        layout.setContentsMargins(0, 0, 0, 0)

        self.content_widget.setLayout(layout)

        

        self.app_windows = []

    

    def set_wallpaper(self, image_path):

        if os.path.exists(image_path):

            self.wallpaper_path = image_path

            pixmap = QPixmap(image_path)

            self.wallpaper_label.setPixmap(pixmap.scaled(

                self.size(), 

                Qt.KeepAspectRatioByExpanding, 

                Qt.SmoothTransformation

            ))

        else:

            # Fallback to solid color

            self.wallpaper_label.setStyleSheet("background-color: #121212;")

    

    def resizeEvent(self, event):

        super().resizeEvent(event)

        if hasattr(self, 'wallpaper_path') and os.path.exists(self.wallpaper_path):

            pixmap = QPixmap(self.wallpaper_path)

            self.wallpaper_label.setPixmap(pixmap.scaled(

                self.size(), 

                Qt.KeepAspectRatioByExpanding, 

                Qt.SmoothTransformation

            ))

    

    def open_app(self, app_class):

        app_window = app_class()

        self.app_windows.append(app_window)

        app_window.show()



if __name__ == "__main__":

    missing_files = check_required_files()

    if missing_files:

        print(Fore.RED + "Critical files missing:" + Fore.RESET)

        for file in missing_files:

            print(f" - {file}")

        print(Fore.RED + "\nDelix is crashed" + Fore.RESET)

        while True:

            if True:

                print(Fore.RED + "\nDelix is crashed" + Fore.RESET)

                

            time.sleep(10)

            os.system('cls')

    else:

        app = QApplication(sys.argv)

        

        def show_main_window():

            window = MacOSWindow()

            window.showFullScreen()

        

        # Set dark palette

        dark_palette = QApplication.palette()

        dark_palette.setColor(QPalette.Window, QColor(30, 30, 30))

        dark_palette.setColor(QPalette.WindowText, QColor(220, 220, 220))

        dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))

        dark_palette.setColor(QPalette.AlternateBase, QColor(35, 35, 35))

        dark_palette.setColor(QPalette.ToolTipBase, QColor(220, 220, 220))

        dark_palette.setColor(QPalette.ToolTipText, QColor(220, 220, 220))

        dark_palette.setColor(QPalette.Text, QColor(220, 220, 220))

        dark_palette.setColor(QPalette.Button, QColor(50, 50, 50))

        dark_palette.setColor(QPalette.ButtonText, QColor(220, 220, 220))

        dark_palette.setColor(QPalette.BrightText, QColor(255, 0, 0))

        dark_palette.setColor(QPalette.Link, QColor(0, 150, 255))

        dark_palette.setColor(QPalette.Highlight, QColor(0, 120, 215))

        dark_palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))

        app.setPalette(dark_palette)



        # Show splash screen

        splash = SplashScreen(on_loaded_callback=show_main_window)

        splash.showFullScreen()

        

        sys.exit(app.exec_())