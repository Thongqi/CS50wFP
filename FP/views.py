from rest_framework import serializers as serializers
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Places, States

import json
import psycopg2

# postgres
conn = psycopg2.connect(database = "finalp", 
                        user = "finalp_user", 
                        host= 'dpg-crb7k33tq21c73cg3lng-a',
                        password = "vrVlqog32vqbwsJznxvPJfVWol6ALFdZ",
                        port = 5432)
cursor = conn.cursor()

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
        tag = request.POST.getlist('chk[]')
        days = request.POST.get('select_days')
        transport = request.POST.get('transport')

        # places = list(fp_places.objects.values("name"))
        places = cursor.execute("SELECT * FROM fp_places")
  
        # If flight or ferry
        if transport == 'Flight':
            # If Flight
            if 'Outdoor' in tag or 'Nature' in tag:
                day_1_2 = 'Telaga 7 Waterfall'
            else:
                day_1_2 = 'Crocodile Adventure Land'
            
        else:
            # If Ferry
            day_1_2 = None
        day_1_2_info = Places.objects.get(name=day_1_2) if day_1_2 else None
        
        # Day 2
        if 'History' in tag or 'Culture' in tag:
            day_2_2 = 'Kota Mahsuri'

        else:
            day_2_2 = None
        day_2_2_info =Places.objects.get(name=day_2_2) if day_2_2 else None
        
        # 3D2N
        if days == '3D2N':
            # 3D:flight
            if transport == 'Flight':
                day_3_1 = 'Sandy Skulls Beach'
                if day_1_2 != 'Crocodile Adventure Land':
                    day_3_2 =  'Temurun Waterfall'
                elif 'Animal' in tag:
                    day_3_2 =  'Crocodile Adventure Land'
                else:
                    day_3_2 = None
            # 3D:ferry
            else:
                if 'Animal' in tag:
                    day_3_1 = 'Langkawi Wildlife Park'
                else:
                    day_3_1 = 'Kilim Geoforest Park'
                day_3_2 = 'Teow Soon Huat Duty Free Sdn. Bhd.'
                
            day_3_1_info = Places.objects.get(name=day_3_1)
            day_3_2_info = Places.objects.get(name=day_3_2) if day_3_2 else None
            
            day_3_3 = None
            day_4_1 = None
            day_4_2 = None
            
        # 4D3N
        else:
            # 4D:Flight
            if transport == 'Flight': 
                day_4_2 = None
                if 'Animal' in tag:
                    day_3_1 = 'Langkawi Wildlife Park'
                elif 'Outdoor' in tag or 'Nature' in tag:
                    day_3_1 = 'Temurun Waterfall'
                else:
                    day_3_1 = 'Kilim Geoforest Park'

                if 'Outdoor' in tag or 'Nature' in tag:
                    day_3_2 = 'Kilim Geoforest Park'
                elif 'Adventure' in tag or 'Sporty' in tag:
                    day_3_2 = 'SKYTREX Adventure'

                else:
                    if day_3_1 == 'Kilim Geoforest Park':
                        day_3_2 = 'Public Gardens Teluk Yu'
                    else:
                        day_3_2 = 'Kilim Geoforest Park'
                    day_4_2 = None
                day_3_3 = 'Teow Soon Huat Duty Free Sdn. Bhd.'
                day_4_1 = 'Sandy Skulls Beach'

            # 4D:Ferry
            else:
                day_3_3 = None
                if 'Outdoor' in tag or 'Nature' in tag:
                    day_3_1 = 'Telaga 7 Waterfall'
                elif 'Animal' in tag:
                    day_3_1 = 'Kilim Geoforest Park'
                else:
                    day_3_1 = 'Sandy Skulls Beach'
                    
                if 'Adventure' in tag or 'Sporty' in tag:
                    day_3_2 = 'SKYTREX Adventure'
                    
                elif day_3_1 == 'Sandy Skulls Beach':
                    day_3_2 = 'Crocodile Adventure Land'
                else:
                    day_3_2 = 'Sandy Skulls Beach'
                    
                # ferry:day4
                if 'Animal' in tag:
                    day_4_1 = 'Langkawi Wildlife Park'
                else:
                    day_4_1 = 'Kilim Geoforest Park'
                day_4_2 = 'Teow Soon Huat Duty Free Sdn. Bhd.'
                
                    
            day_3_1_info =Places.objects.get(name=day_3_1)

            day_3_2_info = Places.objects.get(name=day_3_2) if day_3_2 else None
            day_3_3_info =Places.objects.get(name=day_3_3) if day_3_3 else None
            day_4_1_info =Places.objects.get(name=day_4_1)
            day_4_2_info =Places.objects.get(name=day_4_2) if day_4_2 else None
        return render(request, "FP/itinerary.html", {
            "tag":tag,
            "days": days,
            "places": places,
            "day_1_2": day_1_2,
            "day_1_2_info":day_1_2_info,
            "day_2_2":day_2_2,
            "day_2_2_info":day_2_2_info,
            "day_3_1": day_3_1,
            "day_3_1_info":day_3_1_info,
            "day_3_2":day_3_2,
            "day_3_2_info":day_3_2_info,            
            "day_3_3":day_3_3,
            "day_3_3_info":day_3_3_info,
            "day_4_1": day_4_1,
            "day_4_1_info":day_4_1_info,
            "day_4_2": day_4_2,
            "day_4_2_info":day_4_2_info,
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

def itinerary (request):
    
    return render(request, "FP/itinerary.html")

