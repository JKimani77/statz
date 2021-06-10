import urllib.request, json
from .models import *

def process_apiresults(item_list):
    
    source_results = []

    for i in item_list:
        title = i.get('title')
        image = i.get('thumbnail')
        url = i.get('url')
        competition_name = i.get('competition.id')

        if title:
            a = Apidata(title,image,url,competition_name)
            source_results.append(a)

    return source_results

def get_apistuff():
    '''
    function to get json response to request
    '''
    
    
    #with urllib.request.urlopen(url)as url:
        #apidata = url.read()
        #apiresponse = json.loads(apidata)

        #apiresults = []

        #if apiresponse['items']:
            #apilist = apiresponse['items']
            #apiresults = process_apiresults(apilist)

    #return apiresults
pass
