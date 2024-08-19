from django.urls import path
from flowerapp import views
urlpatterns = [
    path('add_flower', views.add_flower),
    path('home', views.home, name='home'),
    path('more/<int:flower_id>/', views.more),
    path('addcart/<int:flower_id>/', views.add_cart),
    path('viewcart', views.view_cart),
    path('delete/<int:flower_id>/',views.remove_cart),
    path('',views.login_user),
    path('registeruser', views.register_user),
    path('logout', views.user_logout),
    path('myprofile', views.myprofile),
    path('editimage', views.edit_image)
]