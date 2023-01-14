from django.urls import path
from . import views

urlpatterns = [
    path('criminal_info/',views.Criminal_Info_View.as_view()),
]
