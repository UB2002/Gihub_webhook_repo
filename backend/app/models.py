from pydantic import BaseModel
from typing import Optional
from enum import Enum

class ActionType(str, Enum):
    PUSH = "PUSH"
    PULL_REQUEST = "PULL_REQUEST"
    MERGE = "MERGE"

class WebhookEvent(BaseModel):
    request_id: str
    author: str
    action: ActionType
    from_branch: Optional[str] = None
    to_branch: str
    timestamp: str  # ISO UTC string, e.g. "2025-07-03T14:00:00Z"
