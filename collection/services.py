from __future__ import annotations

from .dataclasses import (
    CollectionDTO,
    CollectionListResult,
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
        user,
        is_public: bool | None = None,
        owner_id: int | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> CollectionListResult:
        visibility_filter = self._resolve_visibility_filter(user=user, requested_owner_id=owner_id, explicit_public=is_public)
        return self.repository.list(owner_id=owner_id, is_public=visibility_filter, limit=limit, offset=offset)

    def create_collection(
        self,
        *,
        owner,
        name: str,
        description: str | None,
        is_public: bool,
        movie_ids: list[int] | None,
    ) -> CollectionDTO:
        payload = CollectionPayload(
            owner_id=owner.id,
            name=name,
            description=description or '',
            is_public=is_public,
            movie_ids=movie_ids or [],
        )
        return self.repository.create(payload)

    def retrieve_collection(self, *, user, collection_id: int) -> CollectionDTO:
        collection = self.repository.retrieve(collection_id)
        self._ensure_can_view(user=user, owner_id=collection.owner_id, is_public=collection.is_public)
        return collection

    def update_collection(
        self,
        *,
        user,
        collection_id: int,
        name: str | None = None,
        description: str | None = None,
        is_public: bool | None = None,
        movie_ids: list[int] | None = None,
    ) -> CollectionDTO:
        current = self.repository.retrieve(collection_id)
        self._ensure_can_edit(user=user, owner_id=current.owner_id)
        payload = CollectionUpdatePayload(
            name=name,
            description=description,
            is_public=is_public,
            movie_ids=movie_ids,
        )
        return self.repository.update(collection_id, payload)

    def delete_collection(self, *, user, collection_id: int) -> None:
        current = self.repository.retrieve(collection_id)
        self._ensure_can_edit(user=user, owner_id=current.owner_id)
        self.repository.delete(collection_id)

    def _resolve_visibility_filter(self, *, user, requested_owner_id: int | None, explicit_public: bool | None) -> bool | None:
        if explicit_public is not None:
            return explicit_public
        if requested_owner_id is not None and self._is_owner(user=user, owner_id=requested_owner_id):
            return None
        return True

    def _ensure_can_view(self, *, user, owner_id: int, is_public: bool) -> None:
        if is_public:
            return
        if self._has_admin_access(user):
            return
        if not self._is_owner(user=user, owner_id=owner_id):
            raise PermissionError('You do not have access to this collection.')

    def _ensure_can_edit(self, *, user, owner_id: int) -> None:
        if self._has_admin_access(user):
            return
        if not self._is_owner(user=user, owner_id=owner_id):
            raise PermissionError('You do not have permissions to modify this collection.')

    @staticmethod
    def _is_owner(*, user, owner_id: int) -> bool:
        return bool(user) and getattr(user, 'is_authenticated', False) and user.id == owner_id

    @staticmethod
    def _has_admin_access(user) -> bool:
        return bool(user) and getattr(user, 'is_authenticated', False) and getattr(user, 'is_staff', False)
