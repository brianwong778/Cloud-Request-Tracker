from google.cloud import pubsub_v1
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

try:
    PROJECT_ID = os.getenv('PROJECT_ID')
    SUBSCRIPTION_NAME = os.getenv('SUBSCRIPTION_NAME')
    TOPIC_NAME = os.getenv('TOPIC_NAME')

    if not all([PROJECT_ID, SUBSCRIPTION_NAME, TOPIC_NAME]):
        raise ValueError("Environment variables for PROJECT_ID, SUBSCRIPTION_NAME, or TOPIC_NAME are not set")

    def callback(message):
        print(f"Received error message: {message.data.decode('utf-8')}")
        message.ack()

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_NAME)

    print(f"Listening for messages on {subscription_path}...")
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)

    try:
        streaming_pull_future.result()
    except Exception as e:
        print(f"An exception occurred: {e}")
        streaming_pull_future.cancel()

except Exception as e:
    print(f"Error loading environment variables: {e}")
