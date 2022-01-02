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
    def l1setup():
        original_bp_string = '0eNqlXO1O40gQfBf/TlbzPT28ygmd+PBxlhIncpzTIcS7rwl7i0lsn7vq1y4IXOnpmpqeSoW36nF3ro9d0/bV3VvVPB3aU3X3x1t1al7ah93H9/rXY13dVU1f76tN1T7sP76qd/VT3zVP233TNu3L9rlrdrvqfVM17XP9b3Vn3+83Vd32Td/Unw+8fPH6Z3veP9bd8AP/86hNdTycht8+tB+vYXji1lrzI26q1+G/MfgfcQB7brrhdy8/E943NxhOj2HiF0ZYg+HVGGKVZQQ1RBZlFfE3xF8Pp357HprYvXSH4d/tY73rp1bKj8pw1xjDyv9Hm/Z47qsJyKSHdGEV5OHcz2BmANNzZQrA81H37JruFX1ZNpFLaQ1Q2NJaThVmLVBZ5BpmnR7TCLua/jto3z20p+Oh6+chFxs4BRHUEFkLAciIYdv1pSP7+rk577e/6Xg87OpJSH8twG3dvPz9eDh3H0dVCBsb7P0UFqAfxrDUEDVoKeSa6gWlOLJMp9cTKUqddHo5KeQp5/QziCSlSjqvLkvYk9QFPSZ5kjq9umRWl51aXfLN3vsmLslPCYvLSm3OWvV3okXQir8r3AxpAUp4w2EaBBO4ubivdvmy6lbhuOnYImT3ngM1EGgAlnOphZPLGbnBH+Jm4jAhbmbuJoDRRjhQjDZFO83aRaZOXbsNd/lASBOsuqyoLQuQFkvyMgDKMnZ7IF6GoL4Z2Jvz6NvhPdw1JE6d3yFSbtblTJh6bFJf2Zasg0k2ZO62C23eIOq6irauwnl/ZrojEdCE8TUa0YRoOUxkw0bH3XShDRs9BwpxMernj5KV01yM1BUeIk2iICHOZP1KBuUgF4VyJjBacm4IxMpkKKcCYUzizBGEMUmvMsIOjslrpwK50dJvQ4FLG2smb/UpUL4MRNYUlUeraMfipB1KRDuhJq0bIk45HSRh3rWbG9eS9k4iXvm6s6FcN2SPZr0sCKlE2VFveM6Mblk/XWT2apwDhQkJXAbuIu7r6Pey5hzOiTLebsemNbTIHKYgmEJZYkt1LnSwcKCCgIrR3smcW4KcgrCUIwaRRpy6LK8tC7FNSV5KAAwVIXkpUW+olGvMm7daXZianSRRuQmfpw8ByWp/bcm6n6QDZ4eCu1dvh2ZlXYULfFzqmnosF/GARKE4DhPZscVTRhu2Y0vgQCEulkj5VVhHE4cJdTQDFqNTDlpFKE8MpE3hQAULlBnGsoJoY42lMAXC1KtPCfTiqm2PciN4V0GG2ZSUCYxhhlHWGq3xUbTjqzVa56N4NYR2PilGeYwP+s4EreYGK2u0E0ix2lduKVMU26xAAlVYUbJUZmxu0LKWiomB29JSHigodkAOVTzbtERhYuTMjL2EdlQoULCj6vuNHwljWiUvjguTXZRRHzZXBz7GkCsLQ8JkZQllTWGIK5JWreYCT5w+8+HyNei3OWc68GFd5FKAcUaknTryMXb+8jo+ZM5fTFhr1KEPF9WVFSpMeKls8tMZhnMuIWnwpF0KbVskeGrpbYskT8eoGCN94GwgrKuRA8W6mjgfCOwqly1DuyqcFYR1tXCgUFeRgOrYgMLWdxRRBT5w9Qv0OlY5k6CwgcuhgcQN+k/jqafNoP84nnrwC2pPRLQnbkhUfG5uDApqH6SoXzn1uTpwxwJRMlaaomFiebMjEZBKHTtu2MYEYqmFFjwgllrYa2EMFCZETiClKoHuaKJAwY5myqvBOioUJtbRQlk1WEeB6GqmR/lkudBTmFG55Lj3+C7Pvd98/vGUu9HfWtlU/9Td6bNAGY674nIoMeTo399/AleJfcE='
        bp_json = json.loads(
            zlib.decompress(base64.b64decode(
                original_bp_string[1:])).decode('utf8'))
        modentities = bp_json['blueprint']['entities']
        return modentities


    recipe = {
        'allunder':{'step':6,'gauge':7,'desity':2,'items':9,'positive':u1norm(),'negative':u1flip()},
        'basic':{'step':9,'gauge':7,'desity':1,'items':14,'positive':n1norm(),'negative':n1norm()},
        'lightning':{'step':56,'gauge':7,'desity':7,'items':162,'positive':l1setup(),'negative':l1setup()},
        'basicsss':{}
    }

# print(pizzamenu.recipe['allunder']['step'])
