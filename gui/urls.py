"""
URL configuration for gui project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from project1.views import SignupPage, project
from project1.views import led
from project1.views import counter
from project1.views import calci
from project1.views import index
from project1.views import LoginPage
from project1.views import singup
from project1.views import LogoutPage
from project1.views import predict

urlpatterns = [
    path("admin/", admin.site.urls),
    path("project1/", project, name="project"),
    path("led/", led, name="led"),
    path("counter/", counter, name="counter"),
    path("calci/", calci, name="calci"),
    path("index/", index, name="index"),
    path("login/", LoginPage, name="login"),
    path("signup/", SignupPage, name="signup"),
    # keep legacy misspelled route for existing links
    path("singup/", singup, name="singup"),
    path("logout/", LogoutPage, name="logout"),
    path("predict/", predict, name="predict"),

]
