from django.contrib import admin
from django.urls import path
from core.views import home, registerpro, cadprod, listprod, registercli, cadcli, listcli, deleteprod, confirmdeleteprod, deletecateg
from core.views import editcli, deletecli, confirmeditcli, confirmdeletecli, teste, editprod, confirmeditprod, categorias, cadcateg
from core.views import searchprod, searchcli
urlpatterns = [
    path('', home),
    path('home', home, name='home'),
    path('registerpro', registerpro, name='registerpro'),
    path('cadprod', cadprod, name='cadprod'),
    path('listprod', listprod, name='listprod'),
    path('editprod/<int:id>', editprod, name='editprod'),
    path('confirmeditprod/<int:id>', confirmeditprod, name='confirmeditprod'),
    path('deleteprod/<int:id>', deleteprod, name='deleteprod'),
    path('confirmdeleteprod/<int:id>', confirmdeleteprod, name='confirmdeleteprod'),
    path('registercli', registercli, name='registercli'),
    path('cadcli', cadcli, name='cadcli'),
    path('listcli', listcli, name='listcli'),
    path('editcli/<int:id>', editcli, name='editcli'),
    path('confirmeditcli/<int:id>', confirmeditcli, name='confirmeditcli'),
    path('deletecli/<int:id>', deletecli, name='deletecli'),
    path('confirmdeletecli/<int:id>', confirmdeletecli, name='confirmdeletecli'),
    path('categorias', categorias, name="categorias"),
    path('cadcateg', cadcateg, name="cadcateg"),
    path('deletecateg', deletecateg, name='deletecateg'),
    path('searchprod', searchprod, name="searchprod"),
    path('searchcli', searchcli, name='searchcli'),
    path('teste', teste, name='teste'),
    



]
