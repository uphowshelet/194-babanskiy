import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, 
                             QTableWidgetItem, QHeaderView, QAbstractItemView,
                             QPushButton, QInputDialog)
from PyQt5.QtCore import QStringListModel
from PyQt5 import uic
from xml_processor import XMLProcessor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(current_dir, "main_gui.ui"), self)
        self.processor = XMLProcessor()
        self.found_elements = []

        self.pushButton.clicked.connect(self.load_xml)
        self.pushButton_2.clicked.connect(self.save_to_db)
        self.pushButton_3.clicked.connect(self.refresh_all)
        self.pushButton_4.clicked.connect(self.perform_search)
        self.pushButton_5.clicked.connect(self.save_sorted_file)

        self.radioButton.setChecked(True)

        self.stats_model = QStringListModel()
        self.listView_2.setModel(self.stats_model)
        self.file_model = QStringListModel()
        self.listView_3.setModel(self.file_model)

        self.setup_tables()
        self.setup_tabs()
        self.update_interface()
        self.load_schemas_list()

    def setup_tables(self):
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["имя", "тип", "значение", "x", "y"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setHorizontalHeaderLabels(["id", "схема", "имя", "тип", "значение", "x", "y", "удалить"])
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setHorizontalHeaderLabels(["имя файла", "дата", "кол-во элементов"])
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.itemDoubleClicked.connect(self.on_schema_selected)

    def setup_tabs(self):
        self.tabWidget.setTabText(0, "просмотр схемы")
        self.tabWidget.setTabText(1, "результаты поиска")
        self.tabWidget.setTabText(2, "все схемы")

    def update_interface(self):
        self.file_model.setStringList([self.processor.get_file_info()])
        self.stats_model.setStringList(self.processor.get_statistics())
        self.fill_elements_table()
        self.pushButton_2.setEnabled(self.processor.current_document_data is not None)

    def fill_elements_table(self):
        elements = self.processor.get_elements_for_table()
        self.tableWidget.setRowCount(len(elements))
        for row, element in enumerate(elements):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(element.get('name', '')))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(element.get('type', '')))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(element.get('value', '')))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(element.get('x', '')))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(element.get('y', '')))

    def update_search_table(self):
        self.tableWidget_2.setColumnCount(9) 
        self.tableWidget_2.setHorizontalHeaderLabels(["id", "схема", "имя", "тип", "значение", "x", "y", "удалить", "открыть схему"])
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.setRowCount(len(self.found_elements))
        
        for row, element in enumerate(self.found_elements):
            self.tableWidget_2.setItem(row, 0, QTableWidgetItem(str(element['search_id'])))
            self.tableWidget_2.setItem(row, 1, QTableWidgetItem(element['filename']))
            self.tableWidget_2.setItem(row, 2, QTableWidgetItem(element['name']))
            self.tableWidget_2.setItem(row, 3, QTableWidgetItem(element['type']))
            self.tableWidget_2.setItem(row, 4, QTableWidgetItem(element['value']))
            self.tableWidget_2.setItem(row, 5, QTableWidgetItem(element['x']))
            self.tableWidget_2.setItem(row, 6, QTableWidgetItem(element['y']))
            
            delete_btn = QPushButton("удалить")
            delete_btn.clicked.connect(lambda checked, r=row: self.delete_search_element(r))
            self.tableWidget_2.setCellWidget(row, 7, delete_btn)
            
            open_btn = QPushButton("открыть схему")
            open_btn.clicked.connect(lambda checked, filename=element['filename']: self.open_schema_from_search(filename))
            self.tableWidget_2.setCellWidget(row, 8, open_btn)

    def open_schema_from_search(self, filename):
        if self.processor.load_schema_from_db(filename):
            self.update_interface()
            self.tabWidget.setCurrentIndex(0)
            QMessageBox.information(self, "успех", f"схема {filename} загружена")
        else:
            QMessageBox.warning(self, "ошибка", f"не удалось загрузить схему {filename}")

    def delete_search_element(self, row):
        if 0 <= row < len(self.found_elements):
            del self.found_elements[row]
            for i, element in enumerate(self.found_elements):
                element['search_id'] = i + 1
            self.update_search_table()

    def load_schemas_list(self):
        schemas = self.processor.get_all_schemas()
        self.tableWidget_3.setRowCount(len(schemas))
        for row, schema in enumerate(schemas):
            self.tableWidget_3.setItem(row, 0, QTableWidgetItem(schema['filename']))
            self.tableWidget_3.setItem(row, 1, QTableWidgetItem(schema['date']))
            self.tableWidget_3.setItem(row, 2, QTableWidgetItem(str(schema['element_count'])))

    def load_xml(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "выбор файла", "", "TCD Files (*.tcd);;All Files (*)")
        if file_path and self.processor.load_and_process_xml(file_path):
            self.update_interface()
            QMessageBox.information(self, "успех", "файл успешно загружен и обработан")

    def save_to_db(self):
        success, message = self.processor.save_to_db()
        if success:
            QMessageBox.information(self, "успех", message)
            self.load_schemas_list()
        else:
            QMessageBox.warning(self, "ошибка", message)

    def refresh_all(self):
        self.update_interface()
        self.load_schemas_list()

    def perform_search(self):
        search_text = self.lineEdit.text().strip()
        if not search_text:
            QMessageBox.warning(self, "ошибка", "введите текст для поиска")
            return

        if self.radioButton.isChecked():
            new_elements = self.processor.search_elements_in_current(search_text)
            search_scope = "в текущей схеме"
        else:
            new_elements = self.processor.search_elements_in_all(search_text)
            search_scope = "во всех схемах"
        
        if not new_elements:
            QMessageBox.information(self, "результат", f"элементы не найдены {search_scope}")
            return
        
        start_index = len(self.found_elements)
        for element in new_elements:
            element['search_id'] = start_index + len(self.found_elements) + 1
            self.found_elements.append(element)

        self.update_search_table()
        self.tabWidget.setCurrentIndex(1)
        QMessageBox.information(self, "результат", f"найдено {len(new_elements)} элементов {search_scope}")

    def save_sorted_file(self):
        if not self.found_elements:
            QMessageBox.warning(self, "ошибка", "нет элементов для сохранения")
            return

        description, ok = QInputDialog.getText(self, "описание", "название бд:")
        if ok:
            success, message = self.processor.save_sorted_results(self.found_elements, description)
            if success:
                QMessageBox.information(self, "успех", message)
            else:
                QMessageBox.warning(self, "ошибка", message)

    def on_schema_selected(self, item):
        filename = self.tableWidget_3.item(item.row(), 0).text()
        if self.processor.load_schema_from_db(filename):
            self.update_interface()
            self.tabWidget.setCurrentIndex(0)
            QMessageBox.information(self, "успех", f"схема {filename} загружена")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
