import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.selector import selector

from .const import DOMAIN
from .const import REGIONS

_LOGGER = logging.getLogger(__name__)

class MeteocatConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Meteocat integration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step where the user selects a location."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title=user_input["location"], data=user_input)

        # Define the user interface form schema
        schema = vol.Schema(
            {
                vol.Required("location"): selector(
                    {
                        "select": {
                            "options": [
                                {"value": code, "label": description} for code, description in REGIONS
                            ]
                        }
                    }
                )
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=schema, errors=errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Return the options flow handler."""
        return MeteocatOptionsFlowHandler(config_entry)


class MeteocatOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options for Meteocat integration."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        # Remove direct assignment of self.config_entry (deprecated)
        self.options = dict(config_entry.options)
        
    async def async_step_init(self, user_input=None):
        """Manage the options for the custom integration."""
        errors = {}

        if user_input is not None:
            # Save the user input (update interval) in the options
            return self.async_create_entry(title="", data=user_input)

        schema = vol.Schema(
            {
                vol.Required(
                    "update_interval",
                    default=self.options.get("update_interval", 60)  # Default to 60 minutes if not set
                ): vol.All(int, vol.Range(min=1, max=1440))  # Enforce a range of 1 to 1440 minutes
            }
        )

        return self.async_show_form(
            step_id="init", 
            data_schema=schema, 
            errors=errors,
        )