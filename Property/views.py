from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from . models import Property,Property_Detail,FavouriteProperty,User
from . forms import ApartmentTypeForm, PropertyDetailForm, PropertyForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

class AddProperty(CreateView):
    form_class = PropertyForm
    template_name = 'property/addproperty.html'
    success_url ='/'
    success_message = 'List successfully saved!!!!'

class AddPropertyDetail(CreateView):
    form_class = PropertyDetailForm
    template_name = 'property/addpropertydetail.html'
    success_url ='/'
    success_message = 'List successfully saved!!!!'

class AddApartmentType(CreateView):
    form_class = ApartmentTypeForm
    template_name = 'property/addapartment_type.html'
    success_url ='/'
    success_message = 'List successfully saved!!!!'

# class EditProperty(UpdateView):
#     model = Property_Detail
#     template_name = 'pages/editproperty.html'


def propertydetail(request, property_id):
    property=get_object_or_404(Property_Detail, pk=property_id)

    context={
        'listing':property
    }

    return render(request, 'property/propertydetail.html', context)

def favouriteList(request):
    new = Property_Detail.objects.filter(favourites=request.user)
    return render(request,'pages/favourites.html',{'listings':new})

@login_required
def favouriteAdd(request,favourite_id):
    post = get_object_or_404(Property_Detail, id=favourite_id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
