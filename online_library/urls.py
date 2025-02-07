"""online_library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home_module.urls')),
    path('', include('account_module.urls')),
    path('contact-us/', include('contact_module.urls')),
    path('blog/', include('blog_module.urls')),
    path('books/', include('books_module.urls')),
    path('dashboard/', include('user_pannel_module.urls')),
    path('search-box/', include('siteSetting_module.urls')),
    path('writers/', include('writers_module.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
