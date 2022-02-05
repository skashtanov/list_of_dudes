import instaloader
import sys
from datetime import datetime

if __name__ == '__main__':
    properties = {
        'email': sys.argv[1],
        'password': sys.argv[2],
        'username': sys.argv[3]
    }

    instagram = instaloader.Instaloader()
    instagram.login(properties['email'], properties['password'])

    profile = instaloader.Profile.from_username(instagram.context, properties['username'])

    followees = set(map(lambda followee: followee.username, profile.get_followees()))
    followers = set(map(lambda follower: follower.username, profile.get_followers()))

    unsubscribed_dudes = followees - followers
    
    with open(f'dudes_{datetime.today().date()}.txt', 'a') as output:
        for dude in unsubscribed_dudes:
            output.write(f'@{dude}\n')
