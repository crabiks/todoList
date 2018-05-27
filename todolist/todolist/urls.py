
from django.contrib import admin
from django.urls import path
from tasks.views import index, categories, add_category, edit_category, delete_category

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('categories/', categories, name='categories-list'),
    path('add_category/', add_category, name='add-category'),
    path('edit_category/<int:category_id>', edit_category, name='edit-category'),
    path('delete_category/<int:category_id>', delete_category, name='delete-category')
]
