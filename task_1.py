"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла"""
import os


def func1(path: str) -> tuple:
    sep1 = path.rfind("\\")
    sep2 = path.rfind(".")
    return s[:sep1], s[sep1 + 1:sep2], s[sep2 + 1:]


def func2(path: str) -> tuple:
    file_dir = os.path.dirname(path)
    file_name_parts = os.path.splitext(os.path.basename(path))
    return file_dir, file_name_parts[0], file_name_parts[1][1:]


s = "C:\\Users\\Ivan\\PycharmProjects\\python_hw5\\task_1.py"
print(func1(s))
print(func2(s))
