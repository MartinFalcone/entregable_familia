
from django.contrib import admin
from django.urls import path
from entregable_familia.views import familia_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path("familia_template/", familia_template), 
    
]
