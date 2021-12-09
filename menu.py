from telebot import types
from settings import TOKEN


def make_main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item3 = types.KeyboardButton('Cart')
    item2 = types.KeyboardButton('Delivery address')
    item1 = types.KeyboardButton('Items')
    markup.add(item1, item2, item3)
    return markup


def make_category_butt(itemlist):
    categoryMarkup = types.InlineKeyboardMarkup(row_width=1)
    categorylist = set([x.category for x in itemlist])
    buttons = [types.InlineKeyboardButton(text=str(cat), callback_data=str(cat)) for cat in sorted(categorylist)]
    return categoryMarkup.add(*buttons)


def make_item_butt(itemlist, cat):
    itemsMarkup = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(text=str(x.name), callback_data=str(x.ID)) for x in itemlist if
               x.category == cat]
    return itemsMarkup.add(*buttons)


def items_butt(item):
    return types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="Add to cart", callback_data='ADD'+str(item.ID)))

    # make_item_butt(get('db.db'), 'First')
