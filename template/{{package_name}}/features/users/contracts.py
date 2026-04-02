from dataclasses import dataclass
from uuid import UUID


@dataclass(slots=True, kw_only=True)
class AuthenticateUserCommand:
    email: str
    password: str


@dataclass(slots=True, kw_only=True)
class AccessToken:
    access_token: str
    expires_in: int
    token_type: str = "bearer"


@dataclass(slots=True, kw_only=True)
class GetUserCommand:
    user_id: UUID


@dataclass(slots=True, kw_only=True)
class ListUsersCommand:
    page: int = 1
    page_size: int = 20
