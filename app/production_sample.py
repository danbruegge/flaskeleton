# -*- coding: utf-8 -*-
from app.settings import *


SECRET_KEY = ''
DEBUG = False
ASSETS_DEBUG = DEBUG

DEBUG_TB_PROFILER_ENABLED = DEBUG

ERROR_MAIL = {
    'smtp': '<SMTP SERVER',
    'to': ['<TO>'],
    'from': '<FROM>',
    'subject': '<SUBJECT>'
}
