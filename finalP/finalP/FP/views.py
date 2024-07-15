from rest_framework import serializers as serializers
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Places, States

import json

# Create your views here.
@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

def index(request):
    if request.method == 'POST':
        destination = request.POST
        
        return redirect(qa)
    



    else:
        places = Places.objects.all()
        return render(request, "FP/index.html", {
            
        })
    

# autocomplete search box API
def places(request):
    places = list(States.objects.values("states"))
    # places = serializers.serialize("json", places)
    return JsonResponse({"places":places}, safe=False)


def qa(request):
    if request.method == 'POST':
         tag = request.POST.getlist('chk[]',"")
         
         return render(request, "FP/qa.html", {
            "tags":tag,
        })
    else:
        tags = [c[0] for c in Places.OPTIONS]
        return render(request, "FP/qa.html", {
            "tags":tags,
        })
# calculate distance from place to place
# data = request.body
#         data = data.decode('utf-8')

#         data = json.loads(data)
#         start = data.get("from", "")
#         end = data.get("to", "")
       
#         start_coor= Places.objects.get(name = start).location
#         end_coor = Places.objects.get(name = end).location
        
#         return JsonResponse({"start":start_coor, "end":end_coor}, safe=False)
#         return render(request, "FP/index.html", {
#             "start": start,
#         })

def ui (request):
    return render(request, "FP/what-to-wear.html")