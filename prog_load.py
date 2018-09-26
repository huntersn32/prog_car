import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import Design_load  # Это конвертированный файл дизайна
import sqlite3
from datetime import datetime

class ExampleApp(QtWidgets.QMainWindow, Design_load.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле Design_load.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.loadbtnReis.clicked.connect(self.load_Db_reis) #Выполнить функцию load_Db_reis
        self.loadbtnCash.clicked.connect(self.load_Db_cash) #Выполнить функию cash

    def load_Db_reis(self):
        
        date_L = self.dateLoad.selectedDate() # дата загрузки
        date_L = date_L.toString('dd.MM.yyyy') # перевод в читаемый формат
        L = date_L
        country_load = self.cmbLoad.currentText() # страна загрузки
        date_U = self.dateUpload.selectedDate() # дата выгрузки
        date_U = date_U.toString('dd.MM.yyyy') # перевод в читаемый формат
        U = date_U
        country_upload = self.cmbUpload.currentText() # страна выгрузки
        car = self.cmbCarnumber.currentText() # № машины
        fio = self.cmbDriverfio.currentText() # ФИО водителя
        cash = self.lineCashdrive.text() # Стоимость перевозки
        val = self.cmbVal.currentText() # валюта
        pool = (date_L,country_load,date_U,country_upload,
                car,fio,cash,val)

        print(L)
        print(U)
       

        conn = sqlite3.connect("test.db") # или :memory: чтобы сохранить в RAM
        
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO roads(date_load,Country_load,date_upload,
Counry_upload,Car_number,Fraht,Fraht_val,Fio_driver)
                  VALUES (?,?,?,?,?,?,?,?)""",(date_L,country_load,
                                               date_U,country_upload,
                                               car,cash,val,fio)
                       )
                                 
        conn.commit()
        conn.close()

    def load_Db_cash(self):
        dateload = self.dateLoadCash.selectedDate() # Дата загрузки
        dateload = dateload.toString('dd.MM.yyy')
        carnumbercash = self.cmb_car_cash.currentText() # номер машины
        fiocash = self.fiocmbCash.currentText() # ФИО водителя
        casheur = self.cmbCashLoadEuro.text() # получено евро
        cahsrub = self.cmbCashLoadRub.text() # получено рублей
        spenteuro = self.cmbCashSpentEuro.text() # потрачено евро
        spentrub = self.cmbCashSpentRub.text() # потрачено руб
        cashKm = self.CashKm.text() # пройденный километраж
        grosscash = self.CashGross.text() # вес груза
        esp = int(grosscash)*0,4
        summa = (cashKm*esp)/100
        self.lcdCash.intValue(summa)
        print(summa)
        rashodDT = summa

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
 

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
