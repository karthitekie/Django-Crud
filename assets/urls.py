from django.urls import path
from . import views

urlpatterns = [

    path('', views.asset_list, name='asset_list'),  
    path('<int:asset_id>/maintenance/', views.maintenance_history, name='maintenance_history'),
    path('create/', views.create_asset, name='create_asset'),     
    path('maintenance_due_report/', views.maintenance_due_report, name='maintenance_due_report'),
    path('category/', views.category_view, name='category'),
    path('sub-category/', views.sub_category_view, name='sub_category'),
    path('department/', views.department_view, name='department'),
    path('location/', views.location_view, name='location'),


]
