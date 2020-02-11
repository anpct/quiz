"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from tst import views as tst_views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tst_views.register, name="register"),
    path('questions/', tst_views.questions, name="questions"),
    path('results-of-students-list/', tst_views.results, name="results"),
    path('signup/', user_views.signup, name="signup"),
]
