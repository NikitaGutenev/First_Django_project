import os
from random import randint


deals = [
        {"id": 1, "customer": "Elon Mask", "short_description": "Make a website for rocket control.", 
         "description": "Long description", "price": 97500, "status": True},
        {"id": 2, "customer": "Bill Gates", "short_description": "To-Do: fix some bugs in microsoft office.", 
         "description": "Long description", "price": 12700, "status": True},
        {"id": 3, "customer": "Vitaliy Buterin", "short_description": "Make a bridge 'Ethereum' to 'Graphene'", 
         "description": "Long description", "price": 32000, "status": False},
    ]


def set_data(title, *args, **kwargs):
    data = {
            "name_of_site": "best freelancer GGG",
            "title": title, 
            "menu": [
                {
                    "title": "Главная страница", 
                    "url_name": "index",
                }, 
                {
                    "title": "Сделать заказ", 
                    "url_name": "make_order",
                }, 
                {
                    "title": "Портфолио", 
                    "url_name": "portfolio",
                }, 
                {
                    "title": "О фрилансере", 
                    "url_name": "about_author",
                }, 
                {
                    "title": "О сайте", 
                    "url_name": "about_site",
                },
                {
                    "title": "Secret",
                    "url_name": "secret"
                }
            ],
        }
    for i in args:
        if isinstance(i, dict):
            data.update(i)
    data.update(kwargs)
    return data


def get_photo():
    lst = [(adress, files) for adress, dirs, files in os.walk('Iamgggutya/gggutya/static/gggutya/img/')]
    photo = lst[0][1][randint(0,len(lst[0][1])-1)]
    if photo.count('logo'):
        while photo.count('logo'):
            photo = lst[0][1][randint(0,len(lst[0][1])-1)]
    res = lst[0][0].rpartition('static')[-1] + photo
    return res


ABOUT_SITE = """Сайт создан для отработки навыков и закрепления теории курса по Django.
Если вы нашли какие-то ошибки и/или замечания в коде, то автор сайта будет очень рад, если вы
ему об этом скажете.
<b>Сайт - а-ля личный сайт фрилансера.</b>

Такие дела <3"""