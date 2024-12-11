from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import IntegrationInstaApiClient
    from .coordinator import InstaDataUpdateCoordinator


type IntegrationInstaConfigEntry = ConfigEntry[IntegrationInstaData]


@dataclass
class IntegrationInstaData:

    client: IntegrationInstaApiClient
    coordinator: InstaDataUpdateCoordinator
    integration: Integration
