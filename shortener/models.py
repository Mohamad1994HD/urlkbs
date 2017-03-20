from django.db import models
from django.conf import settings
from .utils import make_shortcode
from .validators import validate_url
from django_hosts.resolvers import reverse

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 16)

# Create your models here.
class KbsURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
   
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = make_shortcode(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(KbsURL, self).save(*args, **kwargs)

    def refresh_shortcode(self):
        self.shortcode = make_shortcode(self)
 
    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
    
    def get_shortcode(self):
        return str(self.shortcode)

    def get_short_url(self):
        url_path = reverse('short', kwargs={'code':self.shortcode},
                           host='www', scheme='http')
        return url_path
