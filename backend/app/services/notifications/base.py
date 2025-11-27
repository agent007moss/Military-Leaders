"""Notification engine scaffolding (no real delivery in Phase 1).

Provides pure placeholders for future in-app, email, SMS, and push channels.
"""

from dataclasses import dataclass
from typing import Literal, Dict, Any


Channel = Literal["in_app", "email", "sms", "push"]


@dataclass
class NotificationMessage:
    recipient_id: str
    channel: Channel
    template_key: str
    context: Dict[str, Any]


class NotificationService:
    """Non-functional placeholder.

    All methods are stubs to keep call‑sites compiling without doing work.
    """

    def send(self, message: NotificationMessage) -> None:
        # TODO: implement delivery in later phases
        return None

    def schedule(self, message: NotificationMessage) -> None:
        # TODO: implement scheduling/cron integration in later phases
        return None
