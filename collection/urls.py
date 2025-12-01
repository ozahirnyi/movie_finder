from django.urls import path

from .views import CollectionCloneView, CollectionDetailView, CollectionListCreateView, CollectionMoviesView, CollectionSubscriptionView

urlpatterns = [
    path('collections/', CollectionListCreateView.as_view(), name='collections'),
    path('collections/<int:collection_id>/', CollectionDetailView.as_view(), name='collection_detail'),
    path('collections/<int:collection_id>/movies/', CollectionMoviesView.as_view(), name='collection_movies'),
    path('collections/<int:collection_id>/subscribe/', CollectionSubscriptionView.as_view(), name='collection_subscribe'),
    path('collections/<int:collection_id>/clone/', CollectionCloneView.as_view(), name='collection_clone'),
]
