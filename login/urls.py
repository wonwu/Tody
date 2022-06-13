from django.urls import path
from django.contrib.auth import views as auth_views
from . import login_views
from django.conf import settings
from django.conf.urls.static import static



app_name ='login'

urlpatterns = [
    path('', login_views.index, name='index'),
    path('login/',auth_views.LoginView.as_view(template_name='login/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', login_views.signup, name='signup'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)