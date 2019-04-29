from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
import json, sys, os
import binascii
import json
import datetime
# Create your views here.

from decimal import Decimal
from pprint import pprint
import environ

env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env('.env')


def post_home(request):

    title = 'vk_parser'
    keywords = 'vk_parser'

    return render(request, 'home.html', {
        'title': title,
        'keywords': keywords,
    })


