from django.conf.urls import url
from .views import KBSUrlView

urlpatterns = [
    url(r'^$', KBSUrlView.as_view(), name='api'),
] 
