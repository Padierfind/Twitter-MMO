print('In File: src/user_handling.py')

from datetime import datetime

from src.db_handling import DbHandler


class User:

    def __init__(self, name: str, level: int, character_class: str, xp: int, money: int, status: str,
                 status_id: int, stats: dict, items_equipped: dict, items_inventory: dict):
        print('In Method: __init__()')

        self.user_name = name
        self.level = level
        self.character_class = character_class
        self.xp = xp
        self.money = money
        self.status = status
        self.status_id = status_id
        self.stats = stats
        self.items_equipped = items_equipped
        self.items_inventory = items_inventory

    def __init__(self, name: str):
        print('In Method: __init__()')

        self.user_name = name
        self.level = 1
        self.character_class = None
        self.xp = None
        self.money = None
        self.status = 'idle'
        self.status_id = 0
        self.stats = {
            'intelligence': 1,
            'writing speed': 1,
            'luck': 1,
            'smiley usage': 1,
            'cynicism': 1,
            'vibes': 1
        }
        self.items_equipped = {
            'device': 'Smartphone',
            'clothes': None,
            'hat': None,
            'accessoire': None
        }
        self.items_inventory = {}

    def check_if_user_is_registered(self):
        print("In Method: check_if_user_is_registered()")

        handler = DbHandler()
        db = 'twitter_mmo'  # change for production
        collection = 'users'

        result_of_db_operation = handler.read_one_doc_by_param_from_database(db_name=db, collection_name=collection,
                                                                             doc_value=self.user_name,
                                                                             doc_param='user_id')

        if result_of_db_operation['success'] is True:
            self.level = result_of_db_operation['result']['level']
            self.character_class = result_of_db_operation['result']['character_class']
            self.xp = result_of_db_operation['result']['xp']
            self.money = result_of_db_operation['result']['money']
            self.status = result_of_db_operation['result']['status']
            self.status_id = result_of_db_operation['result']['status_id']
            self.stats = result_of_db_operation['result']['stats']
            self.items_equipped = result_of_db_operation['result']['items_equipped']
            self.items_inventory = result_of_db_operation['result']['items_inventory']

            return True
        else:
            return False

    def register_user(self):
        print("In Method: register_user()")

        handler = DbHandler()
        db = 'twitter_mmo'  # change for production
        collection = 'users'

        user_dict = {
            'user_id': self.user_name,
            'level': self.level,
            'character_class': self.character_class,
            'xp': self.xp,
            'money': self.money,
            'status': self.status,
            'status_id': self.status_id,
            'stats': self.stats,
            'items_equipped': self.items_equipped,
            'items_inventory': self.items_inventory,
            'registration_time': datetime.today()
        }

        result_of_db_operation = handler.write_to_database(db_name=db, collection_name=collection,
                                                           json_to_write=user_dict)

        if result_of_db_operation['success'] is True:
            return True
        else:
            return False

    def set_character_class(self, chosen_class: str):
        self.character_class = chosen_class

        handler = DbHandler()
        db = 'twitter_mmo'  # change for production
        collection = 'users'

        param_to_get_doc = 'user_id'
        param_to_change = 'character_class'
        new_value = chosen_class

        result_of_db_operation = handler.update_one_doc_by_param_from_database(db_name=db, collection_name=collection,
                                                                               doc_param_find=param_to_get_doc,
                                                                               doc_value_find=self.user_name,
                                                                               doc_param_new=param_to_change,
                                                                               doc_value_new=new_value)

        if result_of_db_operation['success'] is True:
            return True
        else:
            return False


def get_all_users_in_db():
    print('In Method: get_all_users_in_db()')

    handler = DbHandler()
    db = 'twitter_mmo'
    collection = 'user'

    result_of_db_operation = handler.read_all_docs_in_collection(db_name=db, collection_name=collection)

    items = []

    for user in result_of_db_operation['result']:
        new_user = User(name=user['user_id'], level=user['level'], character_class=user['character_class'],
                        xp=user['xp'], money=user['money'], status=user['status'], status_id=user['status_id'],
                        stats=user['stats'], items_equipped=user['items_equipped'],
                        items_inventory=user['items_inventory'])
        items.append(new_user)

    return items
