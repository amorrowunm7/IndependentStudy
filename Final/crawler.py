import graphlab as gl
import pickle
import twitter

import graphlab as gl
import pickle
import twitter

# Lets create out api object w/ OAuth parameters
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

apis = []
for token in API_TOKENS:
    apis.append( twitter.Api(consumer_key=token['consumer_key'],
                    consumer_secret=token['consumer_secret'],
                    access_token_key=token['access_token_key'],
                    access_token_secret=token['access_token_secret'],
                    requests_timeout=60))



account_screen_name = 'fairmediawatch'
account_id = '54679731'

from collections import defaultdict
nodes = set()
edges = defaultdict(list)



try:
    print "Loading followers for %s" % account_screen_name
    f = open("following1", "rb")
    following = pickle.load(f)
except Exception as e:
    print "Failed. Generating followers for %s" % account_screen_name
    following = api.GetFriendIDs(screen_name=account_screen_name)
    pickle.dump(following, open("following1", "wb"))

try:
    print "Loading nodes and edges for depth = 1, for %s" % account_screen_name
    n = open("nodes.follow1.set", "rb")
    e = open("edges.follow1.dict", "rb")
    nodes = pickle.load(n)
    edges = pickle.load(e)
except Exception as e:
    print "Failed. Generating nodes and edges for depth = 1, for %s" % account_screen_name
    for follower in following:
        nodes.add(follower)
        edges[account_id].append(follower)
    pickle.dump(nodes, open("nodes.follow1.set", "wb"))
    pickle.dump(edges, open("edges.follow1.dict", "wb"))

### Depth2

# for follower, following_depth2 in following_depth_part1.iteritems():
#     twitter_graph.add_vertex(name=str(follower))
#     try:
#         twitter_graph.add_vertices( [str(f) for f in following_depth2] )
#         twitter_graph.add_edges( [(str(f), str(follower)) for f in following_depth2 ] )
#     except Exception as e:
#         print f
#         raise e

import time

api_idx = 0
api = apis[api_idx]

blacklist= ["74323323"]
#turnover = False

for follower in following:
    success = False
    
    if follower in blacklist:
        print("Skipping due to blacklist")
        continue

    while not success:
        try:
            print("Getting followers for follower %s" % follower)
            followers_depth2_list = api.GetFriendIDs(follower)
            success = True
            time.sleep(1)
        except Exception as e:
            print("API Exception %s; api-idx = %d" % (str(e), api_idx))
            
            if api_idx % len(API_TOKENS) == 0 and api_idx >= len(API_TOKENS): #and not turnover:
                print("Save edges to pickle file for follower = %s" % follower)
                pickle.dump(edges, open("edges.follow2.dict", "wb"))
                
                print("Sleeping ...")
                time.sleep(60)
            else:
                api_idx += 1
                api = apis[api_idx % len(API_TOKENS)]
            
    
    print("Adding followers to the graph")
    for follower_depth2 in followers_depth2_list:
        if follower_depth2 in nodes:
            edges[follower] = follower_depth2



print("FINAL: Adding followers to the graph")
for follower_depth2 in followers_depth2_list:
    if follower_depth2 in nodes:
        edges[follower] = follower_depth2
print("Save edges to pickle file for follower = %s" % follower)
pickle.dump(edges, open("edges.follow2.dict", "wb"))