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

from random import shuffle

import game_support


class Game(QMainWindow):
    def __init__(self, players : game_support.player):
        super().__init__()
        uic.loadUi('game.ui', self)
        self.setWindowTitle("Poker")
        self.players = players
        self.current_player = self.players[0]
        self.money_label.setText(f"Бабосики: {self.current_player.money}")
        self.current_player_label.setText(f"{self.current_player.name}")
        self.origin_card_deck = self.gen_deck()
        self.card_deck = list(self.origin_card_deck.keys())
        shuffle(self.card_deck)
        self.current_table = -1
        self.decrypt_deck()
        self.deal_cards()
        self.table = self.deal_table()
        self.print_player_cards()
        self.btn_next.clicked.connect(self.next_player)




    def next_table(self):
        if self.current_table >= 4:
            return
        self.current_table +=1
        # card1 = self.get_card_name(self.encrypt_card(self.table[self.current_table], self.current_player))

    def open_table(self):
        if self.current_table >= 0:
            card1 = self.get_card_name(self.encrypt_card(self.table[0], self.current_player))
            self.table0.setPixmap(QPixmap("cards/" + card1 + ".jpg"))
        if self.current_table >= 1:
            card2 = self.get_card_name(self.encrypt_card(self.table[1], self.current_player))
            self.table1.setPixmap(QPixmap("cards/" + card2 + ".jpg"))
        if self.current_table >= 2:
            card3 = self.get_card_name(self.encrypt_card(self.table[2], self.current_player))
            self.table2.setPixmap(QPixmap("cards/" + card3 + ".jpg"))
        if self.current_table >= 3:
            card4 = self.get_card_name(self.encrypt_card(self.table[3], self.current_player))
            self.table3.setPixmap(QPixmap("cards/" + card4 + ".jpg"))
        if self.current_table >= 4:
            card5 = self.get_card_name(self.encrypt_card(self.table[4], self.current_player))
            self.table4.setPixmap(QPixmap("cards/" + card5 + ".jpg"))


    def next_player(self):
        for i in range(len(self.players)):
            if self.players[i] == self.current_player:
                if i == len(self.players) - 1:
                    self.next_table()
                    self.current_player = self.players[0]
                else:
                    self.current_player = self.players[i + 1]
                self.current_player_label.setText(f"{self.current_player.name}")
                self.print_player_cards()
                self.current_player_label.setText(f"{self.current_player.name}")
                self.money_label.setText(f"Бабосики: {self.current_player.money}")

                return

    def print_player_cards(self):
        card1 = self.get_card_name(self.encrypt_card(self.current_player.card1, self.current_player))
        card2 = self.get_card_name(self.encrypt_card(self.current_player.card2, self.current_player))
        self.hand1.setPixmap(QPixmap("cards/" + card1 + ".jpg"))
        self.hand2.setPixmap(QPixmap("cards/" + card2 + ".jpg"))
        self.hand1.setScaledContents(True)
        self.hand2.setScaledContents(True)
        self.open_table()

    def decrypt_deck(self):
        P = game_support.generate_simple_number(10**4, 10**9)
        for i in range(len(self.players)):
            self.players[i].P = P
            self.players[i].generate_parametrs()
            for j in range(len(self.card_deck)):
                self.card_deck[j] = self.players[i].decrypt(self.card_deck[j])
            shuffle(self.card_deck)

    def deal_cards(self):
        for i in range(len(self.players)):
            self.players[i].card1 = self.card_deck[0]
            self.players[i].card2 = self.card_deck[1]
            self.card_deck.remove(self.players[i].card1)
            self.card_deck.remove(self.players[i].card2)

    def deal_table(self):
        table = []
        for i in range(5):
            table.append(self.card_deck[0])
            self.card_deck.remove(self.card_deck[0])
            self.card_deck.remove(self.card_deck[0])
        return table

    def encrypt_card(self, c, player : game_support.player):
        card = c

        for i in range(len(self.players)):
            if (self.players[i] == player):
                continue
            card = self.players[i].encrypt(card)

        card = player.encrypt(card)
        print(card)
        return card

    def get_card_name(self, card):
        return self.origin_card_deck[card]

    def gen_deck(self):
        suits = ['P', 'K', 'C', 'B']
        faces = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'B', 'Q', 'K', 'A']

        cards = []
        for suit in suits:
            for face in faces:
                cards.append(str(face + suit))
        return {i: cards[i - 2] for i in range(2, 54)}