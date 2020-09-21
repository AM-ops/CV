from django.conf.urls import url
from . import views

app_name = 'messageapp'

urlpatterns = [
    url(r'^create$',views.MessageCreate.as_view(),name='create'),
]
