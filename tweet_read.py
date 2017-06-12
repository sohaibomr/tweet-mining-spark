import tweepy
#hello


from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json




      
      
      
class TweetListener(StreamListener):
    
    def __init__(self, csocket):
        self.client_socket=csocket
        
    def on_data(self, data):
      try:
          msg = json.loads( data )
          print( msg['text'].encode('utf-8') )
          self.client_socket.send( msg['text'].encode('utf-8') )
          return True
      except BaseException as e:
          print("Error on_data: %s" % str(e))
      return True
            
    
    def on_error(self, status):
        print (status)
        return True
        
        


def sendData(csocket):
    """
    Method:sendData
    description:
    """
    auth=OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twitter_stream=Stream(auth, TweetListener(csocket))
    twitter_stream.filter(track=['Barcelona'])
    
        
        
if __name__=="__main__":
    s=socket.socket()
    host="127.0.0.1"
    port=8888
    
    s.bind((host, port))
    print("Listening on port: %s" % str(port))

    s.listen(5)                 # Now wait for client connection.
    c, addr = s.accept()        # Establish connection with client.
    print "I am C", c

    print( "Received request from: " + str( addr ) )

    sendData( c )
