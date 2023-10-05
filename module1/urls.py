from django.conf import settings
from django.urls import path, include
from . import views
from django.conf.urls.static import static



# app_name = 'navbar'
urlpatterns = [
    path('',views.Homepage, name = 'home1'),
    # path('a',views.Homepage1, name = 'home11'),
    path('a',views.page1, name = 'page1'),

    ]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)