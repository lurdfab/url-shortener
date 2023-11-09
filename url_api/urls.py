from django.urls import path
from .api import *

urlpatterns = [
    path('list/', ShortenerListView.as_view(), name='all_links'),
    path('create/', ShortnerCreateView.as_view(), name='create'),

]
