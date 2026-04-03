from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass(slots=True, kw_only=True)
class AuthenticateUserCommand:
    email: str
    password: str


@dataclass(slots=True, kw_only=True)
class AuthenticateUserResult:
    access_token: str
    expires_in: int
    token_type: str = "bearer"


@dataclass(slots=True, kw_only=True)
class CurrentUserDTO:
    id: UUID
    email: str
    full_name: str


@dataclass(slots=True, kw_only=True)
class UserDTO:
    id: UUID
    email: str
    full_name: str
    is_active: bool
    created_at: datetime


@dataclass(slots=True, kw_only=True)
class UserCredentialsDTO:
    user: UserDTO
    password_hash: str


@dataclass(slots=True, kw_only=True)
class GetUserQuery:
    user_id: UUID


@dataclass(slots=True, kw_only=True)
class ListUsersQuery:
    page: int = 1
    page_size: int = 20
