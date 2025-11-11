"""Climate platform for Syncleo Kettle."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACMode,
)
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .coordinator import PolarisDataUpdateCoordinator
from .const import DOMAIN
from .protocol import PowerType

_LOGGER = logging.getLogger(__name__)

SUPPORTED_TEMPERATURES = list(range(40, 101, 5))  # 40°C to 100°C in 5°C steps

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigType,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Syncleo Kettle climate platform from config entry."""
    coordinator: KettleDataUpdateCoordinator = hass.data[DOMAIN][config_entry.entry_id]
    
    async_add_entities([SyncleoKettleClimate(coordinator, config_entry.entry_id)])

class SyncleoKettleClimate(ClimateEntity):
    """Representation of a Syncleo Kettle as a climate device."""
    
    _attr_has_entity_name = True
    _attr_name = None
    
    def __init__(self, coordinator: KettleDataUpdateCoordinator, entry_id: str) -> None:
        """Initialize the climate device."""
        self.coordinator = coordinator
        self._entry_id = entry_id
        self._attr_unique_id = f"{coordinator._mac}_climate"
        self._attr_device_info = coordinator.device_info
        
        # Static attributes
        self._attr_temperature_unit = UnitOfTemperature.CELSIUS
        self._attr_supported_features = (
            ClimateEntityFeature.TARGET_TEMPERATURE |
            ClimateEntityFeature.TURN_ON |
            ClimateEntityFeature.TURN_OFF
        )
        self._attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT, HVACMode.COOL, HVACMode.HEAT_COOL]
        self._attr_min_temp = 5
        self._attr_max_temp = 75
        self._attr_target_temperature_step = 1

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.data.get("connected", False)

    @property
    def current_temperature(self) -> float | None:
        """Return the current temperature."""
        return self.coordinator.data.get("current_temperature")

    @property
    def target_temperature(self) -> float | None:
        """Return the temperature we try to reach."""
        return self.coordinator.data.get("target_temperature")

    @property
    def hvac_mode(self) -> HVACMode:
        """Return current operation mode."""
        power_type = self.coordinator.data.get("power_type")
        if power_type == PowerType.OFF:
            return HVACMode.OFF
        else:
            return HVACMode.HEAT

    @property
    def hvac_action(self) -> str | None:
        """Return current HVAC action."""
        if self.coordinator.data.get("is_heating", False):
            return "heating"
        elif self.hvac_mode == HVACMode.HEAT:
            return "idle"
        else:
            return "off"

    async def async_set_temperature(self, **kwargs: Any) -> None:
        """Set new target temperature."""
        if (temperature := kwargs.get(ATTR_TEMPERATURE)) is not None:
            await self.coordinator.async_set_temperature(int(temperature))

    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None:
        """Set new operation mode."""
        if hvac_mode == HVACMode.OFF:
            await self.coordinator.async_set_power(PowerType.OFF)
        else:  # HVACMode.HEAT
            # Use CUSTOM mode to allow custom temperature
            await self.coordinator.async_set_power(PowerType.ON)

    async def async_added_to_hass(self) -> None:
        """When entity is added to hass."""
        self.async_on_remove(
            self.coordinator.async_add_listener(self.async_write_ha_state)
        )

    @property
    def should_poll(self) -> bool:
        """No need to poll, coordinator notifies of updates."""

        return False


