from . import views
from .forms import LoginForm
from django.urls import path
from django.contrib.auth import views as AuthViews


app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('Terms-of-use', views.Terms_of_use, name="terms-of-use"),
    path('Privacy-Policy/', views.Privacy_Policy, name="Privacy-Policy"),
    path('About/', views.About, name="About"),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.Signup, name="signup"),
    path('logout/', views.logout_view, name='logout'),
    path('login/', AuthViews.LoginView.as_view(template_name='core/login.html',authentication_form=LoginForm), name='login')
]