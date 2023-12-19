from django.urls import path
from . import views
app_name = 'shopping_app'

urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>',views.prodDetail,name='prodCatDetail')
]