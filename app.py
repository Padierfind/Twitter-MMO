print('In File: app.py')

from src.twitter_authentication import get_auth
from src.user_handling import User, get_all_users_in_db

import src.tweet_handler as tweet_handler
import src.item_handling as item_handling
import configs.tweet_strings as tweet_strings

import tweepy

auth = get_auth()
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print('In Method: on_status()')

        # https://www.geeksforgeeks.org/python-status-object-in-tweepy/

        user = User(status.user.screen_name)

        # 1: Check registration status
        is_registered = user.check_if_user_is_registered()

        if not is_registered:
            if 'register' in status.text:
                successfully_registered = user.register_user()

                if successfully_registered:
                    to_tweet = tweet_strings.successfully_registered
                else:
                    to_tweet = tweet_strings.random_error
            else:
                to_tweet = tweet_strings.not_registered

            return tweet_handler.queue_tweet(api=api, user_name=user.user_name, text=to_tweet, reply_id=status.id)
        elif user.character_class is None:
            # If registered but no class chosen, send class selection tweet
            if 'memer' in status.text:
                if user.set_character_class('memer') is True:
                    to_tweet = tweet_strings.choose_memer
                else:
                    to_tweet = tweet_strings.random_error
            elif 'alt' in status.text:
                if user.set_character_class('alt') is True:
                    to_tweet = tweet_strings.choose_alt
                else:
                    to_tweet = tweet_strings.random_error
            elif 'fake' in status.text:
                if user.set_character_class('fake') is True:
                    to_tweet = tweet_strings.choose_fake
                else:
                    to_tweet = tweet_strings.random_error
            elif 'debater' in status.text:
                if user.set_character_class('debater') is True:
                    to_tweet = tweet_strings.choose_debater
                else:
                    to_tweet = tweet_strings.random_error
            else:
                to_tweet = tweet_strings.choose_class

            return tweet_handler.queue_tweet(api=api, user_name=user.user_name, text=to_tweet, reply_id=status.id)

        # 2: Check for state independent commands

        if 'character' in status.text or 'info' in status.text or 'status' in status.text or 'account' in status.text:
            found_other_user_in_text = False

            for other_user in get_all_users_in_db():
                if other_user.user_name in status.text and other_user.user_name != user.user_name:
                    to_tweet = tweet_strings.get_char_info(other_user)
                    found_other_user_in_text = True
                    break

            if not found_other_user_in_text:
                to_tweet = tweet_strings.get_char_info(user)

            return tweet_handler.queue_tweet(api=api, user_name=user.user_name, text=to_tweet, reply_id=status.id)
        elif 'help' in status.text:
            to_tweet = tweet_strings.help
            return tweet_handler.queue_tweet(api=api, user_name=user.user_name, text=to_tweet, reply_id=status.id)
        elif 'stats' in status.text:
            return
        elif 'inventory' in status.text:
            found_item_in_text = False

            for item in item_handling.get_all_items_in_db():
                if item.name in status.text:
                    to_tweet = tweet_strings.get_item_info(item)
                    found_item_in_text = True
                    break

            if not found_item_in_text:
                to_tweet = tweet_strings.get_inventory(user)

            return tweet_handler.queue_tweet(api=api, user_name=user.user_name, text=to_tweet, reply_id=status.id)
        elif 'delete' in status.text:
            to_tweet = tweet_strings.delete_user
            return tweet_handler.queue_tweet(api=api, user_name=user.user_name, text=to_tweet, reply_id=status.id)

        # 3: Check for status

        if user.status == 'idle':
            return
        elif user.status == 'quest':
            return
        elif user.status == 'arena':
            return


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

myStream.filter(track=['@Tweet_Arena'])
