from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
#
from shortener.models import KbsURL
from .serializers import UrlSerializer

class KBSUrlView(APIView):
    renderer_classes = (JSONRenderer, )
    
    def get(self, request):
        return Response({'API version': '1.0'})
    
    def post(self, request):
        serializer = UrlSerializer(data=request.POST)
        context = {"accepted" : 1}
        print (request.POST)

        if serializer.is_valid():
            new_url = serializer.validated_data['url']
            obj, created = KbsURL.objects.get_or_create(url=new_url)
            response_serializer = UrlSerializer(obj)
            context['data'] = response_serializer.data
            return Response(context)
        context = {
                    'accepted': 0,
                    'msg': 'Invalid URL'
                   }        
        return Response(context) 
