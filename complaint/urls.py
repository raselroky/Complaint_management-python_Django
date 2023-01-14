from django.urls import path,include

from . import views
urlpatterns = [
    path('complaints/',views.ComplaintView.as_view())
]