from django.urls import path
from base.views import order_views as views


urlpatterns = [

    path('add', views.addOrderItems, name='orders-add'),
    path('<str:pk>', views.getOrderById, name='user-order'),

    # path('', views.getOrders, name='orders'),
    # path('myorders', views.getMyOrders, name='myorders'),

    # path('<str:pk>/deliver', views.updateOrderToDelivered, name='order-delivered'),

    # path('<str:pk>/pay', views.updateOrderToPaid, name='pay'),
]