import os

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

def notify():
    print("Sending alert...")
