import json
from os import name
import zlib
import base64
def bpana():
    original_bp_string = '0eNqdk9uKhDAMQP8lz3VAx2t/ZVkWL0ECvVHrsjL471udUYYdB1efJJicnKbNDSrRo7GkHPAbdKo0gdNBa6mZ4h/gKYMBeDYyoFqrDviHT6NWlWJKcINB4EAOJTBQpZwiFFg7S3UgSZFqg8aSEDARVIMeGY6fDFA5coR34BwMX6qXFVqfsINiYHTnq7V6SIaXZNaMLolv05D1VfPfeGQv9OgoPX7Qw//Qryu996e1rdX+G1Qo3Hvw9S/YKy6TVaZ3sNEnXvtIbKiXwXoYowW+9kqeem3gkgPaxb627t0b7/Ts3abb4tkB8QUVn5h3fvbVJNvexQHvdN97GbjfrHkZ+dNiM/hG290L8jDOiiiL87yIwmwcfwH4BlKu'
    bp_json = json.loads(zlib.decompress(base64.b64decode(original_bp_string[1:])).decode('utf8'))
    modentities = bp_json['blueprint']['entities']
    return modentities
def bp():
    original_bp_string = '0eNqdk9uKhDAMQP8lz3VAx2t/ZVkWL0ECvVHrsjL471udUYYdB1efJJicnKbNDSrRo7GkHPAbdKo0gdNBa6mZ4h/gKYMBeDYyoFqrDviHT6NWlWJKcINB4EAOJTBQpZwiFFg7S3UgSZFqg8aSEDARVIMeGY6fDFA5coR34BwMX6qXFVqfsINiYHTnq7V6SIaXZNaMLolv05D1VfPfeGQv9OgoPX7Qw//Qryu996e1rdX+G1Qo3Hvw9S/YKy6TVaZ3sNEnXvtIbKiXwXoYowW+9kqeem3gkgPaxb627t0b7/Ts3abb4tkB8QUVn5h3fvbVJNvexQHvdN97GbjfrHkZ+dNiM/hG290L8jDOiiiL87yIwmwcfwH4BlKu'
    bp_json = json.loads(zlib.decompress(base64.b64decode(original_bp_string[1:])).decode('utf8'))
    modentities = bp_json['blueprint']['entities']
    return bp_json

# for enti in bp_json['blueprint']['entities']:
#     if enti['name'] == 'electric-mining-drill':

#         print(enti['position'])
def extendminer():
    modentities = bpana()
    outentity = []
    outitem = ''
    slimit = 75
    

    for i in range(int(76/2)):
        # print(i)
        setnum = 9
        stepgauge = 6
        for item in bpana():
            outitem = item
            # print(outitem)
            outitem['entity_number'] = item['entity_number'] + i*setnum
            outitem['position']['x'] = item['position']['x'] + i*stepgauge

            if outitem["name"] == "underground-belt" and i//12:
                outitem["name"] = 'fast-underground-belt'
                if i//25:
                    outitem["name"] ='express-underground-belt'


            # print(modentities)

            outentity.append(outitem)
    # print(outentity)
    outjson = bp()
    outjson['blueprint']['entities'] = outentity
    with open('mod.json','w') as file:
        json.dump(outjson,file)
        # file.write(json.dumps(outjson))
        print('0' + base64.b64encode(zlib.compress(bytes(json.dumps(outjson), 'utf8'))).decode('utf8'))
extendminer()
# there is one entity in the blueprint, it's an assembler with a item request for 2 prod-3 modules and no recipe set
# for the fields of the blueprint json see https://wiki.factorio.com/Blueprint_string_format
# bp_json['blueprint']['entities'][0]['items'] = {'copper-plate': 200} # overwrites existing item request
# bp_json['blueprint']['entities'][0]['recipe'] = 'copper-cable' # creates new key/value pair


# changed_bp_string = '0' + base64.b64encode(zlib.compress(bytes(json.dumps(bp_json), 'utf8'))).decode('utf8')
# print(changed_bp_string)
