# -*- coding: utf-8 -*-
from cat import Cat

cats = [
    {"name": "Барон", "gender": "мальчик", "age": "2 года"},
    {"name": "Сэм", "gender": "мальчик", "age": "2 года"}
]

if __name__ == "__main__":
    for cat in cats:
        my_cat = Cat(name = cat["name"],
                     gender = cat["gender"],
                     age = cat["age"])
        my_cat.print_info()