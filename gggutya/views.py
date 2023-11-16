from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import capfirst, slugify
from gggutya.templates.templates_helper import deals, set_data, get_photo


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    data = set_data("Главная страница", deals = deals)
    return render(request, "gggutya/index.html", context=data)


def about_site(request):
    data = set_data("О сайте")
    return render(request, "gggutya/about_site.html", context=data)


def about_author(request):
    new_data = {
        "name": "Никита",
        "second_name": "Гутенев",
        "old": 16,
        "sex": "Мужской",
    }
    data = set_data("О фрилансере", new_data)
    return render(request, "gggutya/about_author.html", context=data)


def portfolio(request):
    data = set_data("Портфолио")
    return render(request, "gggutya/portfolio.html", context=data)


def check_order(request, id):
    new_data = deals[id-1]
    data = set_data("Полное описание заказа", new_data)
    return render(request, "gggutya/check_order.html", context=data)


def make_order(request):
    data = set_data("Сделать заказ")
    return render(request, "gggutya/make_order.html", context=data)


def secret(request):
    data = set_data("Secret", get_photo = get_photo)
    return render(request, "gggutya/secret.html", context=data)


def no_error_404(request, exception):
    return HttpResponseBadRequest("<h1>Такой страницы нет!</h1>")