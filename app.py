from mastodon import Mastodon
import random
import os

mastodon = Mastodon(
    client_id=os.environ['client_id'],
    client_secret=os.environ['client_secret'],
    access_token=os.environ['access_token'],
    api_base_url=os.environ['instance']
)

emojis = open('emojis.txt','r').read().split('\n')
message = ' '.join(random.choices(emojis, k=3))

print('Posting toot:', message)
mastodon.toot(message)