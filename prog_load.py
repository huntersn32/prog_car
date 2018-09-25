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
        

    def load_Db_reis(self):
        
        date_L = self.dateLoad.selectedDate()
        date_L = date_L.toString('dd.MM.yyyy')
        L = date_L
        country_load = self.cmbLoad.currentText()
        date_U = self.dateUpload.selectedDate()
        date_U = date_U.toString('dd.MM.yyyy')
        U = date_U
        country_upload = self.cmbUpload.currentText()
        car = self.cmbCarnumber.currentText()
        fio = self.cmbDriverfio.currentText()
        cash = self.lineCashdrive.text()
        val = self.cmbVal.currentText()
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

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
 

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
