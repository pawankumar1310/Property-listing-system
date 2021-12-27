
from django.urls import path

from .models import Property_Detail
from . import views

urlpatterns = [
    path('addproperty/',views.AddProperty.as_view(),name='addproperty'),
    path('addproperty/detail/',views.AddPropertyDetail.as_view(),name='addpropertydetail'),
    path('addapartmenttype/',views.AddApartmentType.as_view(),name='addapartmenttype'),
    path('/<uuid:property_id>',views.propertydetail,name='propertydetails'),
    path('/favourite/<uuid:favourite_id>',views.favouriteAdd,name='favouriteadd'),
    path('favourites/', views.favouriteList,name='favouritelist'),

]
