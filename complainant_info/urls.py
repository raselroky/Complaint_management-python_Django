from django.urls import path
from . import views

urlpatterns = [
    path('complainant_info/',views.Complainant_Info_View.as_view()),
]