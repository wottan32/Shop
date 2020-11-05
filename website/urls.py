from django.urls import path
from website import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('cart/', views.cart, name='cart'),
    path('category/', views.category, name='category'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('contact/', views.contact, name='contact'),
    path('elements/', views.elements, name='elements'),
    path('login/', views.login, name="login"),
    path('singleBlog/', views.singleblog, name='singleblog'),
    path('singleproduct/', views.singleproduct, name='singleproduct'),
    path('tracking/', views.tracking, name='tracking'),
]
