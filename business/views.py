from django.shortcuts import render
import os
import sys
import urllib.request
import json

# Create your views here.


def info_search(request):

    if request.method == 'GET':
            
        client_id = "5fvIjJBkrax3JfgIS8D4"
        client_secret = "oLexIVNJqx"

        query = request.GET.get('query')

        encText = urllib.parse.quote("{}".format(query))
        url = "https://openapi.naver.com/v1/search/news?query=" + encText + '&display=100' # json 결과
        movie_api_request = urllib.request.Request(url)
        movie_api_request.add_header("X-Naver-Client-Id", client_id)
        movie_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(movie_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items')
            context = {
                'items': items
            }
            return render(request, 'business/search/info_search.html', context=context)

