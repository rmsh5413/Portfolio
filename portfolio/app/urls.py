from django.contrib import admin
from .import views
from django.urls import path,include

urlpatterns = [
    path('', views.index,name='index'),
    path('add-contact', views.contactUs,name='contact'),
    path('portfolio-detail/<int:id>/', views.portfolioDetail,name='portfolioDetail'),
    # path('',include('app.urls'))
]
