from django.contrib import admin
from django.urls import path,include

from . import views

# forget reset pssowrd import 
from django.contrib.auth import views as auth_views


# uplading file import file 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',views.home,name='home'),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('resume/',views.resume,name="resume"),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('social-auth/',include('social_django.urls'),name='social'),
   
   
    path('change_password/',views.change_password,name='change_password'),

    
    #   4 reset path 
   
#    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
#    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
#    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
#    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


    # path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    # path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='reset_password_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
   
  

]
   


    
  

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    