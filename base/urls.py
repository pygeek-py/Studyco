from django.urls import path  
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('seeall-users/', views.seeall, name="seeall"),
    path('profile-user/<str:username>/<str:pk>', views.profile, name="profile"),
    path('profile-users/<str:username>/<str:first_name>/<str:pk>', views.profiles, name="profiles"),
    path('create-profile/', views.bring, name="bring"),
    path('sec/<str:pk>', views.sec, name="sec"),
    path('pool/<str:pk>', views.pool, name="pool"),
    path('work/', views.work, name="work"),
    path('message/<str:pk>/<str:topic>/', views.message, name="message"),
    path('basedon/<str:pk>/<str:lang>/', views.basedons, name="basedons"),
    path('edit-profile/', views.editprofile, name="editprofile"),
    path('register/', views.register, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)