"""number_predictor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import URLResolver, re_path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from mega_api.models import *
from mega_api.views import *

router: DefaultRouter = DefaultRouter(trailing_slash=False)
router.register(r'mega_millions/winning_sets', WinningSets, 'winning_sets')
router.register(r'mega_millions/balls', Balls, 'balls')
router.register(r'mega_millions/mega_balls', MegaBalls, 'mega_balls')
router.register(r'mega_millions/users', Users, 'users')

urlpatterns: list[URLResolver] = [
    re_path(r'^', include(router.urls)),
    re_path(r'^register$', register_user),
    re_path(r'^login$', login_user),
    re_path(r'^api-token-auth$', obtain_auth_token),
    re_path(r'^api-auth', include('rest_framework.urls',
            namespace='rest_framework')),
]
