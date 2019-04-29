from django import template
import math

register = template.Library()

import time
import timeago, datetime
from datetime import datetime

@register.filter(name='print_timestamp')
def print_timestamp(timestamp):
    now = datetime.now()
    date = datetime.fromtimestamp(timestamp)
    return time.strftime("%Y-%m-%d %H:%M:%S %z", time.gmtime(timestamp)) +" (" +timeago.format(date, now, 'en')+")"

