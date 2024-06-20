from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.report_form, name="report_form"),
    path("thanks", views.thanks),
    ]