from django.http import HttpResponseRedirect
from django.conf import settings

DEFAULT_REDIRECT = getattr(settings, 'DEFAULT_REDIRECT_URL', 
                                     'http://www.kbs.com:8000'
                           )

def wildcard_redirect(request, path=None):
   # new_url = DEFAULT_REDIRECT
   # print ("path:{}".format(path))
   #j if path is not None:
   #     new_url = DEFAULT_REDIRECT + '/' + path
    return HttpResponseRedirect(DEFAULT_REDIRECT)
