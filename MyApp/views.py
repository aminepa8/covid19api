from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.http import HttpResponse
import json,requests
from subprocess import Popen, PIPE, STDOUT
from requests_html import HTML,HTMLSession
from django.urls import path

# Create your views here.



def ScrapyStages(Country ='morocco'):

    session = HTMLSession()
    dataStatistics = []
    linkScrap = 'https://www.worldometers.info/coronavirus/country/'+ Country 
    r = session.get(linkScrap)
    CountryStatistics = r.html.find('.col-md-8 .content-inner .maincounter-number span')
    LastUpdateTime = r.html.find('.col-md-8 .content-inner > div:nth-child(4)')
    LastUpdate = LastUpdateTime[0].text
    print(LastUpdate)
    print('Country : '+Country)
    
    
    CoronavirusCases  =  CountryStatistics[0].text
    print('Coronavirus Cases: '+CoronavirusCases)
    Deaths = CountryStatistics[1].text
    print('Deaths: '+Deaths)
   
    Recovered = CountryStatistics[2].text
    print('Recovered: '+Recovered)
    CountryData ={
            'LastUpdate' : LastUpdate,
            'Country' :Country,
            'CoronavirusCases' : CoronavirusCases,
            'Deaths' : Deaths,
            'Recovered' : Recovered,
            
            }
    dataStatistics.append(CountryData)
    
    json_file = json.dumps(dataStatistics)#,indent=4
    
    #print('********************JSON FILE*******************')
    return json_file
    #End Scrappy func
    #@csrf_exempt


@api_view(["GET"])
def ScrappyService(request):
        pagenbr = request.query_params.get('country')
        if request.method == 'GET':
            data = ScrapyStages(pagenbr)
            response = Response({"data":data} , 
            content_type='application/json', status=200)
            ##response = Response(data, status=200, template_name=None, headers=None, content_type='application/json')
            return response