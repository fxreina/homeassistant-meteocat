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
                        "text": {}
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
            return self.async_create_entry(title="", data=user_input)

        schema = vol.Schema(
            {
#                vol.Required("location", default=self.config_entry.data.get("location")): selector(
#                    {
#                        "text": {}
#                    }
#                )
                vol.Required(
                    "location",
                    default=self.options.get("location", "")  # Use self.options instead of config_entry.data
                ): selector(
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

        return self.async_show_form(step_id="init", data_schema=schema, errors=errors)
