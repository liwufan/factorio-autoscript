import json
from os import name, read
import zlib
import base64
import math
import pizzareci

prodlevel = 9
menu = pizzareci.pizzamenu()
preferrecipe = 'basic'

def bp():
    original_bp_string = '0eNqdk9uKhDAMQP8lz3VAx2t/ZVkWL0ECvVHrsjL471udUYYdB1efJJicnKbNDSrRo7GkHPAbdKo0gdNBa6mZ4h/gKYMBeDYyoFqrDviHT6NWlWJKcINB4EAOJTBQpZwiFFg7S3UgSZFqg8aSEDARVIMeGY6fDFA5coR34BwMX6qXFVqfsINiYHTnq7V6SIaXZNaMLolv05D1VfPfeGQv9OgoPX7Qw//Qryu996e1rdX+G1Qo3Hvw9S/YKy6TVaZ3sNEnXvtIbKiXwXoYowW+9kqeem3gkgPaxb627t0b7/Ts3abb4tkB8QUVn5h3fvbVJNvexQHvdN97GbjfrHkZ+dNiM/hG290L8jDOiiiL87yIwmwcfwH4BlKu'
    bp_json = json.loads(
        zlib.decompress(base64.b64decode(
            original_bp_string[1:])).decode('utf8'))
    modentities = bp_json['blueprint']['entities']
    return bp_json

def bamboomaker(length, type):
    bottleneck = 900 / 30 / (1 + prodlevel / 10) / 2
    outentity = []
    outitem = ''
    # slimit = 75
    # print(bpp(menu.recipe[preferrecipe]['positive']))
    

    for i in range(length):
        menul = pizzareci.pizzamenu()

        # print(i)
        setnum = 9
        stepgauge = 6
        if length % 2:
            for item in menul.recipe[preferrecipe]['positive']:
                outitem = item
                outitem['entity_number'] = item['entity_number'] + i * setnum
                outitem['position']['x'] = item['position']['x'] + i * stepgauge

                if outitem["name"] == "underground-belt" and i / bottleneck >= 1:
                    outitem["name"] = 'fast-underground-belt'
                    if i / bottleneck >= 2:
                        outitem["name"] = 'express-underground-belt'
                outentity.append(outitem)
        else:
            for item in menul.recipe[preferrecipe]['negative']:
                outitem = item
                outitem['entity_number'] = item['entity_number'] + i * setnum
                outitem['position']['x'] = item['position']['x'] + i * stepgauge

                if outitem["name"] == "underground-belt" and i / bottleneck >= 1:
                    outitem["name"] = 'fast-underground-belt'
                    if i / bottleneck >= 2:
                        outitem["name"] = 'express-underground-belt'
                outentity.append(outitem)
        menul = 0
    outjson = bp()
    outjson['blueprint']['entities'] = outentity
    print(outentity)

    return outentity


def coodshifter(stick, x, y):
    for entity in stick:
        entity['position']['x'] += x
        entity['position']['y'] += y

    return stick


def pizza(dlist, lanes, gauge, step):
    roundminer = []
    temporder = 1

    for diorder in range(len(dlist)):
        if lanes % 2:
            nline = coodshifter(bamboomaker(dlist[diorder], preferrecipe),
                                (dlist[0] - dlist[diorder]) * step / 2,
                                diorder * gauge)
            for line in nline:
                line['entity_number'] = temporder
                temporder += 1
                roundminer.append(line)
            if diorder > 0:
                bline = coodshifter(bamboomaker(dlist[diorder], 'n'),
                                    (dlist[0] - dlist[diorder]) * step / 2,
                                    0 - diorder * gauge)
                for line in bline:
                    line['entity_number'] = temporder
                    temporder += 1
                    roundminer.append(line)
        else:
            nline = coodshifter(bamboomaker(dlist[diorder], 'n'),
                                (dlist[0] - dlist[diorder]) * step / 2,
                                diorder * gauge)
            for line in nline:
                line['entity_number'] = temporder
                temporder += 1
                roundminer.append(line)
            bvert = 0 - (diorder + 1) * gauge
            bline = coodshifter(bamboomaker(dlist[diorder], 'n'),
                                (dlist[0] - dlist[diorder]) * step / 2, bvert)
            for line in bline:
                line['entity_number'] = temporder
                temporder += 1
                roundminer.append(line)

    cablepole(roundminer)

    return roundminer


