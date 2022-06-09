import pyrebase
import time
import random
from datetime import datetime


config = {

    "apiKey": "AIzaSyD4SnNOozEfyHWbDsgIzZLAYfBwGYnn6-A",
    "authDomain": "esp8266-4c64e.firebaseapp.com",
    "databaseURL": "https://esp8266-4c64e-default-rtdb.firebaseio.com",
    "projectId": "esp8266-4c64e",
    "storageBucket": "esp8266-4c64e.appspot.com",
    "messagingSenderId": "987808530245",
    "appId": "1:987808530245:web:2ab112676191df3fd3482c"
  
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()


temp = [26.5, 36.5, 16.5, 24, 23.6, 18.9, 39.5, 46.5, 27, 26.5]
percent = [96.5, 36.5, 16.5, 24, 83.6, 68.9, 39.5, 46.5, 97, 96.5]


while True:
    temperatura1 = random.choice(temp)
    temperatura2 = random.choice(temp)
    temperatura3 = random.choice(temp)
    temperatura4 = random.choice(temp)
    humidade = random.choice(percent)
    co2 = random.choice(percent)
   
    data_hora = datetime.today()
    data_hora = data_hora.strftime("%d/%m/%Y %H:%M:%S")
    
    db.child("test").update({"horac1": str(data_hora)})
    db.child("test").update({"temperaturac1": float(temperatura1)})
    
    db.child("test").update({"horac2": str(data_hora)})
    db.child("test").update({"temperaturac2": float(temperatura2)})
    
    db.child("test").update({"horac3": str(data_hora)})
    db.child("test").update({"temperaturac3": float(temperatura3)})
    
    db.child("test").update({"horas1": str(data_hora)})
    db.child("test").update({"temperaturas1": float(temperatura4)})
    db.child("test").update({"humidades1": str(humidade)})
    db.child("test").update({"co2s1": float(co2)})
    
    time.sleep(1)