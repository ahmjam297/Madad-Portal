from django.urls import path
from . import views as c_views

urlpatterns= [
path('',c_views.homepage,name='home'),
path('about',c_views.about,name='about'),
path('dept',c_views.dept,name='dept'),
path('Adcomplain',c_views.Adcomplain,name='Adcomplain'),
path('Acomplain',c_views.Acomplain,name='Acomplain'),
path('Ccomplain',c_views.Ccomplain,name='Ccomplain'),
path('Ecomplain',c_views.Ecomplain,name='Ecomplain'),
path('Mcomplain',c_views.Mcomplain,name='Mcomplain'),
path('Scomplain',c_views.Scomplain,name='Scomplain'),
path('Rcomplain',c_views.Rcomplain,name='Rcomplain'),
path('AdminComplainCheck',c_views.AdminComplainCheck,name='AdminComplainCheck'),
path('DeptComplainCheck',c_views.DeptComplainCheck,name='DeptComplainCheck'),
path('UserComplainCheck',c_views.UserComplainCheck,name='UserComplainCheck'),
path('complain/<int:pk>/update/',c_views.ComplainUpdateView.as_view(), name='complain-update'),
path('user-detail/<str:username>',c_views.user_detail,name='user-detail'),
path('thank',c_views.thank,name='thank'),
];
