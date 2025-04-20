import logging
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.selector import selector

from .const import DOMAIN, REGIONS

_LOGGER = logging.getLogger(__name__)


class MeteocatConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Meteocat integration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step where the user selects a location."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title=user_input["location"], data=user_input)

        schema = vol.Schema(
            {
                vol.Required("location"): selector(
                    {
                        "select": {
                            "options": [
                                {"value": code, "label": description}
                                for code, description in REGIONS
                            ]
                        }
                    }
                )
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=schema, errors=errors
        )

    def async_get_options_flow(self, config_entry):
        """Return the options flow handler."""
        return MeteocatOptionsFlowHandler(config_entry)


class MeteocatOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options for Meteocat integration."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry
        self.options = dict(config_entry.options)

    async def async_step_init(self, user_input=None):
        """Manage the options for the custom integration."""
        errors = {}

        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        schema = vol.Schema(
            {
                vol.Required(
                    "update_interval",
                    default=self.options.get("update_interval", 60)
                ): vol.All(int, vol.Range(min=1, max=1440))
            }
        )

        return self.async_show_form(
            step_id="init",
            data_schema=schema,
            errors=errors,
        )
