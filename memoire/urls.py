"""memoire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from memoire.views import home, search, reference, add_comment, author, journal, discipline

urlpatterns = [
    path('', home, name='home'),
    path('references/<int:reference_id>', reference, name='reference'),
    path('authors/<int:author_id>', author, name='author'),
    path('journals/<int:journal_id>', journal, name='journal'),
    path('disciplines/<int:discipline_id>', discipline, name='discipline'),
    path('references/<int:reference_id>/comments', add_comment, name='add_comment'),
    path('search/', search, name='search'),
    path('admin/', admin.site.urls),
]
