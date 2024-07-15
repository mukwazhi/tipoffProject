from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('report_form', views.report_form, name="report_form"),
    path('track', views.track, name="track"),
    path("thanks", views.thanks),
    ]