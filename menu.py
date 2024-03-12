import os.path
import sqlite3
import sys
import time
from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
import sqlite3

import game
import game_support


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui', self)
        self.setWindowTitle("Poker")
        self.tableStyle = "QTableWidget{\ngridline-color: #666666}"
        self.headerStyle = "::section:pressed {background-color: #323232;\nborder: none;}\n::section {background-color: #323232;\nborder: none;}"
        self.btnOpenStyle = ':hover{\nbackground-color: darkgreen;\n}\n:pressed{\nbackground-color: green;\n}\nQPushButton{border:none} '
        self.btnCloseStyle = ":hover{\nbackground-color: darkred;\n}\n:pressed{\nbackground-color: red;\n}\nQPushButton{border:none}"
        self.init_player_table()
        self.btn_start.clicked.connect(lambda: self.start_game())



    def init_player_table(self):
        self.tableWidget.horizontalHeader().setStyleSheet(self.headerStyle)
        self.tableWidget.setStyleSheet(self.tableStyle)
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setColumnCount(3)
        headers = ['игрок', 'бабосики', '']
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        self.tableWidget.setSpan(self.tableWidget.rowCount() - 1, 0, 1, 3)

        btnAdd = QPushButton()
        btnAdd.setText("+")
        # btnAdd.setIcon(QIcon("iconOpen.png"))
        # btnAdd.setIconSize(QSize(20, 20))
        btnAdd.setStyleSheet(self.btnOpenStyle)
        btnAdd.clicked.connect(self.add_player)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount() - 1, 0, btnAdd)

    def add_player(self):
        self.tableWidget.setCellWidget(self.tableWidget.rowCount() - 1, 0, None)
        btnDel = QPushButton()
        btnDel.setIcon(QIcon("iconClose.png"))
        btnDel.setIconSize(QSize(20, 20))
        btnDel.setStyleSheet(self.btnCloseStyle)
        btnDel.clicked.connect(lambda: self.DelCurrentRow())
        self.tableWidget.setSpan(self.tableWidget.rowCount() - 1, 0, 1, 1)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount() - 1, 2, btnDel)

        self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        self.tableWidget.setSpan(self.tableWidget.rowCount() - 1, 0, 1, 3)

        btnAdd = QPushButton()
        btnAdd.setText("+")
        # btnAdd.setIcon(QIcon("iconOpen.png"))
        # btnAdd.setIconSize(QSize(20, 20))
        btnAdd.setStyleSheet(self.btnOpenStyle)
        btnAdd.clicked.connect(self.add_player)
        self.tableWidget.setCellWidget(self.tableWidget.rowCount() - 1, 0, btnAdd)

        self.tableWidget.selectionModel().clear()

    def DelCurrentRow(self):
        row = self.tableWidget.currentRow()
        if row > -1:  # Если есть выделенная строка/элемент
            self.tableWidget.removeRow(row)
            self.tableWidget.selectionModel().clear()

    def start_game(self):
        players = []
        for i in range(self.tableWidget.rowCount()-1):
            current_player = game_support.player()
            current_player.name = self.tableWidget.item(i, 0).text()
            current_player.money = int(self.tableWidget.item(i, 1).text())
            print(f"{current_player.name} - {current_player.money}")
            players.append(current_player)
        self.gameWindow = game.Game(players)
        self.gameWindow.setGeometry(self.geometry())
        self.gameWindow.show()
        self.hide()


