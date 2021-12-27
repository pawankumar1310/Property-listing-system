from django.urls import path
from .import views
from django.urls import path
from .views import EmailAttachmentView

urlpatterns = [
    path('',views.home, name='home'),
    path('allproperty/',views.index, name='all_list'),
    path('<uuid:propertydetail_id>',EmailAttachmentView.as_view(),name='emailattachment'),
]
