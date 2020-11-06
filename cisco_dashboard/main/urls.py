from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ben', views.ben, name='ben'),
    path('fraser', views.fraser, name='fraser'),
    path('jake', views.jake, name='jake'),
    path('johnathan', views.johnathan, name='johnathan'),
    path('ruofan', views.ruofan, name='ruofan'),
    
    path('<slug:org_slug>', views.showOrg, name = "show_org"),
    path('<slug:org_slug>/<slug:net_slug>', views.showNet, name = "show_net")
]