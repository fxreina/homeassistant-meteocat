import logging
import aiohttp
import async_timeout
import unicodedata
import xml.etree.ElementTree as ET

from homeassistant.components.sensor import SensorEntity
#from homeassistant.const import TEMP_CELSIUS
from homeassistant.const import UnitOfTemperature
from .const import DOMAIN
from .const import PRECIPITATION_MAPPING
from .const import FORECAST_MAPPING
from .const import REGIONS  # Import the REGIONS list


_LOGGER = logging.getLogger(__name__)

URL = "http://static-m.meteo.cat/content/opendata/ctermini_comarcal.xml"

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the Meteocat sensors."""
    region_id = entry.data.get("location")
#   async_add_entities([MeteocatSensor(region_id, day) for day in [1, 2]], True)
    async_add_entities([
        MeteocatSensor(region_id, day=1),
        MeteocatSensor(region_id, day=2)
    ])

class MeteocatSensor(SensorEntity):
    """Representation of a Meteocat Sensor."""

    def __init__(self, region_id, day):
        """Initialize the sensor."""
        self._region_id = str(region_id)
        self._day = day
        self._day_name = "Day1" if day == 1 else "Day2"
         # Get location name from REGIONS
        location_name = next((name for id, name in REGIONS if id == self._region_id), f"Region {self._region_id}")
         # Normalize name (remove accents, convert spaces to underscores, and lowercase)
        self._location_name = unicodedata.normalize("NFKD", location_name).encode("ASCII", "ignore").decode("ASCII")
         #self._location_name = self._location_name.lower().replace(" ", "_")       
        self._state = None
        self._attr_unique_id = f"meteocat_forecast_{self._location_name.lower().replace(' ', '_')}_{self._day_name.lower()}"
        self._attr_name = f"Meteocat Forecast {location_name} {self._day_name}"
        self._attributes = {}

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._attr_name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

    async def async_update(self):
        """Fetch new state data for the sensor."""
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(10):
                    async with session.get(URL) as response:
                        xml_text = await response.text()
                        self._parse_xml(xml_text)
        except Exception as e:
            _LOGGER.error("Error fetching data: %s", e)
            self._state = None

    def _parse_xml(self, xml_data):
        root = ET.fromstring(xml_data)

        # Find the correct region
        forecast = root.find(f".//prediccio[@idcomarca='{self._region_id}']")
        if forecast is not None:
            # Get all "variable" elements (each day has one)
            variables = forecast.findall("variable")

            # Convert self._day to integer before comparing
            day_index = int(self._day) - 1
            
            # Ensure the requested day exists

            if len(variables) > day_index: # Use '>' instead of '>=' to avoid off-by-one errors
                variable = variables[day_index]
                if variable is not None:
                     # Extract weather symbols and remove ".png"
                    morningforecast = variable.get("simbolmati", "").replace(".png", "")
                    afternoonforecast = variable.get("simboltarda", "").replace(".png", "")
                    icon_morning = f"https://static-m.meteo.cat/assets-w3/images/meteors/estatcel/{morningforecast}.svg" if morningforecast else None
                    icon_afternoon = f"https://static-m.meteo.cat/assets-w3/images/meteors/estatcel/{afternoonforecast}.svg" if afternoonforecast else None
                    
                     # Get descriptions from FORECAST_MAPPING (default to empty string if not found)
                    desc_morning = FORECAST_MAPPING.get(morningforecast, "").capitalize()
                    desc_afternoon = FORECAST_MAPPING.get(afternoonforecast, "").capitalize()                    

                     # Set state: concatenate if different, otherwise use one
                    self._state = desc_morning if desc_morning == desc_afternoon else f"{desc_morning} / {desc_afternoon}"

                     # Map IDs to descriptive values for precipitation
                    precip_morning_id = variable.get("probprecipitaciomati")
                    precip_afternoon_id = variable.get("probprecipitaciotarda")
                    precipitation_morning = PRECIPITATION_MAPPING.get(precip_morning_id, "Unknown")
                    precipitation_afternoon = PRECIPITATION_MAPPING.get(precip_afternoon_id, "Unknown")

                    self._attributes = {
                        "min_temp": variable.get("tempmin"),
                        "max_temp": variable.get("tempmax"),
                        "date": variable.get("data"),
                        "morning_precip": precipitation_morning,
                        "morning_intensity": variable.get("intensitatprecimati"),
                        "morning_accum": variable.get("precipitacioacumuladamati"),
                        "afternoon_precip": precipitation_afternoon,
                        "afternoon_intensity": variable.get("intensitatprecitarda"),
                        "afternoon_accum": variable.get("precipitacioacumuladatarda"),
                        "icon_morning": icon_morning,
                        "icon_afternoon": icon_afternoon,
                }
            else:
                _LOGGER.warning("No forecast available for day %s in region %s", self._day, self._region_id)
                self._state = None
        else:
            _LOGGER.warning("No forecast found for region %s", self._region_id)
            self._state = None