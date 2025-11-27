"""Mobile sync scaffolding.

Provides placeholder hooks for future offline-first synchronization between
mobile clients and the backend API.
"""

from typing import Any, Dict, List


class MobileSyncService:
    """Non-functional placeholder for sync orchestration."""

    def pull_changes(self, soldier_id: str) -> List[Dict[str, Any]]:
        """Fetch changes for a given profile (stub)."""
        return []

    def push_changes(self, soldier_id: str, changes: List[Dict[str, Any]]) -> None:
        """Accept client-side changes (stub)."""
        return None
