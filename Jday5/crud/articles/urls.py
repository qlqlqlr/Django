from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 전체 게시글 조회
    path('', views.index, name='index'),
    # 단일 게시글 조회
    path('<int:pk>/', views.detail, name = 'detail'),
    # CREATE
    # path('new/', views.new, name = 'new'),
    path('create/', views.create, name = 'create'),
    # DELETE
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    # UPDATE
    # path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('<int:pk>/update/', views.update, name = 'update'),
]
