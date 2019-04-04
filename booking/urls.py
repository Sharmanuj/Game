from django.urls import path,include
from . import views

app_name='booking'

urlpatterns=[
    # path('',views.CustomerFormView.as_view(),name='booking'),
    path('search',views.SearchRoom.as_view(),name='search-room'),
    path('RoomList/<int:city>',views.ListRoom.as_view(),name='list-room')
]