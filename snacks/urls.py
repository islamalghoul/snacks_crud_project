from django.urls import path,include
from .views import Snacks,SnackList,Create,Update,Delete
urlpatterns = [
    path('',Snacks.as_view(),name='snack'),
    path('snack_detail/<pk>',SnackList.as_view(),name='SnackList'),
    path('create/',Create.as_view(),name='Create'),
    path('update/<pk>',Update.as_view(),name='Update'),
    path('delete/<pk>',Delete.as_view(),name='Delete')
    ]