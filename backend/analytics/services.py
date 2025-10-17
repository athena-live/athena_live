"""Service layer for the analytics app."""
from typing import Any, Dict


def track_placeholder(event: str, payload: Dict[str, Any]) -> None:
    """Stub for analytics tracking."""
    _ = (event, payload)
