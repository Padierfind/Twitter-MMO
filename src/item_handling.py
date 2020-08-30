print('In File: src/item_handling.py')

from src.db_handling import DbHandler


class Item:

    def __init__(self, name: str, category: str, level: int, stats: dict, power: int):
        print('In Method: __init__()')

        self.name = name
        self.category = category
        self.level = level
        self.stats = stats
        self.power = power


def get_all_items_in_db():
    print('In Method: get_all_items_in_db()')

    handler = DbHandler()
    db = 'twitter_mmo'
    collection = 'items'

    result_of_db_operation = handler.read_all_docs_in_collection(db_name=db, collection_name=collection)

    items = []

    for item in result_of_db_operation['result']:
        new_item = Item(name=item['name'], category=item['category'], level=item['level'], stats=item['stats'],
                        power=item['power'])
        items.append(new_item)

    return items
