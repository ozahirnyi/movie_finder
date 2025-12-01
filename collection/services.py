from __future__ import annotations

from .dataclasses import (
    CollectionDTO,
    CollectionListResult,
    CollectionMovieListResult,
    CollectionPayload,
    CollectionUpdatePayload,
)
from .repositories import CollectionRepository


class CollectionService:
    def __init__(self, repository: CollectionRepository | None = None):
        self.repository = repository or CollectionRepository()

    def list_collections(
        self,
        *,
        viewer_id: int,
        is_staff: bool,
        is_public: bool | None = None,
        owner_id: int | None = None,
        subscribed: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> CollectionListResult:
        visibility_filter = self._resolve_visibility_filter(viewer_id=viewer_id, requested_owner_id=owner_id, explicit_public=is_public)
        subscriber_id = viewer_id
        only_subscribed = bool(subscribed)
        return self.repository.list(
            owner_id=owner_id,
            is_public=visibility_filter,
            limit=limit,
            offset=offset,
            subscriber_id=subscriber_id,
            only_subscribed=only_subscribed,
        )

    def create_collection(
        self,
        *,
        owner_id: int,
        name: str,
        description: str | None,
        is_public: bool,
        movie_ids: list[int] | None,
    ) -> CollectionDTO:
        payload = CollectionPayload(
            owner_id=owner_id,
            name=name,
            description=description or '',
            is_public=is_public,
            movie_ids=movie_ids or [],
        )
        return self.repository.create(payload)

    def retrieve_collection(self, *, viewer_id: int, is_staff: bool, collection_id: int) -> CollectionDTO:
        collection = self.repository.retrieve(collection_id, viewer_id=viewer_id)
        self._ensure_can_view(viewer_id=viewer_id, is_staff=is_staff, owner_id=collection.owner_id, is_public=collection.is_public)
        return collection

    def update_collection(
        self,
        *,
        viewer_id: int,
        is_staff: bool,
        collection_id: int,
        name: str | None = None,
        description: str | None = None,
        is_public: bool | None = None,
        movie_ids: list[int] | None = None,
    ) -> CollectionDTO:
        current = self.repository.retrieve(collection_id)
        self._ensure_can_edit(viewer_id=viewer_id, is_staff=is_staff, owner_id=current.owner_id)
        payload = CollectionUpdatePayload(
            name=name,
            description=description,
            is_public=is_public,
            movie_ids=movie_ids,
        )
        return self.repository.update(collection_id, payload)

    def delete_collection(self, *, viewer_id: int, is_staff: bool, collection_id: int) -> None:
        current = self.repository.retrieve(collection_id)
        self._ensure_can_edit(viewer_id=viewer_id, is_staff=is_staff, owner_id=current.owner_id)
        self.repository.delete(collection_id)

    def list_collection_movies(
        self, *, viewer_id: int, is_staff: bool, collection_id: int, limit: int | None = None, offset: int | None = None
    ) -> CollectionMovieListResult:
        collection = self.repository.retrieve(collection_id, viewer_id=viewer_id)
        self._ensure_can_view(viewer_id=viewer_id, is_staff=is_staff, owner_id=collection.owner_id, is_public=collection.is_public)
        return self.repository.list_movies(collection_id=collection_id, limit=limit, offset=offset)

    def subscribe(self, *, viewer_id: int, is_staff: bool, collection_id: int) -> None:
        collection = self.repository.retrieve(collection_id, viewer_id=viewer_id)
        if self._is_owner(viewer_id=viewer_id, owner_id=collection.owner_id):
            return
        self._ensure_can_view(viewer_id=viewer_id, is_staff=is_staff, owner_id=collection.owner_id, is_public=collection.is_public)
        self.repository.subscribe(collection_id=collection_id, user_id=viewer_id)

    def unsubscribe(self, *, viewer_id: int, collection_id: int) -> None:
        self.repository.unsubscribe(collection_id=collection_id, user_id=viewer_id)

    def clone_collection(self, *, viewer_id: int, is_staff: bool, collection_id: int) -> CollectionDTO:
        source = self.repository.retrieve(collection_id, viewer_id=viewer_id)
        self._ensure_can_view(viewer_id=viewer_id, is_staff=is_staff, owner_id=source.owner_id, is_public=source.is_public)
        return self.repository.clone(source_id=collection_id, owner_id=viewer_id)

    def _resolve_visibility_filter(self, *, viewer_id: int, requested_owner_id: int | None, explicit_public: bool | None) -> bool | None:
        if explicit_public is not None:
            return explicit_public
        if requested_owner_id is not None and self._is_owner(viewer_id=viewer_id, owner_id=requested_owner_id):
            return None
        return True

    def _ensure_can_view(self, *, viewer_id: int, is_staff: bool, owner_id: int, is_public: bool) -> None:
        if is_public:
            return
        if self._has_admin_access(is_staff=is_staff):
            return
        if not self._is_owner(viewer_id=viewer_id, owner_id=owner_id):
            raise PermissionError('You do not have access to this collection.')

    def _ensure_can_edit(self, *, viewer_id: int, is_staff: bool, owner_id: int) -> None:
        if self._has_admin_access(is_staff=is_staff):
            return
        if not self._is_owner(viewer_id=viewer_id, owner_id=owner_id):
            raise PermissionError('You do not have permissions to modify this collection.')

    @staticmethod
    def _is_owner(*, viewer_id: int, owner_id: int) -> bool:
        return viewer_id == owner_id

    @staticmethod
    def _has_admin_access(*, is_staff: bool) -> bool:
        return is_staff
