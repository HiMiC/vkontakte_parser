from django.core.management.base import BaseCommand, CommandError
import urllib.request
import json
from pprint import pprint
import os, io
import csv
import json, sys, os
import json
import datetime
import time
import environ

env = environ.Env(DEBUG=(bool, False), )
environ.Env.read_env('.env')


# https://github.com/rabbit10086/allproject/blob/c21a0fd4a0b28f3d548c8ffed7b47fb3783eea73/IDCG_Auto/idcm/ethtes.py




class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    #  def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):

        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        # pprint(w3.eth.blockNumber)
        # exit()
        geth_host = 'http://' + env('GETH_HOST', default='gethnode') + ':' + env('GETH_PORT', default='8545')

        exit(WARNING + "ОСТАНОВЛЕНО Синхронизируется блокчейн до текущего состояния: " + ENDC)






        self.stdout.write(self.style.SUCCESS('Successfully closed poll'))
