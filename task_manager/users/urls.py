from django.urls import path

from .views import UserCreateView, UserDelete, UserListView, UserUpdateView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDelete.as_view(), name='user_delete'),
    path('', UserListView.as_view(), name='users_list')
]
