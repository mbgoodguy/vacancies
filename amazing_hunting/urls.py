"""amazing_hunting URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads.views import service
from amazing_hunting import settings
from vacancies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('vacancies/', views.VacancyListView.as_view()),
    path('vacancy/', include('vacancies.urls')),
    path('root/', service.health_check),
    path('', include('ads.urls')),
    path('company/', include('companies.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
