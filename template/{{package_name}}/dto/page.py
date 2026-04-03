from dataclasses import dataclass
from typing import Generic
from typing import TypeVar

ItemT = TypeVar("ItemT")


@dataclass(slots=True)
class PageDTO(Generic[ItemT]):
    items: list[ItemT]
    total_pages: int
    page: int
    page_size: int
    total_items: int
