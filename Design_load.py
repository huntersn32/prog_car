# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/house/prog/Design_load.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 633)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/truck.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(50, 50))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateLoadcash = QtWidgets.QTabWidget(self.centralwidget)
        self.dateLoadcash.setGeometry(QtCore.QRect(10, 10, 781, 521))
        self.dateLoadcash.setIconSize(QtCore.QSize(40, 40))
        self.dateLoadcash.setObjectName("dateLoadcash")
        self.TabReis = QtWidgets.QWidget()
        self.TabReis.setObjectName("TabReis")
        self.loadbtnReis = QtWidgets.QPushButton(self.TabReis)
        self.loadbtnReis.setGeometry(QtCore.QRect(600, 390, 161, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loadbtnReis.setIcon(icon1)
        self.loadbtnReis.setIconSize(QtCore.QSize(40, 40))
        self.loadbtnReis.setObjectName("loadbtnReis")
        self.cmbLoad = QtWidgets.QComboBox(self.TabReis)
        self.cmbLoad.setGeometry(QtCore.QRect(250, 40, 111, 22))
        self.cmbLoad.setObjectName("cmbLoad")
        self.cmbLoad.addItem("")
        self.cmbLoad.addItem("")
        self.cmbLoad.addItem("")
        self.cmbLoad.addItem("")
        self.cmbLoad.addItem("")
        self.cmbLoad.addItem("")
        self.label = QtWidgets.QLabel(self.TabReis)
        self.label.setGeometry(QtCore.QRect(50, 20, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.TabReis)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.TabReis)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 111, 16))
        self.label_3.setObjectName("label_3")
        self.cmbUpload = QtWidgets.QComboBox(self.TabReis)
        self.cmbUpload.setGeometry(QtCore.QRect(250, 240, 111, 22))
        self.cmbUpload.setObjectName("cmbUpload")
        self.cmbUpload.addItem("")
        self.cmbUpload.addItem("")
        self.cmbUpload.addItem("")
        self.cmbUpload.addItem("")
        self.cmbUpload.addItem("")
        self.cmbUpload.addItem("")
        self.label_4 = QtWidgets.QLabel(self.TabReis)
        self.label_4.setGeometry(QtCore.QRect(250, 220, 121, 16))
        self.label_4.setObjectName("label_4")
        self.cmbCarnumber = QtWidgets.QComboBox(self.TabReis)
        self.cmbCarnumber.setGeometry(QtCore.QRect(250, 100, 141, 22))
        self.cmbCarnumber.setObjectName("cmbCarnumber")
        self.cmbCarnumber.addItem("")
        self.cmbCarnumber.addItem("")
        self.cmbDriverfio = QtWidgets.QComboBox(self.TabReis)
        self.cmbDriverfio.setGeometry(QtCore.QRect(410, 100, 241, 22))
        self.cmbDriverfio.setObjectName("cmbDriverfio")
        self.cmbDriverfio.addItem("")
        self.cmbDriverfio.addItem("")
        self.lineCashdrive = QtWidgets.QLineEdit(self.TabReis)
        self.lineCashdrive.setGeometry(QtCore.QRect(420, 240, 141, 22))
        self.lineCashdrive.setObjectName("lineCashdrive")
        self.label_5 = QtWidgets.QLabel(self.TabReis)
        self.label_5.setGeometry(QtCore.QRect(420, 220, 141, 16))
        self.label_5.setObjectName("label_5")
        self.cmbVal = QtWidgets.QComboBox(self.TabReis)
        self.cmbVal.setGeometry(QtCore.QRect(570, 240, 51, 22))
        self.cmbVal.setObjectName("cmbVal")
        self.cmbVal.addItem("")
        self.cmbVal.addItem("")
        self.cmbVal.addItem("")
        self.dateLoad = QtWidgets.QCalendarWidget(self.TabReis)
        self.dateLoad.setGeometry(QtCore.QRect(10, 40, 208, 149))
        self.dateLoad.setSelectedDate(QtCore.QDate(2018, 9, 12))
        self.dateLoad.setObjectName("dateLoad")
        self.dateUpload = QtWidgets.QCalendarWidget(self.TabReis)
        self.dateUpload.setGeometry(QtCore.QRect(10, 240, 208, 149))
        self.dateUpload.setSelectedDate(QtCore.QDate(2018, 9, 21))
        self.dateUpload.setGridVisible(False)
        self.dateUpload.setObjectName("dateUpload")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/world.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dateLoadcash.addTab(self.TabReis, icon2, "")
        self.TabCash = QtWidgets.QWidget()
        self.TabCash.setObjectName("TabCash")
        self.label_6 = QtWidgets.QLabel(self.TabCash)
        self.label_6.setGeometry(QtCore.QRect(60, 20, 101, 16))
        self.label_6.setObjectName("label_6")
        self.dateLoadCash = QtWidgets.QCalendarWidget(self.TabCash)
        self.dateLoadCash.setGeometry(QtCore.QRect(10, 40, 208, 149))
        self.dateLoadCash.setObjectName("dateLoadCash")
        self.cmb_car_cash = QtWidgets.QComboBox(self.TabCash)
        self.cmb_car_cash.setGeometry(QtCore.QRect(230, 40, 151, 22))
        self.cmb_car_cash.setObjectName("cmb_car_cash")
        self.cmb_car_cash.addItem("")
        self.cmb_car_cash.addItem("")
        self.fiocmbCash = QtWidgets.QComboBox(self.TabCash)
        self.fiocmbCash.setGeometry(QtCore.QRect(390, 40, 231, 22))
        self.fiocmbCash.setObjectName("fiocmbCash")
        self.fiocmbCash.addItem("")
        self.fiocmbCash.addItem("")
        self.label_7 = QtWidgets.QLabel(self.TabCash)
        self.label_7.setGeometry(QtCore.QRect(230, 80, 101, 16))
        self.label_7.setObjectName("label_7")
        self.cmbCashLoadEuro = QtWidgets.QLineEdit(self.TabCash)
        self.cmbCashLoadEuro.setGeometry(QtCore.QRect(230, 100, 113, 22))
        self.cmbCashLoadEuro.setObjectName("cmbCashLoadEuro")
        self.label_8 = QtWidgets.QLabel(self.TabCash)
        self.label_8.setGeometry(QtCore.QRect(390, 80, 101, 16))
        self.label_8.setObjectName("label_8")
        self.cmbCashLoadRub = QtWidgets.QLineEdit(self.TabCash)
        self.cmbCashLoadRub.setGeometry(QtCore.QRect(390, 100, 113, 22))
        self.cmbCashLoadRub.setObjectName("cmbCashLoadRub")
        self.label_9 = QtWidgets.QLabel(self.TabCash)
        self.label_9.setGeometry(QtCore.QRect(230, 140, 111, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.TabCash)
        self.label_10.setGeometry(QtCore.QRect(390, 140, 111, 16))
        self.label_10.setObjectName("label_10")
        self.cmbCashSpentEuro = QtWidgets.QLineEdit(self.TabCash)
        self.cmbCashSpentEuro.setGeometry(QtCore.QRect(230, 160, 113, 22))
        self.cmbCashSpentEuro.setObjectName("cmbCashSpentEuro")
        self.cmbCashSpentRub = QtWidgets.QLineEdit(self.TabCash)
        self.cmbCashSpentRub.setGeometry(QtCore.QRect(390, 160, 113, 22))
        self.cmbCashSpentRub.setObjectName("cmbCashSpentRub")
        self.loadbtnCash = QtWidgets.QPushButton(self.TabCash)
        self.loadbtnCash.setGeometry(QtCore.QRect(590, 400, 171, 51))
        self.loadbtnCash.setIcon(icon1)
        self.loadbtnCash.setIconSize(QtCore.QSize(40, 40))
        self.loadbtnCash.setObjectName("loadbtnCash")
        self.label_11 = QtWidgets.QLabel(self.TabCash)
        self.label_11.setGeometry(QtCore.QRect(20, 220, 161, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.TabCash)
        self.label_12.setGeometry(QtCore.QRect(200, 220, 101, 16))
        self.label_12.setObjectName("label_12")
        self.CashKm = QtWidgets.QLineEdit(self.TabCash)
        self.CashKm.setGeometry(QtCore.QRect(20, 240, 113, 22))
        self.CashKm.setObjectName("CashKm")
        self.CashGross = QtWidgets.QLineEdit(self.TabCash)
        self.CashGross.setGeometry(QtCore.QRect(200, 240, 113, 22))
        self.CashGross.setObjectName("CashGross")
        self.lcdCash = QtWidgets.QLCDNumber(self.TabCash)
        self.lcdCash.setGeometry(QtCore.QRect(330, 230, 111, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lcdCash.setFont(font)
        self.lcdCash.setMidLineWidth(0)
        self.lcdCash.setSmallDecimalPoint(False)
        self.lcdCash.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdCash.setProperty("intValue", 0)
        self.lcdCash.setObjectName("lcdCash")
        self.label_13 = QtWidgets.QLabel(self.TabCash)
        self.label_13.setGeometry(QtCore.QRect(330, 210, 121, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.TabCash)
        self.label_14.setGeometry(QtCore.QRect(460, 210, 91, 16))
        self.label_14.setObjectName("label_14")
        self.lcd_euro_lost = QtWidgets.QLCDNumber(self.TabCash)
        self.lcd_euro_lost.setGeometry(QtCore.QRect(460, 230, 91, 31))
        self.lcd_euro_lost.setObjectName("lcd_euro_lost")
        self.label_15 = QtWidgets.QLabel(self.TabCash)
        self.label_15.setGeometry(QtCore.QRect(570, 210, 81, 16))
        self.label_15.setObjectName("label_15")
        self.lcd_rub_lost = QtWidgets.QLCDNumber(self.TabCash)
        self.lcd_rub_lost.setGeometry(QtCore.QRect(570, 230, 81, 31))
        self.lcd_rub_lost.setObjectName("lcd_rub_lost")
        self.label_16 = QtWidgets.QLabel(self.TabCash)
        self.label_16.setGeometry(QtCore.QRect(20, 280, 81, 16))
        self.label_16.setObjectName("label_16")
        self.zp_cash = QtWidgets.QLineEdit(self.TabCash)
        self.zp_cash.setGeometry(QtCore.QRect(20, 300, 113, 22))
        self.zp_cash.setObjectName("zp_cash")
        self.label_17 = QtWidgets.QLabel(self.TabCash)
        self.label_17.setGeometry(QtCore.QRect(530, 80, 59, 14))
        self.label_17.setObjectName("label_17")
        self.curs_cash = QtWidgets.QLineEdit(self.TabCash)
        self.curs_cash.setGeometry(QtCore.QRect(530, 100, 91, 22))
        self.curs_cash.setObjectName("curs_cash")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/banknote.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dateLoadcash.addTab(self.TabCash, icon3, "")
        self.TabDriver = QtWidgets.QWidget()
        self.TabDriver.setObjectName("TabDriver")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dateLoadcash.addTab(self.TabDriver, icon4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.dateLoadcash.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Внесение данных в базу учета"))
        self.loadbtnReis.setText(_translate("MainWindow", "Внести данные"))
        self.cmbLoad.setItemText(0, _translate("MainWindow", "Россия"))
        self.cmbLoad.setItemText(1, _translate("MainWindow", "Греция"))
        self.cmbLoad.setItemText(2, _translate("MainWindow", "Италия"))
        self.cmbLoad.setItemText(3, _translate("MainWindow", "Болгария"))
        self.cmbLoad.setItemText(4, _translate("MainWindow", "Румыния"))
        self.cmbLoad.setItemText(5, _translate("MainWindow", "Чехия"))
        self.label.setText(_translate("MainWindow", "Дата загрузки"))
        self.label_2.setText(_translate("MainWindow", "Страна загрузки"))
        self.label_3.setText(_translate("MainWindow", "Дата выгрузки"))
        self.cmbUpload.setItemText(0, _translate("MainWindow", "Россия"))
        self.cmbUpload.setItemText(1, _translate("MainWindow", "Греция"))
        self.cmbUpload.setItemText(2, _translate("MainWindow", "Италия"))
        self.cmbUpload.setItemText(3, _translate("MainWindow", "Румыния"))
        self.cmbUpload.setItemText(4, _translate("MainWindow", "Болгария"))
        self.cmbUpload.setItemText(5, _translate("MainWindow", "Чехия"))
        self.label_4.setText(_translate("MainWindow", "Страна выгрузки"))
        self.cmbCarnumber.setItemText(0, _translate("MainWindow", "М416ОС / АМ 4275"))
        self.cmbCarnumber.setItemText(1, _translate("MainWindow", "М519НЕ / АМ 3711"))
        self.cmbDriverfio.setItemText(0, _translate("MainWindow", "Маслов Андрей Васильевич"))
        self.cmbDriverfio.setItemText(1, _translate("MainWindow", "Поснов Владимир Михайлович"))
        self.label_5.setText(_translate("MainWindow", "Стоимость перевозки"))
        self.cmbVal.setItemText(0, _translate("MainWindow", "RUB"))
        self.cmbVal.setItemText(1, _translate("MainWindow", "EUR"))
        self.cmbVal.setItemText(2, _translate("MainWindow", "USD"))
        self.dateLoadcash.setTabText(self.dateLoadcash.indexOf(self.TabReis), _translate("MainWindow", "Рейс"))
        self.label_6.setText(_translate("MainWindow", "Дата загрузки"))
        self.cmb_car_cash.setItemText(0, _translate("MainWindow", "М416ОС / АМ 4275"))
        self.cmb_car_cash.setItemText(1, _translate("MainWindow", "М519НЕ / АМ 3711"))
        self.fiocmbCash.setItemText(0, _translate("MainWindow", "Маслов Андрей Васильевич"))
        self.fiocmbCash.setItemText(1, _translate("MainWindow", "Поснов Владимир Михайлович"))
        self.label_7.setText(_translate("MainWindow", "Получено EURO"))
        self.label_8.setText(_translate("MainWindow", "Получено RUB"))
        self.label_9.setText(_translate("MainWindow", "Потрачено EURO"))
        self.label_10.setText(_translate("MainWindow", "Потрачено RUB"))
        self.loadbtnCash.setText(_translate("MainWindow", "Ввести данные"))
        self.label_11.setText(_translate("MainWindow", "Пройденый километраж"))
        self.label_12.setText(_translate("MainWindow", "Вес груза, тонн"))
        self.label_13.setText(_translate("MainWindow", "Расход  топлива л."))
        self.label_14.setText(_translate("MainWindow", "Остаток EURO"))
        self.label_15.setText(_translate("MainWindow", "Остаток RUB"))
        self.label_16.setText(_translate("MainWindow", "ЗП за рейс"))
        self.label_17.setText(_translate("MainWindow", "Курс EURO"))
        self.dateLoadcash.setTabText(self.dateLoadcash.indexOf(self.TabCash), _translate("MainWindow", "Расходы"))
        self.dateLoadcash.setTabText(self.dateLoadcash.indexOf(self.TabDriver), _translate("MainWindow", "Водители"))

