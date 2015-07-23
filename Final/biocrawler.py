import pickle
import twitter
import logging
import time
from collections import defaultdict

logger = logging.getLogger('biocrawler')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('biocrawler.log')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)


from functools import wraps
import errno
import os
import signal

class TimeoutError(Exception):
    pass

def timeout(seconds=60, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

@timeout()
def getBio(api, follower):
    ''' Function that will get a user's list of followers from an api object. 
    NOTE: the decorator ensures that this only runs for 60s at most. '''
    # return api.GetFollowerIDs(follower)
    x = api.GetUser(follower)
    bio =  x.description
    if getattr(x, 'status', None) and getattr(x.status, 'text', None):
        bio = bio + "\n" + x.status.text
    return bio


API_TOKENS = [
    {"consumer_key": 'yp4wi4FASXbsRKa6JxYqzhUlH',
    "consumer_secret": 'Wkh1d5ygAOp4Bp65syFzHRN4xQsS8O4FvU3zHWosX8NXCqMpcl',
    "access_token_key": '16562593-F6lRFe7iyoQEahezhPmaI64oInHZD0LNpcIbbq7Wy',
    "access_token_secret": 'weregYL8n6DI7yZy9pkizIJ78rH2GY02Do9jvpTe7rCey',
    "requests_timeout": 60},

    {"consumer_key": 'NsNYFG9LtZV2XMyigPaCKVyVz',
    "consumer_secret": '4J1vlowybipqXnSrKgLBvmzPmwqx71uHN32noljTgDLS2xQNfI',
    "access_token_key": '16562593-NCuQWVnpzcnB55w7VLdoCkdobdUQBRDJKjIPXAksP',
    "access_token_secret": 'nX9OksrYQxj0jBXYJTkUjlX5mZh4rZljfVRXtSM3Tjc8c',
    "requests_timeout": 60},

    {"consumer_key": 'ZcAMGe2MUcnTO9ATCIo563SHN',
    "consumer_secret": 'dJAB7mBfoYyx27Yccbmzz98GtNigAA67Ish9Y1NjN2wNznciM1',
    "access_token_key": '16562593-AmaoKVLEYL3o8rVUS3b6u4PUbVPTI6BPsyaqCdwxY',
    "access_token_secret": '8pjYJCFWTErJlb2WSkLwsYNoptVazQQs95JAvIU8JApUA',
    "requests_timeout": 60},

    {"consumer_key": 'avZpjObqQN9vue2Y4gu9zIF9X',
    "consumer_secret": 'Ka6WCj3fyon5yGgf5YJIIl8nVcLcUh5YT99N58qy8qv4kfaMbc',
    "access_token_key": '16562593-VNuGD09Cr29ZlzNCWnV5MOujU7PsexSwfTgfKQNqC',
    "access_token_secret": '9P3hB3qDb9zPDFCUhWU16N4CMXPwHacl6HJbCc0EuGj7s',
    "requests_timeout": 60},

    {"consumer_key": 'sQ9H5NKteroNZSWvIrkSWvXR0',
    "consumer_secret": 'lC0ttZKdIZhhJAE1I5RxMxdjpSiADQCVUnHS7LbtfVmI2pz2F2',
    "access_token_key": '16562593-4LOk7QkXWD0boF01BmZ6NP2oPtHmDZ1OVJ883aANG',
    "access_token_secret": 'JJ85qMqzVowN1KdQ6w4YlhJB9YF9eWbw6SGbxQoU6gvne',
    "requests_timeout": 60},

    {"consumer_key": 'DHppZ2LG3iYj8vEx7ibRRLN35',
    "consumer_secret": 'wdTQeyp7ZNDN7ne40IriRw7Ah1J8cAi2OIlw4MVtgpq5MMKjYE',
    "access_token_key": '16562593-WN8zvEWAxVfJPrneMwUjDoVQw0geuLckOOJqFimsC',
    "access_token_secret": 'ZgVi2onPB3RPGtRmPBs6QXymIMgXwJHUOQycesp64S0Hp',
    "requests_timeout": 60},

    {"consumer_key": 'lIgtfdkC2WmN7XAcicrGygQBp',
    "consumer_secret": '2D9WIJN2MIPwFpMeIGcP6vWjQC8vvy7G5ZlHMSH1F1CsgWGKfz',
    "access_token_key": '16562593-7lhPpeZNNAGoQQJnqcnTtBiGq1O52XMZ4CMeVqXiY',
    "access_token_secret": 'WKRBQsr36MMB2EpCcZLr89ik0MSJfPoBORCKu9E1hw96I',
    "requests_timeout": 60},

    {"consumer_key": '1XFu2urZzoMoC5sadXAjA7IoQ',
    "consumer_secret": 'FrJOlHfNLp3M7ejJWiO5k74E9ai6L5EzQJ45HmlsUINbh8qUUi',
    "access_token_key": '16562593-Texko6g7VyCwhNUfxBDoJKJl4058hpvQkqAYWRKpi',
    "access_token_secret": 'ISZCTvN6bYJVaJ3Z2iidQObTzE2pxkINBLi0WWe9Ab2Zv',
    "requests_timeout": 60},

    {"consumer_key": 'r8Bvdm6I8QrRPuVzP4VtRYpqd',
    "consumer_secret": 'CzA8u8M8nDiDCCrSzCsXpR3SyTGCaLppDWbdTxSg78ZKgtKkhh',
    "access_token_key": '16562593-I3l0ZSmfZbMxIQ2NbiiM2eDMA4KNzFmFBeUkWxunR',
    "access_token_secret": '9HkILP4kSMF0hgvsB126jpoUzsRXETYMlSM0YSKb2yMJH',
    "requests_timeout": 60},

    {"consumer_key": 'NmMjfP1Zt3n2VDZ15X7SDGM6G',
    "consumer_secret": 'j9JBx7HUbMpcDnFteiIAAgHSoA8idlqQ20A1xbvnMrqMrOHQ1n',
    "access_token_key": '16562593-zUNyMUdO9JnSIstmTrqdyHHmX2lpv9NqkQxGC8faP',
    "access_token_secret": 'DEeHvLjTXlxNGmqDntXOK0cJCX08cnpg0btoRXWATW3X2',
    "requests_timeout": 60}
]

# Now create a list of twitter API objects
apis = []
for token in API_TOKENS:
    apis.append( twitter.Api(consumer_key=token['consumer_key'],
                    consumer_secret=token['consumer_secret'],
                    access_token_key=token['access_token_key'],
                    access_token_secret=token['access_token_secret'],
                    requests_timeout=60))

api_idx = 0
api = apis[api_idx]
api_updated = False

logger.info("Loading nodes depth = 1")
n = open("nodes.follow1.set", "rb")
nodes = pickle.load(n)

bios = { }




for node in nodes:
    success = False
    
    while not success:
        try:
            logger.info("Getting bio for follower %s" % node)
            bio = None
            bio = getBio(api, node)
            bios[node] = bio
            success = True
        except TimeoutError as e:
            # If api call takes too long, move on
            logger.info("Timeout after 60s for follower %d" % node)
            success = True      # technically not a success but setting flag so next loop moves on
            continue
        except Exception as e:
            # IF we get here, then we hit API limits
            logger.info("API Exception %s; api-idx = %d" % (str(e), api_idx))
            
            # Are we at the begining of api list? 
            # IF so, dump edges so far via pickle and sleep
            if api_updated and api_idx % len(API_TOKENS) == 0 and api_idx >= len(API_TOKENS):
                logger.info("Save bios to pickle file for follower = %s" % node)
                pickle.dump(bios, open("bios", "wb"))
                logger.info("Sleeping ...")
                time.sleep(60)
                api_updated = False
            # Otherwise, move on to the next api object and try again
            else:
                api_idx += 1
                api = apis[api_idx % len(API_TOKENS)]
                api_updated = True
            
    
    if bio:
        logger.info("Updating bios")
        pickle.dump(bios, open("bios", "wb"))


logger.info("Adding followers to the graph")
pickle.dump(bios, open("bios", "wb"))