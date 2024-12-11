from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

from .entity import IntegrationInstaEntity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import InstaDataUpdateCoordinator
    from .data import IntegrationInstaConfigEntry

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="insta_follower",
        name="Insta_follower_count",
        icon="mdi:instagram",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: IntegrationInstaConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities(
        IntegrationInstaSensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class IntegrationInstaSensor(IntegrationInstaEntity, SensorEntity):
    _attr_state_class = "measurement"  # Add state_class attribute
    
    def __init__(
        self,
        coordinator: InstaDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> int | None:
        """Return the native value of the sensor."""
        #return self.coordinator.data.get("body")
        #return self.coordinator.data.get("data", {}).get("follower_count")
        follower_count = self.coordinator.data.get("data", {}).get("follower_count")
        if follower_count is not None:
            try:
                return int(follower_count)  # Try convert to int
            except ValueError:
                return None  # If no success return null
        return None
        
    @property
    def unit_of_measurement(self) -> str | None:
        return "followers"  # Set unit to 'subs'