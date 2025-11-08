from django.urls import path

from .views import CollectionDetailView, CollectionListCreateView

urlpatterns = [
    path('collections/', CollectionListCreateView.as_view(), name='collections'),
    path('collections/<int:collection_id>/', CollectionDetailView.as_view(), name='collection_detail'),
]
