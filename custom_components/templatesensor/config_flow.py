"""Adds config flow for templatesensor."""
import logging

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import template as templater

from .const import DEVICE_CLASSES, DOMAIN

_LOGGER = logging.getLogger(__name__)


class TemplateSensorFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for templatesensor."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    def __init__(self):
        """Initialize."""
        self._errors = {}

    async def async_step_user(self, user_input={}):
        """Handle a flow initialized by the user."""
        self._errors = {}
        if user_input is not None:
            valid = await self._validate_template(user_input["template"])
            if valid:
                return self.async_create_entry(
                    title=user_input["name"], data=user_input
                )
            else:
                self._errors["base"] = "template"

            return await self._show_config_form(user_input)

        return await self._show_config_form(user_input)

    async def _show_config_form(self, user_input):
        """Show the configuration form to edit location data."""

        # Defaults
        name = ""
        template = ""
        icon = ""
        unit = ""
        device_class = ""

        if user_input is not None:
            if "name" in user_input:
                name = user_input["name"]
            if "template" in user_input:
                template = user_input["template"]
            if "icon" in user_input:
                icon = user_input["icon"]
            if "unit" in user_input:
                unit = user_input["unit"]
            if "device_class" in user_input:
                device_class = user_input["device_class"]

        data_schema = vol.Schema(
            {
                vol.Required("name", default=name): str,
                vol.Required("template", default=template): str,
                vol.Optional("icon", default=icon): str,
                vol.Optional("unit", default=unit): str,
                vol.Optional("device_class", default=device_class): vol.In(
                    DEVICE_CLASSES
                ),
            }
        )
        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=self._errors
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return OptionsFlowHandler(config_entry)

    async def _validate_template(self, template):
        """Return true if template is valid."""
        try:
            templater.Template(template, self.hass).async_render()
            return True
        except Exception as exception:  # pylint: disable=broad-except
            _LOGGER.error(exception)
            pass
        return False


class OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        """Initialize UniFi options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data_schema = vol.Schema(
            {
                vol.Required(
                    "name", default=self.config_entry.options.get("name")
                ): str,
                vol.Required(
                    "template", default=self.config_entry.options.get("template")
                ): str,
                vol.Optional(
                    "icon",
                    description={
                        "suggested_value": self.config_entry.options.get("icon")
                    },
                ): str,
                vol.Optional(
                    "unit",
                    description={
                        "suggested_value": self.config_entry.options.get("unit")
                    },
                ): str,
                vol.Optional(
                    "device_class",
                    description={
                        "suggested_value": self.config_entry.options.get("device_class")
                    },
                ): vol.In(DEVICE_CLASSES),
            }
        )

        return self.async_show_form(step_id="user", data_schema=data_schema)
