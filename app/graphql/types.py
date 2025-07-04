from __future__ import annotations
from datetime import datetime
import enum
from typing import List, Optional
from uuid import UUID

import strawberry


@strawberry.type
class UserType:
    id: UUID
    email: str


@strawberry.type
class PathItemType:
    id: Optional[UUID]
    name: str


@strawberry.type
class FolderType:
    id: UUID
    name: str
    created_at: datetime
    updated_at: Optional[datetime]
    folders: List["FolderType"]
    files: List[FileType]
    links: List[LinkType]
    permissions: List[FolderPermissionType]
    parent: Optional["FolderType"]
    owner: UserType
    path: List[PathItemType]


@strawberry.type
class FileType:
    id: UUID
    name: str
    created_at: datetime
    updated_at: Optional[datetime]
    folder: Optional[FolderType]
    starred: bool
    file: str
    size: int
    mime_type: str
    ext: str
    permissions: List[FilePermissionType]
    links: List[LinkType]


@strawberry.type
class LinkType:
    id: UUID
    token: str
    target_type: LinkTarget
    target_id: UUID
    shared_with_sub: Optional[str]
    is_public: bool
    created_at: datetime
    expires_at: Optional[datetime]
    folder: Optional[FolderType]
    file: Optional[FileType]


@strawberry.enum
class Role(str, enum.Enum):
    owner = "owner"
    editor = "editor"
    viewer = "viewer"


@strawberry.type
class FilePermissionType:
    id: UUID
    user_id: str
    file: FileType
    role: Role
    user: UserType


@strawberry.type
class FolderPermissionType:
    id: UUID
    user_id: str
    folder: FolderType
    role: Role
    user: UserType


@strawberry.input
class FolderCreationInput:
    name: str
    parent_id: Optional[UUID] = None


@strawberry.input
class FolderUpdateInput:
    name: Optional[str] = None
    parent_id: Optional[UUID] = None


@strawberry.type
class DeleteResponse:
    """Deletion response"""

    success: bool
    message: str


@strawberry.input
class FileUpdateInput:
    name: Optional[str] = None
    folder_id: Optional[UUID] = None
    starred: Optional[bool] = None


@strawberry.enum
class LinkTarget(enum.Enum):
    FOLDER = "folder"
    FILE = "file"


@strawberry.input
class LinkInput:
    file_id: Optional[UUID] = None
    folder_id: Optional[UUID] = None
    password: Optional[str] = None
    expires_at: Optional[datetime] = None
