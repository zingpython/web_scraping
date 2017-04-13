import twitter
import json


CONSUMER_KEY = 'Q88u0KvQK4f7fGfqO43SxVbcE'
CONSUMER_SECRET = 'ahQk6VKzjuF5eucS6a6DJT3LubBqnBTj5JxT2BvBTaIDMKkZhO'
OAUTH_TOKEN = '797271725629173762-0Y2XBwZGwjfcTpXLGLxZCKOI3mDmEtq'
OAUTH_TOKEN_SECRET = 'tdVlX8T6NZzoOiEpG6f7oAUrMRwOK765sITdzWgbhjRZo'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
						   CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)



WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

world_trends_set = set([trend['name']for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name']for trend in us_trends[0]['trends']])

# print("US Trends",us_trends_set)
# print("World trends",world_trends_set)

common_trends = world_trends_set.intersection(us_trends_set)
# third
# print("Common trends",common_trends)

q = '#SignsThatYourNoLongerInLove'
count = 10
# See https://dev.twitter.com/docs/api/1.1/get/search/tweets
search_results = twitter_api.search.tweets(q=q, count=count)
# fourth
# print(search_results)
statuses = search_results['statuses']


status_texts = [ status['text'] for status in statuses ]
screen_names = [ user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions'] ]
hashtags = [ hashtag['text'] for status in statuses for hashtag in status['entities']['hashtags'] ]
print(json.dumps(status_texts[0:5], indent=1))

words = [ w for t in status_texts for w in t.split() ]
print(words)















