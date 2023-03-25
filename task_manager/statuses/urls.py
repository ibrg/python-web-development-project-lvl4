from django.urls import path

from .views import StatusListView, StatusCreateView, StatusUpdateView, StatusDeleteView

urlpatterns = [
    path('create/', StatusCreateView.as_view(), name='status_create'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
    path('', StatusListView.as_view(), name='status_list')
]
