from django.urls import path
from .views import (
     product_detail_view,    
     product_create_view, 
     product_update_view,
     product_delete_view, 
     product_list_view
)

app_name = 'products'
urlpatterns = [
    path('<int:id>/', product_detail_view, name='detail'),
    path('create/', product_create_view, name='list'),
    path('<int:my_id>/update/', product_update_view, name='update'),
    path('', product_list_view, name='list'),
    path('<int:my_id>/delete/', product_delete_view, name='delete'),
]
