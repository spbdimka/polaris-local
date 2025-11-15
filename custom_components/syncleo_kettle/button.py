"""Button platform for Syncleo Kettle."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.button import ButtonEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .coordinator import PolarisDataUpdateCoordinator
from .const import DOMAIN, POLARIS_KETTLE_WITH_BACKLIGHT_TYPE

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigType,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Syncleo Kettle button platform from config entry."""
    coordinator: PolarisDataUpdateCoordinator = hass.data[DOMAIN][config_entry.entry_id]
    # Добавим всем потому что хотим дебажить отправку команд
    buttons = [
        DebugButton(coordinator, config_entry.entry_id),
    ]
    
    async_add_entities(buttons)

class DebugButton(ButtonEntity):
    """Representation of a Debug button."""
    
    _attr_has_entity_name = True
    _attr_translation_key = "Send Debug"
    
    def __init__(self, coordinator: PolarisDataUpdateCoordinator, entry_id: str) -> None:
        """Initialize the Child Lock switch."""
        self.coordinator = coordinator
        self._entry_id = entry_id
        self._attr_unique_id = f"{coordinator._mac}_debug_button"
        self._attr_device_info = coordinator.device_info

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.data.get("connected", False)

    async def async_press(self, **kwargs: Any) -> None:
        """Send debug message."""
        await self.coordinator.async_send_tank(True)

    
    async def async_added_to_hass(self) -> None:
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    @property
    def should_poll(self) -> bool:
        """No need to poll, coordinator notifies of updates."""
        return False




