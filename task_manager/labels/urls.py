from django.urls import path

from .views import (LabelCreateView, LabelDeleteView, LabelListView,
                    LabelUpdateView)

urlpatterns = [
    path('create/', LabelCreateView.as_view(), name='label_create'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='label_update'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='label_delete'),
    path('', LabelListView.as_view(), name='label_list')
]
