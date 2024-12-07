from . import views
from django.urls import path,include
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('',views.index,name='index'),
   path('index2/',views.index2,name='index2'),
   path('adding/',views.addingview.as_view(),name='adding'),
   path('select/',views.select,name='select'),
   path('deletelogin/<int:id>/',views.deletelogin,name='deletelogin'),
path('updatelogin/<int:id>/',views.updatelogin,name='updatelogin'),

path('register/',views.registration,name='register'),
path('login/',views.user_login,name='login'),
path('logout/',views.user_logout,name='logout'),



 path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]