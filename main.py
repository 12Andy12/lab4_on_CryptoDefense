import os.path
import sqlite3
import sys
import time
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import game_support
import menu

app = QApplication(sys.argv)

Application = menu.Menu()
Application.show()

try:
    sys.exit(app.exec_())
except SystemExit:
    print('Closing Window...')