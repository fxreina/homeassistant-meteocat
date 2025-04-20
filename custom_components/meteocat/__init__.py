import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Meteocat from a config entry."""
    _LOGGER.info("Setting up Meteocat integration for %s", entry.data)

    # Store the config entry in Home Assistant's data registry
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = entry.data

    # Forward the setup to the sensor platform

    #await hass.config_entries.async_forward_entry_setups(entry, ["weather"])
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Handle removal of an entry."""
    _LOGGER.info("Unloading Meteocat integration for %s", entry.data)

    unload_ok = await hass.config_entries.async_forward_entry_unload(entry, "sensor")
    #unload_ok = await hass.config_entries.async_forward_entry_unload(entry, "weather")

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
