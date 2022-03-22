from django.urls import path,include
from django.views.decorators.csrf import csrf_exempt

from . views import *

urlpatterns = [
    path('login', login.as_view()),
    path('logout', logout_user.as_view()),
    path('rating', rating.as_view()),
    path('average', average.as_view()),
    path('list', list.as_view()),
    path('view', view.as_view()),
    path('register', register.as_view()),

    # path('check', views.check_login, name='check_login'),
    # path('accounts/', include('django.contrib.auth.urls'))
]