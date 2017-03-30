from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.views import View
from .models import KbsURL
from .forms import SubmitURLForm
# Create your views here.
class ApiView(View):
    def get(self, request, *args, **kwargs):
        #return HttpResponse("Api Documentation")
        return render(request, 'shortener/api.html')

class HomeView(View):
    context = {}
    def get(self, request, *args, **kwargs):    
        form = SubmitURLForm()
        self.context['form'] = form 
        return render(request,
                      "shortener/home.html",
                      self.context)

    def post(self, request, *args, **kwargs):
        form = SubmitURLForm(request.POST)
        self.context['form'] = form
   
        if form.is_valid():
            url = form.cleaned_data.get('url')
            obj, created = KbsURL.objects.get_or_create(url=url)
            self.context = {
                            'created':created,
                            'obj': obj
                           }
            return render(request,
                          'shortener/link.html',    
                          self.context
                          ) 
    
        return render(request,
                      "shortener/home.html",
                      self.context)

class RedirectURLView(View):
    def get(self, request, code=None, *args, **kwargs):
        obj = get_object_or_404(KbsURL, shortcode=code)  
        return HttpResponseRedirect(obj.url)



def err404(request):
    return render(request, 'shortener/404.html', {})   

def err500(request):
    return render(request, 'shortener/500.html', {})
