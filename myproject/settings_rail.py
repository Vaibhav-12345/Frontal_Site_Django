from myproject.settings import *

from decouple import config 

SECRET_KEY=config("SECRET_KEY")
ALLOWED_HOSTS = ['https://web-production-fef8.up.railway.app/']