def cablepole(entities):
    polelist = []
    for entity in entities:
        if entity['name'] == 'medium-electric-pole':
            polelist.append(entity)
    for spole in polelist:
        for tpole in polelist:
            if spole['entity_number'] != tpole['entity_number']:
                # print(spole['position']['x']-tpole['position']['x'])
                a = (spole['position']['x'] - tpole['position']['x']) * (
                    spole['position']['x'] - tpole['position']['x'])
                b = (spole['position']['y'] - tpole['position']['y']) * (
                    spole['position']['y'] - tpole['position']['y'])
                c = math.sqrt(a + b)
                if c < 9:
                    spole['neighbours'] = [tpole['entity_number']]
        for et in entities:
            if et['entity_number'] == spole['entity_number']:
                et = spole
    return entities


def jsonwriter(entities):
    output = bp()
    output['blueprint']['entities'] = entities
    bstring = '0' + base64.b64encode(
        zlib.compress(bytes(json.dumps(entities), 'utf8'))).decode('utf8')
    # print(bstring)
    with open('stringbook', 'w') as bbook:
        bbook.write(bstring)
    with open('inspect.json', 'w') as jsfile:
        json.dump(entities, jsfile)


def cook(radius):
    doughlist = []
    # print(menu.recipe[preferrecipe])
    tilegauge = menu.recipe[preferrecipe]['gauge']
    tilestep = menu.recipe[preferrecipe]['step']
    lanesofpatch = int(math.ceil(radius * 2 / tilegauge))
    print(lanesofpatch)

    if lanesofpatch % 2:
        for j in range(lanesofpatch // 2 + 1):
            copysofiter = math.cos(math.asin(
                j * tilegauge / radius)) * radius / tilestep * 2
            doughlist.append(math.ceil(copysofiter))
    else:
        for j in range(lanesofpatch // 2):
            copysofiter = math.cos(math.asin(
                j * tilegauge / radius)) * radius / tilestep * 2
            doughlist.append(math.ceil(copysofiter))

    # print(doughlist)
    cpizza = pizza(doughlist, lanesofpatch, tilegauge, tilestep)
    # jsonwriter(cpizza)
    return cpizza


def pbox():
    return {
        'blueprint': {
            'icons': [{
                'signal': {
                    'type': 'item',
                    'name': 'electric-mining-drill'
                },
                'index': 1
            }],
            'entities': [],
            'item': 'blueprint',
            'version': 281479274889217
        }
    }


def manager(prodction):
    book = {
        'blueprint_book': {
            'blueprints': [],
            'item': 'blueprint-book',
            'label': 'pizza！',
            'icons': [{
                'signal': {
                    'type': 'item',
                    'name': 'electric-mining-drill'
                },
                'index': 1
            }],
            'active_index': 0,
            'version': 281479274889217
        }
    }
    maxminer = 2700 / 30 / (1 + prodction / 10) / 2
    maxrad = maxminer * 3  #charistic of the blueprint
    repeat = 5

    idx = 0
    while repeat < maxminer:
        pizzabox = pbox()
        pizzabox['blueprint']['entities'] = cook(repeat * 3)
        pizzabox['index'] = idx
        idx += 1
        book['blueprint_book']['blueprints'].append(pizzabox)
        repeat += 1

    jsonwriter(book)

    print(maxminer, maxrad)

    # print(prodction)


manager(prodlevel)
# with open('flip.json','w') as file:
#     json.dump(fliptemp(),file)
# print(normaltemp,fliptemp)
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
