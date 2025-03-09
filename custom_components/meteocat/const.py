DOMAIN = "meteocat"

# Mapping for precipitation probabilities

REGIONS = [
    ("1", "Alt Camp"),
    ("2", "Alt Empordà"),
    ("3", "Alt Penedès"),
    ("4", "Alt Urgell"),
    ("5", "Alta Ribagorça"),
    ("6", "Anoia"),
    ("7", "Bages"),
    ("8", "Baix Camp"),
    ("9", "Baix Ebre"),
    ("10", "Baix Empordà"),
    ("11", "Baix Llobregat"),
    ("12", "Baix Penedès"),
    ("13", "Barcelonès"),
    ("14", "Berguedà"),
    ("15", "Cerdanya"),
    ("16", "Conca de Barberà"),
    ("17", "Garraf"),
    ("18", "Les Garrigues"),
    ("19", "Garrotxa"),
    ("20", "Gironès"),
    ("21", "Maresme"),
    ("22", "Montsià"),
    ("23", "Noguera"),
    ("24", "Osona"),
    ("25", "Pallars Jussà"),
    ("26", "Pallars Sobirà"),
    ("27", "Pla d'Urgell"),
    ("28", "Pla de l'Estany"),
    ("29", "Priorat"),
    ("30", "Ribera d'Ebre"),
    ("31", "Ripollès"),
    ("32", "Segarra"),
    ("33", "Segrià"),
    ("34", "La Selva"),
    ("35", "Solsonès"),
    ("36", "Tarragonès"),
    ("37", "Terra Alta"),
    ("38", "L'Urgell"),
    ("39", "Val d'Aran"),
    ("40", "Vallès Occidental"),
    ("41", "Vallès Oriental"),
    ("42", "Moianès"),
    ("43", "Lluçanès"),
# Add more locations here
]
# Optional: Sort the locations alphabetically by description
REGIONS = sorted(REGIONS, key=lambda x: x[1])

PRECIPITATION_MAPPING = {
    "1": "No se n'espera",
    "2": "No es descarta",
    "3": "Possible",
    "4": "Probable",
    "5": "Molt probable",
}