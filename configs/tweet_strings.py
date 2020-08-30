print('In File: configs/tweet_strings.py')

from src.user_handling import User
from src.item_handling import Item
# Max length of a username is 15, so 280-15-1 for @ = 264

# Registration
not_registered = "Seems like you're not registered yet. 😱\nTo do so simply reply with 'register'."
successfully_registered = "Welcome to the Tweet Arena! 🥳\n" \
                          "To play this game simply tweet your actions @ this account using the following " \
                          "structure:\n\n" \
                          "'@Tweet_Arena [Command] [Optional information]'.\n\n" \
                          "For example if you want to open your inventory you'd tweet this:\n\n" \
                          "'@Tweet_Arena open inventory'."
choose_class = "Before entering the Tweet Arena you must choose a class:\n\n" \
                "1. Memer 🤡\n" \
                "2. Alt 🧜\n" \
                "3. Fake Account 🕵\n" \
                "4. Debater 🧐\n" \
                "To select your class simply reply with [class].\n" \
                "For example: If you want to join the Memers write '@Tweet_Arena Memer'."
choose_memer = "Welcome to Meme-Twitter. You're now trapped in the depth of interwebs-culture forever. 🤡\n\n" \
                "At least this comes with some benefits. Your 'cynicism' and 'luck' stats receive an x2 boost.\n\n" \
                "To find out more about stats, try accessing [stats]."
choose_alt = "Welcome to Alt-Twitter 🧜 - the combination of all the weird interests on Twitter. You'll fit right in!" \
             "Your 'vibes' and 'intelligence' stats receive an x2 boost." \
             "To find out more about stats, try accessing [stats]."
choose_fake = "Oh, another Fake-Account. 🕵 I hope you're not here to post unpopular opinions under " \
              "famous peoples tweets.\n\n" \
              "You are? Well, welcome anyway!\n\n" \
              "Your 'writing speed' and 'cynicism' stats receive an x2 boost.\n\n" \
              "To find out more about stats, try accessing [stats]."
choose_debater = "What? You're here to seriously argue with people? On Twitter?!\n\n" \
                 "You must be new. Welcome to the Debaters🧐!\n\n" \
                 "Your 'intelligence' and 'writing speed' stats receive an x2 boost.\n\n" \
                 "To find out more about stats, try accessing [stats]."
random_error = "Something went wrong. Please try again."

# Independent Commands
delete_user = ""
help = ""


def get_char_info(user: User):
    print('In Method: get_char_info()')

    if user.status == "idle":
        availability_text = "Is currently available for battles."
    else:
        availability_text = "Is currently not available for battles."

    text = "--- Player Info: " + str(user.user_name) + " ---\n\n" \
           "Level: " + str(user.level) + "\n"\
           "Class:" + str(user.character_class) + "\n"\
           "XP: " + str(user.xp) + "\n"\
           "Money: " + str(user.money) + " ₿" "\n\n"\
           + availability_text

    return text


def get_inventory(user: User):
    print('In Method: get_inventory()')

    length_inventory = str(len(user.items_inventory)) + "/ 3"

    text_inventory = ""

    for item in user.items_inventory:
        text_inventory += "- " + item + "\n"

    if len(user.items_inventory) < 1:
        text_inventory = "- None\n"

    text = "\n--- Inventory Info ---\n\n" \
           "Equipped\n" \
           "- 🖥 Device : " + str(user.items_equipped['device'] or "None") + "\n" \
           "- 🥻 Clothes : " + str(user.items_equipped['clothes'] or "None") + "\n" \
           "- 🎩 Hat : " + str(user.items_equipped['hat'] or "None") + "\n" \
           "Inventory " + length_inventory + "\n" \
           + text_inventory + \
           "\nFor more info about a specific item use '[inventory] [item name]'" \

    return text


def get_item_info(item: Item):

    item_cat_text = ""

    if item.category == "device":
        item_cat_text = "🖥 Device"
    elif item.category == "clothes":
        item_cat_text = "🥻 Clothes"
    elif item.category == "hat":
        item_cat_text = "🎩 Hat"

    text = "\n--- Item Info: " + str(item.name) + " ---\n\n" \
           "Level " + str(item.level) + "\n" \
           "Power " + str(item.power) + "\n" \
           "Category: " + str(item_cat_text) + "\n\n" \
           "Stats:\n" \
           "- 🧠 Intelligence: + " + str(item.stats['intelligence']) + "\n" \
           "- 🐎 Writing speed: + " + str(item.stats['writing speed']) + "\n" \
           "- 🍀 Luck: + " + str(item.stats['luck']) + "\n" \
           "- 🤣 Smiley usage: + " + str(item.stats['smiley usage']) + "\n" \
           "- 😈 Cynicism: + " + str(item.stats['cynicism']) + "\n" \
           "- 🦩 Vibes: + " + str(item.stats['vibes'])

    return text
