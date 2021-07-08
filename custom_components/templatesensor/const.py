"""Constants for templatesensor."""
from homeassistant.components.sensor import DEVICE_CLASSES

DEVICE_CLASSES = {device_class: device_class for device_class in DEVICE_CLASSES}
DOMAIN = "templatesensor"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.2.0"
PLATFORMS = ["sensor"]
REQUIRED_FILES = [
    "translations/en.json",
    "const.py",
    "config_flow.py",
    "manifest.json",
    "sensor.py",
]
ISSUE_URL = "https://github.com/custom-components/templatesensor/issues"
