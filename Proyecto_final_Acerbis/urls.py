
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from LOGIN import views
#from MAIN import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('LOGIN/', include('LOGIN.urls')),
    path('MAIN/', include('MAIN.urls')),
    path('SIGNUP/', include('SIGNUP.urls')),
    path('PROFILE/', include('PROFILE.urls')),
    
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)