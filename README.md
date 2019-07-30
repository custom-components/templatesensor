# templatesensor

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE.md)

[![hacs][hacsbadge]](hacs)
![Project Maintenance][maintenance-shield]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

_Add template sensors from the UI._

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `templatesensor`.
4. Download _all_ the files from the `custom_components/templatesensor/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Custom Template Sensor"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/templatesensor/.translations/en.json
custom_components/templatesensor/__init__.py
custom_components/templatesensor/config_flow.py
custom_components/templatesensor/const.py
custom_components/templatesensor/manifest.json
custom_components/templatesensor/sensor.py
```

## Configuration

Configuration are done through the UI.

"Configuration" --> "Integrations" --> "+" --> "Custom Template Sensor"

![example][exampleimg]

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[templatesensor]: https://github.com/custom-components/templatesensor
[buymecoffee]: https://www.buymeacoffee.com/ludeeus
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/custom-components/templatesensor.svg?style=for-the-badge
[commits]: https://github.com/custom-components/templatesensor/commits/master
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: https://raw.githubusercontent.com/custom-components/templatesensor/master/example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/custom-components/templatesensor.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Joakim%20Sørensen%20%40ludeeus-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/custom-components/templatesensor.svg?style=for-the-badge
[releases]: https://github.com/custom-components/templatesensor/releases
