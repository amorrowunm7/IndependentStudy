import twitter
import pickle
import time

api = twitter.Api(consumer_key='NsNYFG9LtZV2XMyigPaCKVyVz',
                consumer_secret='4J1vlowybipqXnSrKgLBvmzPmwqx71uHN32noljTgDLS2xQNfI',
                access_token_key='16562593-NCuQWVnpzcnB55w7VLdoCkdobdUQBRDJKjIPXAksP',
                access_token_secret='nX9OksrYQxj0jBXYJTkUjlX5mZh4rZljfVRXtSM3Tjc8c',
                requests_timeout=60)



following = pickle.load(open("following1", "rb"))
numFollowers = len(following)

following_depth2 = { }
counter = 0
for follow in following[numFollowers/2:]:
    success = False
    while not success:
        try:
            print("Processing follower ID %d (%f done)" % (follow, (100.0 * counter) / float(len(following)) ))
            following_depth2[follow] = api.GetFriendIDs(user_id=follow)
            success = True
            counter = counter + 1
 
            print("Saving intermediate results")
            pickle.dump(following_depth2, open("following_depth2.part2", "wb"))
        except twitter.TwitterError as e:
            print("Delaying by a minute due to rate limits")
            time.sleep(60)

#pickle.dumps(following_depth2, open("following2", "wb"))