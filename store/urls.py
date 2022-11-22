from django.urls import path, URLPattern, re_path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    # path('', views.main, name='main'),
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)