from django.conf.urls import url
from . import apis

urlpatterns = [
    url(r'^login/$', apis.LoginView.as_view(), name='login'),
    url(r'^logout/$', apis.LogoutView.as_view(), name='logout'),

    #url(r'^register/$', apis.UserRegistrationView.as_view(), name='register'),

    #url(r'^me/$', apis.UserProfileView.as_view(), name='profile'),

    url(r'^change-password/$', apis.ChangePassword.as_view()),

]
