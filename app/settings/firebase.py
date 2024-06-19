import firebase_admin
from app.settings.env import Env

def initialize_firebase():
  cred = firebase_admin.credentials.Certificate(Env.FIREBASE_DICT)
  firebase_admin.initialize_app(cred)
