import string
import random
from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 6)

def gen_shortcode(size=SHORTCODE_MIN,
                  chars=string.ascii_letters+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def make_shortcode(insta, size=SHORTCODE_MIN):
    newcode = gen_shortcode()
    klass = insta.__class__
    k_exist = klass.objects.filter(shortcode=newcode).exists()
    if k_exist:
        return make_shortcode(size)
    return newcode
