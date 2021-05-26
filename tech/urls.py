from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
