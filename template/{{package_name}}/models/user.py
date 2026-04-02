from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from .base import BaseModel


@dataclass(slots=True, kw_only=True)
class User(BaseModel):
    id: UUID
    email: str
    full_name: str
    is_active: bool
    created_at: datetime


@dataclass(slots=True, kw_only=True)
class UserCredentials(BaseModel):
    user: User
    password_hash: str
