"""The Syncleo Kettle integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from .coordinator import PolarisDataUpdateCoordinator
from .discovery import SyncleoDiscovery

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)

PLATFORMS: list[Platform] = [Platform.WATER_HEATER, Platform.SWITCH, Platform.LIGHT, Platform.SENSOR, Platform.CLIMATE]

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the Syncleo Kettle component."""
    # Предварительно настраиваем discovery с shared Zeroconf
    try:
        from homeassistant.components.zeroconf import async_get_instance
        zc = await async_get_instance(hass)
        discovery = SyncleoDiscovery.get_instance()
        discovery.set_zeroconf_instance(zc)
        
        # Запускаем discovery заранее
        await hass.async_add_executor_job(discovery.start_discovery)
        _LOGGER.info("Pre-started Syncleo device discovery with shared Zeroconf")
    except Exception as err:
        _LOGGER.warning("Could not pre-start discovery: %s", err)
    
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Syncleo Kettle from a config entry."""
    
    mac = entry.data["mac"].replace(":", "").lower()
    device_token = entry.data["device_token"]
    
    coordinator = PolarisDataUpdateCoordinator(hass, mac, device_token)
    
    # Get shared Zeroconf instance
    try:
        from homeassistant.components.zeroconf import async_get_instance
        zc = await async_get_instance(hass)
    except ImportError:
        _LOGGER.warning("Zeroconf not available, falling back to internal instance")
        zc = None
    
    # Setup the kettle connection
    try:
        await coordinator.async_setup(zc)
        await coordinator.async_config_entry_first_refresh()
    except Exception as err:
        _LOGGER.error("Device %s setup failed: %s", mac, err)
        await coordinator.shutdown()
        raise ConfigEntryNotReady(f"Device setup failed: {err}") from err
    
    hass.data.setdefault(entry.domain, {})
    hass.data[entry.domain][entry.entry_id] = coordinator
    
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        coordinator: PolarisDataUpdateCoordinator = hass.data[entry.domain].pop(entry.entry_id)
        await coordinator.shutdown()
    

    return unload_ok
