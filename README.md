![GitHub Activity](https://img.shields.io/github/commit-activity/y/fxreina/homeassistant-meteocat.svg?label=commits)
[![Stable](https://img.shields.io/github/v/release/fxreina/homeassistant-meteocat.svg)](https://github.com/fxreina/homeassistant-meteocat/releases/latest)

# homeassistant-meteocat
<a href="https://www.meteo.cat/" target="_blank"><img src="https://brands.home-assistant.io/meteocat/logo.png" alt="imagen" height="150"></a> <img src="assets/dades_obertes.png" alt="imagen" height="150">

This integration for Home Assistant allows you to incorporate the weather forecast provided by Meteocat (the local meteorological agency of Catalonia) through the open data portal of the Generalitat de Catalunya. Specifically, it queries the service https://static-m.meteo.cat/content/opendata/ctermini_comarcal.xml, which provides the regional weather forecast for the next two days (the current day == today and the following day == tomorrow).

The integration is still under development and is not ready for productive use.

## Table of Contents

1. [Dashboard Example](#Dashboard-Example)<br>
2. [Installation](#Installation)<br>
4. [Quick Start](#Quick-Start)<br>
3. [FAQ](#FAQ)

## Installation

1. Copy contents of custom_components/meteocat/ to custom_components/meteocat/ in your Home Assistant config folder.
4. Restart Home Assistant from "Developer Tools / Yaml / Check and Restart / Restart"
5. Get into "Settings / Devices and Services / Integrations / Add integration".
6. Find the "Meteocat" custom integration and install it.

Configuration:

Select the region (Comarca) for which you want to receive the weather forecast.

![imagen](assets/select_region.png)

## Installation using HACS
[HACS](https://github.com/custom-components/hacs) is a community store for Home Assistant. Although it is planned to solve this in future, for the time being you CANNOT install yet this Meteocat integration from the HACS store.

## Quick Start
This custom component creates two sensors that will deliver the weather forecast for today and tomorrow for the selected region.

<img src="assets/entities.png" alt="imagen">

Each sensor will have attributes showing the max and min forecasted temperatures and the probability and intensity of precipitation splitted by morning and afternoon.

<img src="assets/attributes.png" alt="imagen">

## FAQ

**xxx**

> xxx.
