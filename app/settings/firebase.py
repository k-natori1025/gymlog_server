import firebase_admin
from app.settings.env import Env
import logging

logger = logging.getLogger(__name__)

# def initialize_firebase():
#   cred = firebase_admin.credentials.Certificate(Env.FIREBASE_DICT)
#   firebase_admin.initialize_app(cred)

def initialize_firebase():
    try:
        logger.info("Initializing Firebase Admin SDK...")
        if not firebase_admin._apps:
            cred = firebase_admin.credentials.Certificate(Env.FIREBASE_DICT)
            firebase_admin.initialize_app(cred)
            logger.info("Firebase Admin SDK initialized successfully.")
        else:
            logger.info("Firebase Admin SDK already initialized.")
    except Exception as e:
        logger.error(f"Error initializing Firebase Admin SDK: {str(e)}")
        raise
