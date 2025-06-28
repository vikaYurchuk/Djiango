from django.contrib import admin
from django.urls import include, path
from main import views 
from django.conf.urls.static import static

from project import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('', include('main.urls')),
    path("favourite/", include("favourite.urls")),
    
]

if settings.DEBUG:  # Only serve media files in developmentAdd commentMore actions
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)