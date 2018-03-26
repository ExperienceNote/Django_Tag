from . import views
from django.conf.urls import url
# Create your views here.
urlpatterns=[
url(r'^$',views.index ,name='index')
]
