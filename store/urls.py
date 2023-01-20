from django.urls import path
from store import cart
from store import wishlist
from store import checkout
from store import order
from . import views
from store.controller import authview

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:slug>', views.product, name='product-info'),
    path('<str:cate_slug>/<str:prod_slug>/', views.productview, name='product-view'),

    # login, logout and register api
    path('register/', authview.register, name="registering"),
    path('login/', authview.loginpage, name="login-page"),
    path('logout/', authview.logoutpage, name="logout-page"),

    # cart api
    path('add-to-cart/', cart.addtocart, name="addtocart"),
    path('cart/', cart.myCart, name="my-cart"),
    path('update-cart/', cart.updateCart, name="update-cart"),
    path('delete-cart-item/', cart.deleteItem, name="delete-cart-item"),

    # wishlist api
    path('wishlist/', wishlist.wishList, name="my-list"),
    path('add-wish-item/', wishlist.addtowish, name="add-wish-list"),
    path('del-wish-item/', wishlist.deleteWishItem, name="delete-wish-item"),

    # checkout
    path('checkout/', checkout.checkout, name="checkout"),
    path('placeholder/', checkout.placeholder, name="placeholder"),

    # payment
    path('proceeded-to-pay/', checkout.razorpaycheck, name="razor-pay-check"),
    path('my-orders/', checkout.myorders, name="my-orders"),

    # order details
    path('my-details/', order.myOrderDetails, name="my-orders-details"),
    path('order overview/<str:t_no>/', order.orderOverview, name="order-overview"),

]
