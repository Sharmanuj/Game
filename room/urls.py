from django.urls import path
from . import views

app_name='room'

urlpatterns=[
    path('add',views.AddRoom.as_view(),name='add'),
    path('CountryLookup',views.CountryLookup,name='CountryLookup'),
    path('RegionLookup/<int:pk>',views.RegionLookup,name='RegionLookup'),
    path('CityLookup/<int:pk>',views.CityLookup,name='CityLookup'),
    path('addplace/',views.AddPlace.as_view(),name='addplace'),
    path('ManageSlots/<int:pk>',views.ManageSlots.as_view(),name='ManageSlots'),
    path('get_slots/<int:pk>',views.send_slots_by_day,name='get_slots'),
    path('SetSlots/<int:pk>',views.SetRoomSlots.as_view(),name='set-slots'),
    # path('CreateSlots',views.CreateSlots,name='CreateSlots'),
    
]