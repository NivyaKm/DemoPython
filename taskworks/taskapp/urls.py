from.import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('opr/',views.operations,name='operations')
 ]
