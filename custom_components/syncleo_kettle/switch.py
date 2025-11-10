"""Switch platform for Syncleo Kettle."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.switch import SwitchEntity
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
    """Set up Syncleo Kettle switch platform from config entry."""
    coordinator: PolarisDataUpdateCoordinator = hass.data[DOMAIN][config_entry.entry_id]
    # Добавляем только тем чайникам, у которых есть подсветка
    if coordinator.device_info['model_id'] in POLARIS_KETTLE_WITH_BACKLIGHT_TYPE:
        switches = [
            ChildLockSwitch(coordinator, config_entry.entry_id),
            VolumeSwitch(coordinator, config_entry.entry_id),
            BacklightSwitch(coordinator, config_entry.entry_id),
        ]
    else:
        switches = [
            ChildLockSwitch(coordinator, config_entry.entry_id),
            VolumeSwitch(coordinator, config_entry.entry_id),
            BSSSwitch(coordinator, config_entry.entry_id),
        ]
    
    async_add_entities(switches)

class ChildLockSwitch(SwitchEntity):
    """Representation of a Child Lock switch."""
    
    _attr_has_entity_name = True
    _attr_translation_key = "child_lock"
    
    def __init__(self, coordinator: PolarisDataUpdateCoordinator, entry_id: str) -> None:
        """Initialize the Child Lock switch."""
        self.coordinator = coordinator
        self._entry_id = entry_id
        self._attr_unique_id = f"{coordinator._mac}_child_lock"
        self._attr_device_info = coordinator.device_info

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.data.get("connected", False)

    @property
    def is_on(self) -> bool:
        """Return true if child lock is enabled."""
        return self.coordinator.data.get("child_lock", False)

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the child lock on."""
        await self.coordinator.async_set_child_lock(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the child lock off."""
        await self.coordinator.async_set_child_lock(False)

    async def async_added_to_hass(self) -> None:
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    @property
    def should_poll(self) -> bool:
        """No need to poll, coordinator notifies of updates."""
        return False

class VolumeSwitch(SwitchEntity):
    """Representation of a Volume switch."""
    
    _attr_has_entity_name = True
    _attr_translation_key = "volume"
    
    def __init__(self, coordinator: PolarisDataUpdateCoordinator, entry_id: str) -> None:
        """Initialize the Volume switch."""
        self.coordinator = coordinator
        self._entry_id = entry_id
        self._attr_unique_id = f"{coordinator._mac}_volume"
        self._attr_device_info = coordinator.device_info

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.data.get("connected", False)

    @property
    def is_on(self) -> bool:
        """Return true if volume is enabled."""
        return self.coordinator.data.get("volume", False)

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the volume on."""
        await self.coordinator.async_set_volume(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the volume off."""
        await self.coordinator.async_set_volume(False)

    async def async_added_to_hass(self) -> None:
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    @property
    def should_poll(self) -> bool:
        """No need to poll, coordinator notifies of updates."""
        return False

class BSSSwitch(SwitchEntity):
    """Representation of a Volume switch."""
    
    _attr_has_entity_name = True
    _attr_translation_key = "BSS"
    
    def __init__(self, coordinator: PolarisDataUpdateCoordinator, entry_id: str) -> None:
        """Initialize the Volume switch."""
        self.coordinator = coordinator
        self._entry_id = entry_id
        self._attr_unique_id = f"{coordinator._mac}_BSS"
        self._attr_device_info = coordinator.device_info

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.data.get("connected", False)

    @property
    def is_on(self) -> bool:
        """Return true if volume is enabled."""
        return self.coordinator.data.get("BSS", False)

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the BSS on."""
        await self.coordinator.async_set_BSS(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the BSS off."""
        await self.coordinator.async_set_BSS(False)

    async def async_added_to_hass(self) -> None:
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    @property
    def should_poll(self) -> bool:
        """No need to poll, coordinator notifies of updates."""
        return False

class BacklightSwitch(SwitchEntity):
    """Representation of a Backlight switch."""
    
    _attr_has_entity_name = True
    _attr_translation_key = "backlight"
    
    def __init__(self, coordinator: PolarisDataUpdateCoordinator, entry_id: str) -> None:
        """Initialize the Backlight switch."""
        self.coordinator = coordinator
        self._entry_id = entry_id
        self._attr_unique_id = f"{coordinator._mac}_backlight"
        self._attr_device_info = coordinator.device_info

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.data.get("connected", False)

    @property
    def is_on(self) -> bool:
        """Return true if backlight is enabled."""
        return self.coordinator.data.get("backlight", False)

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn the backlight on."""
        await self.coordinator.async_set_backlight(True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn the backlight off."""
        await self.coordinator.async_set_backlight(False)

    async def async_added_to_hass(self) -> None:
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    @property
    def should_poll(self) -> bool:
        """No need to poll, coordinator notifies of updates."""
        return False

