import logging
from logging.handlers import RotatingFileHandler

#настройка логирования
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

#создание обработчика ротации логов
handler = RotatingFileHandler('my_log.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)


import unittest
#функция которую мы будем тестировать
def add(a, b):
    return a + b

#класс для тестирования функции add
class TestAddFunction(unittest.TestCase):

    #тест для сложения положительных чисел
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    #тест для сложения отрицательных чисел
    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    #тест для сложения чисел с разными знаками
    def test_add_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

    #тест для сложения нулей
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
#запускаем
if __name__ == '__main__':
    unittest.main()



import tkinter as tk

#функция которая будет вызываться при нажатии на кнопку
def change_text():
    main_label.config(text="текст изменен")
#создание главного окна
main_window = tk.Tk()
main_window.title("окно")
#создание метки
main_label = tk.Label(main_window, text="нажмите кнопку для изменения текста")
main_label.pack(pady=10)  # С помощью pack() размещаем метку в окне
#создание кнопки 
change_button = tk.Button(main_window, text="изменить текст", command=change_text)
change_button.pack(pady=10) 
#запуск
main_window.mainloop()
