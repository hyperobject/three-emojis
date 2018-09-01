from mastodon import Mastodon
import random
import os

mastodon = Mastodon( # Get these by going to the Development section of your Mastodon account settings
    client_id=os.environ['client_id'],
    client_secret=os.environ['client_secret'],
    access_token=os.environ['access_token'],
    api_base_url=os.environ['instance']
)

emojis = open('emojis.txt','r').read().split('\n') # Get all the emojis (newline-separated) from emojis.txt
message = ' '.join(random.choices(emojis, k=3)) # Pick 3 random emojis (wow!)

print('Posting toot:', message)
mastodon.toot(message) # Post 'em!