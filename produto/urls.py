from django.urls import path
from . import views

app_name = 'produto'


urlpatterns = [
    path('', views.ListaProdutos.as_view(), name='lista'),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe'),
    path('addtocart/', views.addtocart.as_view(), name='addtocart'),
    path('remcart/', views.RemCart.as_view(), name='remcart'),
    path('carrinho/', views.Carrinho.as_view(), name='carrinho'),
    path('resumodacompra/', views.ResumoDaCompra.as_view(), name='resumodacompra'),
]
