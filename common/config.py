import redis
import os

MAX_REQUEST_COUNT = os.getenv('MAX_REQUEST_COUNT')

TIMEOUT = os.getenv('TIMEOUT')

ACCOUNT_SID = os.getenv('ACCOUNT_SID')

AUTH_TOKEN = os.getenv('AUTH_TOKEN')

TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

redis_client = redis.Redis(host='localhost', port=6379)