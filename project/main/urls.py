from django.contrib import admin
from django.urls import path
from main import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path("delete/<int:id>", views.delete),
    path("edit/<int:id>", views.edit),
    path("create", views.create),
    path("details/<int:id>", views.details),
    
]
