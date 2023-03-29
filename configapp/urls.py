from django.urls import path
from .views import index,category,detail,n_del,add_new,new_update

urlpatterns = [
    path('index/', index,name='home'),
    path('category/<int:pk>/', category,name='category'),
    path('detail/<int:pk>/', detail,name='detail'),
    path('n_del/<int:pk>/', n_del, name='n_del'),
    path('add_new/', add_new, name='add_new'),
    path('new_update/<int:pk>/', new_update, name='new_update'),
]
