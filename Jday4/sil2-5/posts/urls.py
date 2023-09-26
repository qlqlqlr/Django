from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),  # 빈 경로에 대한 뷰 함수를 'index'로 매핑합니다.
]
