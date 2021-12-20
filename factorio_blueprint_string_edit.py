import json
from os import name
import zlib
import base64
import math

original_bp_string = '0eNrVktGqgzAMht8l13WcVofaVxki6sJOmE2lVpkM3/1Yx8HBxi62q13mb/L/yUevULcDdo7Yl7W1Z9DXTelBH+7K8EaN5Zvc04mrNmh+6hA0kEcDArgyoTJ4pMFE2GLjHTVRZ1uEWQDxES+g5VwIQPbkCW9+azGVPJga3dLw2klAZ/tl2HLYIBgm8W4vYAIdyTjd7ZcoRjr91nZwIUAVs3gIUZ+ExI8hsghnrSD0HTcBI7p+tVGZTNJcpUmW5UqmG5CfsN6XoFbZRiFfKLx9tHw2Ga3/UEDVeBqx/Ofzwm/+A0mG6WE='
bp_json = json.loads(zlib.decompress(base64.b64decode(original_bp_string[1:])).decode('utf8'))
print(bp_json)
# for mine in normaltemp():
#     if mine['name'] == 'electric-mining-drill':
#         print(mine)
# for mine in fliptemp():
#     if mine['name'] == 'electric-mining-drill':
#         print(mine)
# there is one entity in the blueprint, it's an assembler with a item request for 2 prod-3 modules and no recipe set
# for the fields of the blueprint json see https://wiki.factorio.com/Blueprint_string_format
# bp_json['blueprint']['entities'][0]['items'] = {'copper-plate': 200} # overwrites existing item request
# bp_json['blueprint']['entities'][0]['recipe'] = 'copper-cable' # creates new key/value pair

test = {
    'blueprint_book': {
        'blueprints': [{
            'blueprint': {
                'icons': [{
                    'signal': {
                        'type': 'item',
                        'name': 'medium-electric-pole'
                    },
                    'index': 1
                }],
                'entities': [{
                    'entity_number': 1,
                    'name': 'medium-electric-pole',
                    'position': {
                        'x': 143.5,
                        'y': -137.5
                    }
                }, {
                    'entity_number': 2,
                    'name': 'medium-electric-pole',
                    'position': {
                        'x': 143.5,
                        'y': -133.5
                    },
                    'neighbours': [1]
                }],
                'item': 'blueprint',
                'version': 281479274889217
            },
            'index': 0
        }, {
            'blueprint': {
                'icons': [{
                    'signal': {
                        'type': 'item',
                        'name': 'medium-electric-pole'
                    },
                    'index': 1
                }],
                'entities': [{
                    'entity_number': 1,
                    'name': 'medium-electric-pole',
                    'position': {
                        'x': 128.5,
                        'y': -139.5
                    }
                }],
                'item': 'blueprint',
                'version': 281479274889217
            },
            'index': 1
        }],
        'item': 'blueprint-book',
        'active_index': 0,
        'version': 281479274889217
    }
}
changed_bp_string = '0' + base64.b64encode(zlib.compress(bytes(json.dumps(test), 'utf8'))).decode('utf8')
print(changed_bp_string)
