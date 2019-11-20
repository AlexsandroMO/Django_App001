from django.urls import path
from . import views

urlpatterns = [ 
    #path('', views.Home, name='url-home'),
    #path('lista-conta', views.ListaConta, name='url-lista-conta'),
    #path('edit-conta/<int:id>', views.editConta, name='url-edit-conta'),
    #path('new_conta/', views.newConta, name='url-new-conta'),
    #path('delete_conta/<int:id>', views.deleteConta, name='url-delete-conta'),
    #path('pk-wallet/<int:id>', views.pkWallet, name='url-pk-wallet'),
    path('homes', views.Homes, name='url-homes'),
]
