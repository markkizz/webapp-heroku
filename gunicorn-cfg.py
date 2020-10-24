# -*- encoding: utf-8 -*-
import os
from string import Template
# bind = '0.0.0.0:5005'
bind = Template('0.0.0.0:$port').substitute(port=os.getenv('PORT') if os.getenv('PORT') else '5005')
workers = 3
accesslog = '-'
loglevel = 'debug'
capture_output = True