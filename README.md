![GitHub Activity](https://img.shields.io/github/commit-activity/y/fxreina/homeassistant-meteocat.svg?label=commits)
[![Stable](https://img.shields.io/github/v/release/fxreina/homeassistant-meteocat.svg)](https://github.com/fxreina/homeassistant-meteocat/releases/latest)

# homeassistant-meteocat
<a href="https://www.meteo.cat/" target="_blank"><img src="https://brands.home-assistant.io/meteocat/logo.png" alt="imagen" height="150"></a> <img src="assets/dades_obertes.png" alt="imagen" height="150">

Esta integración para Home Assistant te permite integrar la previsión meteorológica emitida por Meteocat (la agencia meteorológica local de Catalunya) a través del portal de datos abiertos de la Generalitat de Catalunya. Concretamente, se consulta el servicio https://static-m.meteo.cat/content/opendata/ctermini_comarcal.xml que proporciona la previsión meteorológica por comarcas para los próximos dos días (el día en curso == hoy y el siguiente == mañana).

La integración está todavía en desarrollo y no está lista para su uso productivo.

## Índice de contenidos

1. [Ejemplo de Dashboard](#Ejemplo-de-Dashboard)<br>
2. [Instalación](#Instalación)<br>
3. [FAQ](#FAQ)

## Ejemplo de Dashboard

![Dashboard](assets/dashboard.png)

## Instalación

1. Accede a la carpeta de config de tu home assistant.
2. Crea la carpeta "custom_components/meteocat"
3. Copia el contenido del repositorio en esa carpeta.
4. Reinicia home assistant desde "Developer Tools / Yaml / Check and Restart / Restart"
5. Accede a "Settings / Devices and Services / Integrations / Add integration.
6. Localiza la integración de "Meteocat".

Configuración:

Selecciona la comarca para la que quieres recibir la previsión meteorológica:

![imagen](assets/select_region.png)

## FAQ

**xxx**

> xxx.
