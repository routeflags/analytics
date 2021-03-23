import os
from pyyoutube import Api
from rich import print

api = Api(api_key=os.environ.get('KEY'))
response = api.search_by_keywords(q="surfing",
		search_type=["channel"],
		count=10,
		order='rating')

for i, x in enumerate(response.items):
	print(i+1, x.snippet.channelTitle)
