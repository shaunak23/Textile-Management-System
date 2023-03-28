"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('yarnpage/', views.YarnPage, name="yarnpage"),
    path('yarnpage/submityarndata/', views.SubmitYarnData, name="submityarndata"),
    path('windingpage/', views.WindingPage, name="windingpage"),
    path('windingpage/submitwindingdata/', views.SubmitWindingData, name="submitwindingdata"),
    path('warpingpage/', views.WarpingPage, name="warpingpage"),
    path('warpingpage/submitwarpingdata/', views.SubmitWarpingData, name="submitwarpingdata"),
    path('loomingpage/', views.LoomingPage, name="loomingpage"),
    path('loomingpage/submitloomingdata/', views.SubmitLoomingData, name="submitloomingdata"),
    path('checkingpage/', views.CheckingPage, name="checkingpage"),
    path('checkingpage/submitcheckingdata/', views.SubmitCheckingData, name="submitcheckingdata"),
    path('repairingpage/', views.RepairingPage, name="repairingpage"),
    path('repairingpage/submitrepairingdata/', views.SubmitRepairingData, name="submitrepairingdata"),
    path('dashboardpage/', views.DashboardPage, name="dashboardpage"),
    path('dashboardpage/getdashboarddata/', views.GetDashboardData, name="getdashboarddata"),
    path('showyarndata/', views.ShowYarnCard, name="showyarndata"),
    path('showwindingdata/', views.ShowWindingCard, name="showwindingdata"),
    path('showwarpingdata/', views.ShowWarpingCard, name="showwarpingdata"),
    path('showloomingdata/', views.ShowLoomingCard, name="showloomingdata"),
    path('showcheckingdata/', views.ShowCheckingCard, name="showcheckingdata"),
    path('showrepairingdata/', views.ShowRepairingCard, name="showrepairingdata"),
    path('showpackingdata/', views.ShowPackingCard, name="showpackingdata"),
    path('adminlandingpage/', views.AdminLandingPage, name="adminlandingpage"),
    path('addorderpage/', views.AddOrderPage, name="addorderpage"),
    path('addorderpage/submitaddorder/', views.SubmitOrder, name="submitaddorder"),
    path('detailsnotfound/', views.DetailsNotFound, name="detailsnotfound"),
]   
