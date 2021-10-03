from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('user/create/', views.create_user, name='create_user'),
    path('user/update/<int:user_id>/', views.update_user, name='update_user'),
    path('user/read/<int:user_id>/', views.read_user, name='read_user'),
    path('user/delete/<int:user_id>/', views.delete_user, name='delete_user'),

    path('create/', views.create_cat, name='create_cat'),
    path('update/<int:cat_id>/', views.update_cat, name='update_cat'),
    path('read/<int:cat_id>/', views.read_cat, name='read_cat'),
    path('delete/<int:cat_id>/', views.delete_cat, name='delete_cat'),

    path('review/create/', views.create_review, name='create_review'),
    path('review/update/<int:review_id>/', views.update_review, name='update_review'),
    path('review/read/<int:review_id>/', views.read_review, name='read_review'),
    path('review/delete/<int:review_id', views.delete_review, name='delete_review'),
]
