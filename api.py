

print "QUESTION 1"
#QUESTION 1
'''
An access_token is a unique string of letters and numbers that you pass with every API call

Each access_token is associated with:

Your API application.
The user you are acting on behalf of (for merchants, this is yourself).
The permissions your app has for that user.
'''

print "QUESTION 2"
#QUESTION 2
'''
facebook ip address=  157.240.16.35
google ip address= 172.217.160.238
'''
print "QUESTION 3"
#QUESTION 3
import tweepy
consumer_key='customer_key'
consumer_secret='customer_secret'
access_token='access_token'
access_token_secret='access_secret_token'

oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_token_secret)
api=tweepy.API(oauth)
public_tweets=api.search("api")
print public_tweets
status="testing api"
api.update_status(status=status)

print "QUESTION 4"
#QUESTION 4
'''
Library vs API
A library is a chunk of code designed for reuse that is typically installed locally.
A library is most often wrapped in an API that defines the functionality the library provides and how to use it.
Technically speaking, the term API refers to an interface that doesn't need to have an implementation. ' \
However, when people speak of an API they are usually referring to a reusable library or service.
Where a library is used as a package of code, a service is a running system that provides functionality to other systems and applications.

So for example OpenGL is a “library” and the API for it is defined in the OpenGL specification.
The API comprises a bunch of named constants and a list of function calls specifications.

For example, a ‘web api’ makes use of numerous libraries for oAuth, CORS, REST, etc,
and within those libraries they may also make use of API’s so that they can get standardized input/output when calling them
'''

print "QUESTION 5"
#QUESTION 5
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='client_id', client_secret='client secret')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('username')

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
