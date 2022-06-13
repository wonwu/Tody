from sys import path_hooks
from django import views
from django.contrib import admin
from django.urls import path, include
from login import login_views

urlpatterns = [
    path('', login_views.index, name='index'), # '/' 에 해당되는 path
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('login/', include('login.urls')),
    path('camera/', include('camera.urls'))
    
]
