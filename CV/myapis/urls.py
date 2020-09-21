from django.conf.urls import url
from . import views

app_name = 'myapis'

urlpatterns = [
    url(r'^$',views.APIPage.as_view(),name='all'),
]
