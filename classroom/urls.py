from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
app_name = "classroom"


urlpatterns = [
    path('', views.classpick,name="home"),
    path('about/<str:pk_test>/',views.about,name="about"),
    path('about/<str:pk_test>/schedule',views.schedule,name="schedule"),
    path('about/<str:pk_test>/information',views.information,name="information"),
]

