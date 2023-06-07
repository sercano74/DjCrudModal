from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('add_product', views.add_product ,name='add_product'),
    path('product/<str:product_id>', views.product ,name='product'),
    path('edit_product', views.edit_product ,name='edit_product'),
    path('delete_product/<str:product_id>', views.delete_product ,name='delete_product'),
    # VERSION CON VISTAS CON MODAL 100%
    path('home2', views.home2, name='home2'),
    path('add2_product', views.add2_product ,name='add2_product'),
    path('product2/<str:product_id>', views.product2 ,name='product2'),
    path('edit2_product', views.edit2_product ,name='edit2_product'),
    path('delete2_product/<str:product_id>', views.delete2_product ,name='delete2_product'),

]
