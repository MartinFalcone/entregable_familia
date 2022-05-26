
from django.contrib import admin
from django.urls import path
from appfamilia.views import familia_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path("familia_template/", familia_template), 
    
]
