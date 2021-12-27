from django.urls import path
from .views import userlogin, userlogout,Registration,PasswordChanged
from . import views
from django.contrib.auth import views as auth_views

# app_name = 'accounts'

urlpatterns = [
	path('register/', Registration.as_view(), name='register'),
    path('login/', views.userlogin.as_view(), name='login'),
	path('changepassword/',views.PasswordChanged.as_view(),name='changepassword'),
	path('logout/', userlogout.logout_user, name='logout'),
	path('dashboard/',views.Dashboard,name = 'dashboard'),

	#Reset password urls
	path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
	path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
