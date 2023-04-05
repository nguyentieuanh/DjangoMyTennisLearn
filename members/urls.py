from django.urls import path #tạo ra các đường dẫn path
from . import views #gọi file views để lấy response 

#tạo 1 list lưu các đường dẫn path
urlpatterns = [
    path('members/', views.member, name='members'),
    path('members/details/<int:id>', views.details, name='details'), 
    path('', views.main, name='main'), 
    # path('testing/', views.testing, name='test'),
]