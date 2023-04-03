
import tkinter as t
from tkinter import END
import pandas as pd
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import filedialog as fd
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


firebaseConfig = {
  "apiKey": "AIzaSyD0Nct_JKDGGk-Q2WTxjchNZkiYnJ514NQ",
  "authDomain": "sis-database-f90db.firebaseapp.com",
  "databaseURL": "https://sis-database-f90db-default-rtdb.firebaseio.com",
  "projectId": "sis-database-f90db",
  "storageBucket": "sis-database-f90db.appspot.com",
  "messagingSenderId": "221559006372",
  "appId": "1:221559006372:web:81f674f34f743b72843231",
}

cred = credentials.Certificate('firebase-sdk.json')
firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)
authent = firebase.auth()

db = firebase.database()

data_ = db.child("student_database").child("2022-2026").child("AIML A").get()
data_dict = data_.val()
list_keys = data_dict.keys()
for x in list_keys:
    print(data_dict[x])