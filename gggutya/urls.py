from django.urls import path, register_converter
from . import views, converters


register_converter(converters.Year, "Year")


urlpatterns = [
    path('', views.index, name="index"),
    path("about-site/", views.about_site, name="about_site"),
    path("about-author/", views.about_author, name="about_author"),
    path("porfolio/", views.portfolio, name="portfolio"),
    path("make-order/<int:selected>/", views.make_order, name="make_order"),
    path("make-order/", views.make_order, name="make_order"),
    path("check-order/<int:id>/", views.check_order, name="check_order"),
    path("secret/", views.secret, name="secret"),
]

