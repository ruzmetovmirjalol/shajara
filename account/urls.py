from django.urls import path

from account.views import LoginView, UserView

urlpatterns = [
    path('login/', LoginView.as_view(), name='account-login'),
    path('user/', UserView.as_view(), name='account-user')
]
