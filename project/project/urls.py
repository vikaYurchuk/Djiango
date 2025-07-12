from django.contrib import admin
from django.urls import include, path
from main import views 
from django.conf.urls.static import static

from project import settings

from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(template_name="admin/login.html"), name="login"),
    path('', include('main.urls')),
    path("favourite/", include("favourite.urls")),
    path("orders/", include("orders.urls")),
    
]

if settings.DEBUG:  # Only serve media files in developmentAdd commentMore actions
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)