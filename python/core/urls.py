from django.urls import path
from django.contrib.auth import views as auth_viws

from . import views


urlpatterns = [
	path('', views.frontpage, name='frontpage'),
	path('signup/', views.signup , name='signup'),
	path('login/', auth_viws.LoginView.as_view(template_name='core/login.html') , name='login'),
	path('logout/', auth_viws.LogoutView.as_view() , name='logout'),
]