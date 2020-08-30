print('In File: src/tweet_handler.py')

import tweepy

from src.db_handling import DbHandler


def tweet(api: tweepy.API, text: str):
    print('In Method: tweet()')

    api.update_status(status=text)


def tweet(api: tweepy.API, text: str, reply_id: str):
    print('In Method: tweet()')

    api.update_status(status=text, in_reply_to_status_id=reply_id)


def queue_tweet(api: tweepy.API, user_name: str, text: str):
    print('In Method: queue_tweet()')

    handler = DbHandler()
    db = 'twitter_mmo'  # change for production
    collection = 'tweet_queue'

    tweet_dict = {
        'text': "@" + user_name + " " + text
    }

    result_of_db_operation = handler.write_to_database(db_name=db, collection_name=collection,
                                                       json_to_write=tweet_dict)

    if result_of_db_operation['success'] is True:
        return True
    else:
        return False


def queue_tweet(api: tweepy.API, user_name: str, text: str, reply_id: str):
    print('In Method: queue_tweet()')

    handler = DbHandler()
    db = 'twitter_mmo'  # change for production
    collection = 'tweet_queue'

    tweet_dict = {
        'text': "@" + user_name + " " + text,
        'replay_id': reply_id
    }

    result_of_db_operation = handler.write_to_database(db_name=db, collection_name=collection,
                                                       json_to_write=tweet_dict)

    if result_of_db_operation['success'] is True:
        return True
    else:
        return False
