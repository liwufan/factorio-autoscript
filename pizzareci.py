import json
import zlib
import base64
class pizzamenu:



    def u1norm():
        original_bp_string = '0eNqdk9uKhDAMQP8lz3VAx2t/ZVkWL0ECvVHrsjL471udUYYdB1efJJicnKbNDSrRo7GkHPAbdKo0gdNBa6mZ4h/gKYMBeDYyoFqrDviHT6NWlWJKcINB4EAOJTBQpZwiFFg7S3UgSZFqg8aSEDARVIMeGY6fDFA5coR34BwMX6qXFVqfsINiYHTnq7V6SIaXZNaMLolv05D1VfPfeGQv9OgoPX7Qw//Qryu996e1rdX+G1Qo3Hvw9S/YKy6TVaZ3sNEnXvtIbKiXwXoYowW+9kqeem3gkgPaxb627t0b7/Ts3abb4tkB8QUVn5h3fvbVJNvexQHvdN97GbjfrHkZ+dNiM/hG290L8jDOiiiL87yIwmwcfwH4BlKu'
        bp_json = json.loads(
            zlib.decompress(base64.b64decode(
                original_bp_string[1:])).decode('utf8'))
        modentities = bp_json['blueprint']['entities']
        return modentities

    def u1flip():
        original_bp_string = '0eNqdk9uKhDAMht8l13VBpx5fZRkWD0ECPVHrsjL47ludGRl2FFevSmj6/X+S5gaV6NFYUg6KG3SqNIHTQWupmeIfKBIGAxTpyIBqrTooPn0ataoUU4IbDEIB5FACA1XKKUKBtbNUB5IUqTZoLAkBE0E16JHheGWAypEjvAPnYPhSvazQ+oQdFAOjO/9aq4fJ8COebfrTyzRk/av5lo/sjR4dpfMHPfoP/XLWe+zpKzy+8HrfPdta7c+gQuG2UZe/Rn3Jz0kp0ztY0YkP6Dwbwk/oJAd0kv16dO82hNJFSGJDvQyWeRgt8F0sfilqBZcd8J3v92fbd372eyaTcb9Z8zIWL4vN4BttdzeQhTzNo5RnWR6F6Tj+Au60Uq8='
        bp_json = json.loads(
            zlib.decompress(base64.b64decode(
                original_bp_string[1:])).decode('utf8'))
        modentities = bp_json['blueprint']['entities']
        return modentities
    def n1norm():
        original_bp_string = '0eNqllNtugzAMQP/Fz6EiXMrlV6ZpomBVlkKCQjINIf59KZUYW4PWqE8Q5JxjE8czXITFQZM0UM9ArZIj1G8zjHSVjbh9M9OAUAMZ7IGBbPrbCgW2RlMb9SRJXqNOkxCwMCDZ4RfUfHlngNKQIbwD18X0IW1/Qe0C/kExGNTodit5y8ERo6o65Qwm95bl+Sl3ro6027qGZAt7UCThinOgIg1XpIGKbFMY3chxUNpEFxTGw+Zx/ANP/8ITDzx/6RS4U3ig5w1qXTPoq1bueZTznveYMtu6Tw7WgEdWbLIeO7J9tBUyKIE+YfFb6GGWQQWcnypAWXNQQfVSmx6cAY+fb5sqC+wazgPgeSg8eelOHf2PNCDlJDTlgDu6z9UDd1NzHbT1bi4z+EQ93gNKnhVVUmRlWSW8WJZvh3TcsA=='
        bp_json = json.loads(
            zlib.decompress(base64.b64decode(
                original_bp_string[1:])).decode('utf8'))
        modentities = bp_json['blueprint']['entities']
        return modentities

    recipe = {
        'allunder':{'step':6,'gauge':7,'desity':2,'positive':u1norm(),'negative':u1flip()},
        'basic':{'step':9,'gauge':7,'desity':1,'positive':n1norm(),'negative':n1norm()},
        'triway':{'step':6,'gauge':7,'desity':2,'positive':u1norm(),'negative':u1flip()},
        'basicsss':{}
    }

# print(pizzamenu.recipe['allunder']['step'])
