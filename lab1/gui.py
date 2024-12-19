import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QListWidgetItem
from ui_mainwindow import Ui_MainWindow
from lab1 import setup_database, create_session, NationalNames, StateNames
from lab1_defs import (
    add_national_name, add_state_name, get_first_50_national_names, get_first_50_state_names,
    delete_national_name, delete_state_name, search_national_names_by_name, search_state_names_by_name
)
engine = setup_database("sqlite:///database.sqlite")
session = create_session(engine)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_to_national_names)
        self.ui.pushButton_2.clicked.connect(self.add_to_state_names)
        self.ui.pushButton_3.clicked.connect(self.show_top_50_national_names)
        self.ui.pushButton_4.clicked.connect(self.delete_national_name_by_id)
        self.ui.pushButton_5.clicked.connect(self.search_state_names)
        self.ui.pushButton_6.clicked.connect(self.search_national_names)
        self.ui.pushButton_7.clicked.connect(self.show_top_50_state_names)
        self.ui.pushButton_8.clicked.connect(self.delete_state_name_by_id)
        self.ui.listWidget.itemClicked.connect(self.f)
        self.ui.listWidget_2.itemClicked.connect(self.f)

    def add_to_national_names(self):
        name = self.ui.lineEdit.text()
        year = self.ui.lineEdit_2.text()
        gender = self.ui.lineEdit_3.text()
        count = self.ui.lineEdit_4.text()

        if name and year and gender and count:
            try:
                year = int(year)
                count = int(count)
                add_national_name(name, year, gender, count)
                QMessageBox.information(self, "Успех", f"Имя '{name}' добавлено в NationalNames.")
            except ValueError:
                QMessageBox.warning(self, "Ошибка", "Год и количество должны быть числами.")
        else:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля.")

    def add_to_state_names(self):
        name = self.ui.lineEdit.text()
        year = self.ui.lineEdit_2.text()
        gender = self.ui.lineEdit_3.text()
        state = self.ui.lineEdit_5.text()
        count = self.ui.lineEdit_4.text()

        if name and year and gender and state and count:
            try:
                year = int(year)
                count = int(count)
                add_state_name(name, year, gender, state, count)
                QMessageBox.information(self, "Успех", f"Имя '{name}' добавлено в StateNames.")
            except ValueError:
                QMessageBox.warning(self, "Ошибка", "Год и количество должны быть числами.")
        else:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля.")

    def show_top_50_national_names(self):
        names = get_first_50_national_names()
        self.ui.listWidget_2.clear() 
        for name in names:
            item = QListWidgetItem(f"ID: {name.Id}, Name: {name.Name}, Year: {name.Year}, Gender: {name.Gender}, Count: {name.Count}")
            self.ui.listWidget_2.addItem(item)

    def show_top_50_state_names(self):
        names = get_first_50_state_names()
        self.ui.listWidget.clear()
        for name in names:
            item = QListWidgetItem(f"ID: {name.Id}, Name: {name.Name}, Year: {name.Year}, Gender: {name.Gender}, State: {name.State}, Count: {name.Count}")
            self.ui.listWidget.addItem(item)

    def delete_national_name_by_id(self):
        try:
            id_to_delete = int(self.ui.lineEdit_7.text())
            delete_national_name(id_to_delete)
            QMessageBox.information(self, "Успех", f"Запись с ID {id_to_delete} удалена из NationalNames.")
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите корректный ID.")

    def delete_state_name_by_id(self):
        try:
            id_to_delete = int(self.ui.lineEdit_7.text())
            delete_state_name(id_to_delete)
            QMessageBox.information(self, "Успех", f"Запись с ID {id_to_delete} удалена из StateNames.")
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Введите корректный ID.")

    def search_national_names(self):
        name = self.ui.lineEdit_6.text()
        if name:
            results = search_national_names_by_name(name)
            self.ui.listWidget_2.clear()
            if results:
                for result in results:
                    item = QListWidgetItem(f"ID: {result.Id}, Name: {result.Name}, Year: {result.Year}, Gender: {result.Gender}, Count: {result.Count}")
                    self.ui.listWidget_2.addItem(item)
            else:
                QMessageBox.information(self, "Результат", "Имя не найдено.")
        else:
            QMessageBox.warning(self, "Ошибка", "Введите имя для поиска.")

    def search_state_names(self):
        name = self.ui.lineEdit_6.text()
        if name:
            results = search_state_names_by_name(name)
            self.ui.listWidget.clear()
            if results:
                for result in results:
                    item = QListWidgetItem(f"ID: {result.Id}, Name: {result.Name}, Year: {result.Year}, Gender: {result.Gender}, State: {result.State}, Count: {result.Count}")
                    self.ui.listWidget.addItem(item)
            else:
                QMessageBox.information(self, "Результат", "Имя не найдено.")
        else:
            QMessageBox.warning(self, "Ошибка", "Введите имя для поиска.")
    def f(self, item):
        text = item.text() 
        id_start = text.find("ID")
        id_end = text.find(",")
        id_value = text[id_start+4:id_end].strip()
        self.ui.lineEdit_7.setText(id_value)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
