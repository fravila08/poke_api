from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1
from rest_framework.views import APIView
from rest_framework.response import Response
import pprint
from dotenv import dotenv_values

env = dotenv_values(".env")
pp = pprint.PrettyPrinter(indent=2, depth=2)

class Noun_project(APIView):

    def get(self, request, item):
        auth = OAuth1(env.get("API_KEY"), env.get("SECRET_KEY") )
        endpoint = f"https://api.thenounproject.com/icon/{item}/"
        response = requests.get(endpoint, auth=auth)
        print(f"\n\n\n{env}\n\n\n")
        JSONresponse = response.json()
        pp.pprint(JSONresponse)
        icon_url = JSONresponse.get('icon').get("preview_url")
        # print(icon_url)
        return Response(icon_url)
