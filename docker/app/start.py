#!/usr/bin/env python
import pymongo
import sys
import time
import os


client = pymongo.MongoClient()
dbnames = client.database_names()
if 'conductor_dev' in dbnames:
    pass
else:
    os.system("./micro.py index")
    from app.models import User
    user = User(username="conductor", password_raw="conductor", supervisor=True)
    user.save()

os.system("./micro.py run")

# while True:
#     time.sleep(40)
