from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    # Маршруты для записей ДДС
    path('', views.RecordListView.as_view(), name='record_list'),
    path('create/', views.RecordCreateView.as_view(), name='record_create'),
    path('<int:pk>/update/', views.RecordUpdateView.as_view(), name='record_update'),
    path('<int:pk>/delete/', views.RecordDeleteView.as_view(), name='record_delete'),
    
    # Маршруты для управления справочниками
    path('references/', views.ReferenceListView.as_view(), name='reference_list'),
    
    # Маршруты для управления статусами
    path('references/status/', views.StatusListView.as_view(), name='status_list'),
    path('references/status/create/', views.StatusCreateView.as_view(), name='status_create'),
    path('references/status/<int:pk>/update/', views.StatusUpdateView.as_view(), name='status_update'),
    path('references/status/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),
    
    # Маршруты для управления типами
    path('references/type/', views.TypeListView.as_view(), name='type_list'),
    path('references/type/create/', views.TypeCreateView.as_view(), name='type_create'),
    path('references/type/<int:pk>/update/', views.TypeUpdateView.as_view(), name='type_update'),
    path('references/type/<int:pk>/delete/', views.TypeDeleteView.as_view(), name='type_delete'),
    
    # Маршруты для управления категориями
    path('references/category/', views.CategoryListView.as_view(), name='category_list'),
    path('references/category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('references/category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('references/category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    
    # Маршруты для управления подкатегориями
    path('references/subcategory/', views.SubcategoryListView.as_view(), name='subcategory_list'),
    path('references/subcategory/create/', views.SubcategoryCreateView.as_view(), name='subcategory_create'),
    path('references/subcategory/<int:pk>/update/', views.SubcategoryUpdateView.as_view(), name='subcategory_update'),
    path('references/subcategory/<int:pk>/delete/', views.SubcategoryDeleteView.as_view(), name='subcategory_delete'),
    
    # API для динамической фильтрации
    path('api/categories-by-type/', views.get_categories_by_type, name='api_categories_by_type'),
    path('api/subcategories-by-category/', views.get_subcategories_by_category, name='api_subcategories_by_category'),
] 