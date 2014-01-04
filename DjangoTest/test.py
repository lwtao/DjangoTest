__author__ = 'kevin'

from django.conf import settings
settings.configure()
from django.db import connection
cursor = connection.cursor()
# cursor.
#import MySQLdb as db

