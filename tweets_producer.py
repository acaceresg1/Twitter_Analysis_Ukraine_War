#!/usr/bin/python3
from confluent_kafka import Producer
import argparse
import socket
import time
import os


def yield_entries(tweets_data_file):
  # seek the end of the file
  tweets_data_file.seek(0, os.SEEK_END)
    
  # start infinite loop
  while True:
    # read last line of file
    tweets_entry = tweets_data_file.readline().rstrip()        
    if not tweets_entry:
      time.sleep(0.1) # sleep if no new entries are available
      continue

    yield tweets_entry
    
def send_message(producer, message, topic):
  # Checking that message and topic were specified
  #
  if message == None:
    print("ERROR: A message has to be provided")
    return
  if topic == None:
    print("ERROR: A topic has to be provided")
    return

  producer.produce(topic, value=message)
  producer.flush()

parser = argparse.ArgumentParser()
parser.add_argument("action",choices=['send','list_topics'])
parser.add_argument("-m", "--message",
                    help="message to send if action is 'send'")
parser.add_argument("-t", "--topic",
                    help="topic where the tweet data has to be sent if action is 'send'")
args = parser.parse_args()

# Producer setup
#
conf = {'bootstrap.servers': "localhost:9092",
        'client.id': socket.gethostname()}
producer = Producer(conf)

# Connection to the sensor data file
#
tweets_data_file = open("tweets_war.txt","r")
#tweets_entries = yield_entries(tweets_data_file)    # iterate over the generator
tweets_entries = tweets_data_file
print("Sending tweet data to topic '%s'" % args.topic)
for tweets_entry in tweets_entries:
  send_message(producer, tweets_entry, args.topic)
