import os
import twitter
from rich import print

api = twitter.Api(consumer_key=os.environ.get('CONSUMER_KEY'),
                  consumer_secret=os.environ.get('CONSUMER_SECRET'),
                  access_token_key=os.environ.get('ACCESS_TOKEN_KEY'),
                  access_token_secret=os.environ.get('ACCESS_TOKEN_SECRET'))

keyword = 'うっせぇわ'
query = 'q={}%20lang%3Aja%20-filter%3Areplies&src=typed_query&count=100'.format(keyword)
results = api.GetSearch(raw_query=query)
sorted_results = sorted(results, reverse=True, key=lambda x:x.user.followers_count)

print([(x.user.name, x.user.followers_count) for x in sorted_results])
