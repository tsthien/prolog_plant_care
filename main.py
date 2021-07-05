# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plantcare.ui'
#
# Created by: PyQt5 UI code generator 5.15.4


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import time
from threading import Thread
import requests
from time import localtime, strftime
import random


class Ui_plantcare(object):
    def __init__(self):
        self.df_plants = pd.DataFrame({'Name': [], 'Ws': []})
        self.df_weather = pd.DataFrame({'Date': [], 'Airhumidity': [], 'Temperature': [], 'Lightintensity': []})
        self.running = False

    def setupUi(self, plantcare):
        plantcare.setObjectName("plantcare")
        plantcare.resize(579, 623)
        self.centralwidget = QtWidgets.QWidget(plantcare)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(190, 0, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setWordWrap(False)
        self.Title.setObjectName("Title")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 30, 521, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.AddTitle = QtWidgets.QLabel(self.centralwidget)
        self.AddTitle.setGeometry(QtCore.QRect(30, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AddTitle.setFont(font)
        self.AddTitle.setObjectName("AddTitle")
        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setGeometry(QtCore.QRect(150, 100, 311, 20))
        self.nameInput.setObjectName("nameInput")
        self.WSInput = QtWidgets.QLineEdit(self.centralwidget)
        self.WSInput.setGeometry(QtCore.QRect(150, 170, 311, 20))
        self.WSInput.setText("")
        self.WSInput.setObjectName("WSInput")
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(40, 100, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.NameLabel.setFont(font)
        self.NameLabel.setObjectName("NameLabel")
        self.WSLabel = QtWidgets.QLabel(self.centralwidget)
        self.WSLabel.setGeometry(QtCore.QRect(40, 170, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.WSLabel.setFont(font)
        self.WSLabel.setObjectName("WSLabel")
        self.noteName = QtWidgets.QLabel(self.centralwidget)
        self.noteName.setGeometry(QtCore.QRect(150, 120, 311, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.noteName.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.noteName.setFont(font)
        self.noteName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.noteName.setAutoFillBackground(True)
        self.noteName.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.noteName.setWordWrap(True)
        self.noteName.setObjectName("noteName")
        self.noteWS = QtWidgets.QLabel(self.centralwidget)
        self.noteWS.setGeometry(QtCore.QRect(150, 200, 311, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(109, 109, 109))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.noteWS.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.noteWS.setFont(font)
        self.noteWS.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.noteWS.setAutoFillBackground(True)
        self.noteWS.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.noteWS.setWordWrap(True)
        self.noteWS.setObjectName("noteWS")
        self.submitBut = QtWidgets.QPushButton(self.centralwidget)
        self.submitBut.setGeometry(QtCore.QRect(170, 270, 101, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 150, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 150, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.submitBut.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.submitBut.setFont(font)
        self.submitBut.setObjectName("submitBut")
        self.Status = QtWidgets.QTextBrowser(self.centralwidget)
        self.Status.setGeometry(QtCore.QRect(130, 330, 351, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 151, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(134, 134, 134))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 151, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.Status.setPalette(palette)
        self.Status.setAutoFillBackground(True)
        self.Status.setObjectName("Status")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 360, 521, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.listPlants = QtWidgets.QTextBrowser(self.centralwidget)
        self.listPlants.setGeometry(QtCore.QRect(50, 390, 221, 181))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        self.listPlants.setPalette(palette)
        self.listPlants.setDocumentTitle("")
        self.listPlants.setObjectName("listPlants")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(290, 370, 20, 211))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.listLabel = QtWidgets.QLabel(self.centralwidget)
        self.listLabel.setGeometry(QtCore.QRect(130, 370, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.listLabel.setFont(font)
        self.listLabel.setObjectName("listLabel")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(390, 430, 75, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 150, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 150, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.startButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.startLabel = QtWidgets.QLabel(self.centralwidget)
        self.startLabel.setGeometry(QtCore.QRect(340, 370, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.startLabel.setFont(font)
        self.startLabel.setObjectName("startLabel")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(540, 370, 20, 211))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(20, 370, 20, 211))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(30, 570, 521, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.deleteBut = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBut.setGeometry(QtCore.QRect(340, 270, 101, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(150, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 17, 17))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 120, 215))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.deleteBut.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.deleteBut.setFont(font)
        self.deleteBut.setObjectName("deleteBut")
        self.timeStepLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeStepLabel.setGeometry(QtCore.QRect(320, 400, 61, 21))
        self.timeStepLabel.setObjectName("timeStepLabel")
        self.nameInput_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput_2.setGeometry(QtCore.QRect(390, 400, 81, 21))
        self.nameInput_2.setObjectName("nameInput_2")
        self.weatherOutput = QtWidgets.QTextBrowser(self.centralwidget)
        self.weatherOutput.setGeometry(QtCore.QRect(320, 500, 221, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        self.weatherOutput.setPalette(palette)
        self.weatherOutput.setDocumentTitle("")
        self.weatherOutput.setObjectName("weatherOutput")
        plantcare.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(plantcare)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 21))
        self.menubar.setObjectName("menubar")
        plantcare.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(plantcare)
        self.statusbar.setObjectName("statusbar")
        plantcare.setStatusBar(self.statusbar)

        self.retranslateUi(plantcare)
        QtCore.QMetaObject.connectSlotsByName(plantcare)

        self.submitBut.clicked.connect(self.pressSubmit)
        self.deleteBut.clicked.connect(self.pressDelete)
        self.startButton.clicked.connect(self.pressStart)
    
    def checkInput(self, namePlant, ws):
        # -1 ws not a number
        # -2 ws is negative
        # -3 this name existed
        # -4 name is empty
        # 0 OKE
        if namePlant == '':
            return -4
        try:
            ws = float(ws)
        except Exception as e:
            return -1
        if ws < 0:
            return -2
        if namePlant in self.df_plants['Name'].values:
            return -3
        
        return 0
    
    #Display list plants
    def displayList(self):
        self.listPlants.clear()
        for i in range(len(self.df_plants)):
            text = self.df_plants['Name'].iloc[-1-i] + ' ' + self.df_plants['Ws'].iloc[-1-i]

            word = '<span style=\" color: #0d1f45;\">%s</span>' % text
            self.listPlants.append(word)
    
    #PD tp csv
    def save_plants(self):
        self.df_plants.to_csv('./plants.csv', index=False)

    def save_weather(self):
        self.df_weather.to_csv('./weather.csv', index=False)
    
    #Time started
    def displayWeather(self):

        local_time = strftime("%Y-%m-%d %H:%M:%S", localtime())


        self.weatherOutput.clear()

        text = 'Started at: ' + str(local_time)
        word = '<span style=\" color: #0d1f45;\">%s</span>' % text
        self.weatherOutput.append(word)

                
    #Process export weather's data
    def run(self):
        while self.running == True:
            #Get weather info
            r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Moscow&appid=f3aee7c3b6bfb084ec625bc705b28192')
            jsonres = r.json()
            main = jsonres['main']
            #Get local time
            local_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
            ah = main['humidity']
            tempe = round(main['temp'] - 273.15, 1)
            if (jsonres['weather'][0]['main'] == 'Clear'):
                light = random.randint(1000, 2000)
            else:
                light = random.randint(500, 1000)
            new_row = {'Date': [local_time], 'Airhumidity': [ah], 'Temperature': [tempe], 'Lightintensity': [light]}
            
            self.df_weather = pd.DataFrame(new_row)
            print(self.df_weather.tail(5))
            self.save_weather()
            
            #Timestep
            timeStep = self.nameInput_2.text()
            try:
                timeStep = float(timeStep)
            except Exception as e:
                timeStep = 60
            if timeStep < 0:
                return 60

            time.sleep(timeStep)

    def pressSubmit(self):
        #Check input
        print(self.nameInput.text(), self.WSInput.text())
        check = self.checkInput(self.nameInput.text(), self.WSInput.text())
        if check == -1:
            self.Status.setText('Water storage must be a number!!!')
            self.Status.setStyleSheet("color: #ff0000")
        elif check == -2:
            self.Status.setText('Water storage must be a non-negative number!!!')
            self.Status.setStyleSheet("color: #ff0000")
        elif check == -3:
            self.Status.setText('This name was existed!!!')
            self.Status.setStyleSheet("color: #ff0000")
        elif check == -4:
            self.Status.setText('Name is empty!!!')
            self.Status.setStyleSheet("color: #ff0000")
        elif check == 0:
            #OKE
            new_row = {'Name':self.nameInput.text(), 'Ws':self.WSInput.text()}
            self.df_plants = self.df_plants.append(new_row, ignore_index=True)
            self.displayList()

            self.Status.setText(self.nameInput.text() + ' was added.')
            self.Status.setStyleSheet("color: #29891a")
        self.save_plants()
        
    def pressDelete(self):
        #Input oke then delete
        if self.nameInput.text() in self.df_plants['Name'].values:

            self.Status.setText(self.nameInput.text() + ' was deleted.')
            self.Status.setStyleSheet("color: #29891a")

            self.df_plants.drop(self.df_plants.index[self.df_plants['Name'] == self.nameInput.text()], inplace = True)
            self.df_plants = self.df_plants.reset_index(drop=True)

            self.displayList()

        else:

            self.Status.setText('Name is not exist!!!')
            self.Status.setStyleSheet("color: #ff0000")

        self.save_plants()


    def pressStart(self):
        self.running = not self.running
        if self.running == True:
            self.displayWeather()
            self.startButton.setText("RUNNING")
            self.startButton.setStyleSheet("color: #ff0000")
            #New thread for run function
            t1 = Thread(target=self.run, args=(), daemon=True)
            t1.start()

            
        else:
            self.startButton.setText("START")
            self.startButton.setStyleSheet("color: #009600")


        
        print("Click start/stop")
    

    def retranslateUi(self, plantcare):
        _translate = QtCore.QCoreApplication.translate
        plantcare.setWindowTitle(_translate("plantcare", "plantcare"))
        self.Title.setText(_translate("plantcare", "PLANT CARE"))
        self.AddTitle.setText(_translate("plantcare", "Add a new plant:"))
        self.NameLabel.setText(_translate("plantcare", "Name:"))
        self.WSLabel.setText(_translate("plantcare", "Water storage:"))
        self.noteName.setText(_translate("plantcare", " Name can be the type of tree, and the name must be unique, you will probably get a warning that the name already exists."))
        self.noteWS.setText(_translate("plantcare", " Water storage is a non-negative number,this value will gradually decrease depending on weather conditions, when this index is zero, the plant will need to be watered."))
        self.submitBut.setText(_translate("plantcare", "SUBMIT"))
        self.Status.setHtml(_translate("plantcare", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Status...</p></body></html>"))
        self.listPlants.setHtml(_translate("plantcare", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.listLabel.setText(_translate("plantcare", "List plants:"))
        self.startButton.setText(_translate("plantcare", "START"))
        self.startLabel.setText(_translate("plantcare", "Start receiving notifications:"))
        self.deleteBut.setText(_translate("plantcare", "DELETE"))
        self.timeStepLabel.setText(_translate("plantcare", "Time step(s):"))
        self.weatherOutput.setHtml(_translate("plantcare", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    plantcare = QtWidgets.QMainWindow()
    ui = Ui_plantcare()
    ui.setupUi(plantcare)
    plantcare.show()
    sys.exit(app.exec_())
