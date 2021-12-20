import json
from os import name
import zlib
import base64
import math

original_bp_string = '0eNqFj80KgzAQhN9lzlGqaNW8SinFn6UsJKsksVQk715jL731OMvMN7M7BrPS4lgC9A4eZ/HQtx2en9KbdAvbQtDgQBYK0tukyNAYHI+ZZWF5ZpNjYxAVWCZ6QxfxrkASODB9gafYHrLagdxh+INSWGZ/pGdJGw5i2eW1wgad1ZdrXsdUcG7SPy8ovMj5M1S2RdV0ZVO1bVcWTYwfGn9Nnw=='
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


# changed_bp_string = '0' + base64.b64encode(zlib.compress(bytes(json.dumps(bp_json), 'utf8'))).decode('utf8')
# print(changed_bp_string)
