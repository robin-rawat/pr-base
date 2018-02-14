from django.urls import path,include,re_path
from .views import CreateProfile
from allauth.account.views import LoginView


urlpatterns = [
    path('profile/create', CreateProfile,name='create'),
]
