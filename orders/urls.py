from django.urls import path
from . import views


urlpatterns = [

    path('', views.OrderListView.as_view(), name='order_list'),
    path('order/create/',
         views.OrderCreateView.as_view(), name='order_create'),
    path('<int:pk>/order/edit/', views.OrderUpdateView.as_view(), name='order_edit'),
    path('<int:pk>/order/delete/', views.OrderDeleteView.as_view(), name='order_delete')
]
