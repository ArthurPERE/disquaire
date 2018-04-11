# from django.db import models

ARTISTS = {
  'francis-cabrel': {'name': 'Francis Cabrel'},
  'lej': {'name': 'Elijay'},
  'rosana': {'name': 'Rosana'},
  'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
}


ALBUMS = [
  {'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  {'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
  {'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]},
  {'name': 'Luna Nueva1', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]},
  {'name': 'Luna Nueva2', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
]