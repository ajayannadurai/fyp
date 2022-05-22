from django.urls import path

from . import views
#from mysite import fasttag

app_name='fasttag'

urlpatterns = [
    path('index', views.index, name='index'),
    path('<int:pk>/', views.transfer.as_view(), name='transfer'),
    path('<int:fastid>/pay', views.pay, name='pay'),
    path('sucess/',views.sucess,name="sucess"),
    path('fine/',views.fine,name='fine')

    
]