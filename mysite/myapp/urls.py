from django.urls import path,include

from . views import *

urlpatterns = [
    path('login', login.as_view()),
    path('check_user', check_user.as_view()),
    path('logout_user', logout_user.as_view()),
    # path('check', views.check_login, name='check_login'),
    # path('accounts/', include('django.contrib.auth.urls'))
]