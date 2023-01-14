
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('complaint.urls')),
    path('api/',include('complainant_info.urls')),
    path('api/',include('criminal_info.urls')),
]
