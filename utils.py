import string
import random
from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)

def code_generator(size=SHORTCODE_MIN, 
                   chars=string.letters + string.digits
                   ):
    return ''.join(random.choice(chars) for _ in range(size))

def make_shortcode(Instance, size=SHORTCODE_MIN):
    newcode = code_generator()
    Klass = Instance.__class__
    c_exist = Klass.objects.filter(shortcode=newcode).exists()
    if c_exist:
        return make_shortcode(size)
    return newcode 
