from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'


urlpatterns = [
    path('', adminapp.index, name='index'),
    # path('user/update/<int:user_pk>', adminapp.user_update, name='user_update'),
    path('user/update/<int:user_pk>', adminapp.ShopUserAdminUpdate.as_view(), name='user_update'),
    path('user/delete/<int:user_pk>', adminapp.user_delete, name='user_delete'),
    path('categories/', adminapp.categories, name='categories'),
    path('category/create/', adminapp.ProductCategoryCreate.as_view(), name='category_create'),
    path('category/update/<int:pk>', adminapp.ProductCategoryUpdate.as_view(), name='category_update'),
]
