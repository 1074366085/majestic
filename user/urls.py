from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='user-login'),
    path('user-register', views.register, name='user-register'),
    path('user-all-user', views.all_user, name='user-all-user'),
    path('personal-information',views.personal_information,name='personal-information')
]
