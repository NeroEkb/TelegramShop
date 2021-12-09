import sql
import settings
import menu
import telebot

from item import Cart

method = 'db'


def GetInfo(method):
    if method == 'db':
        return sql.get(settings.db)


list = GetInfo(method)
cart = Cart()
b = telebot.TeleBot(settings.TOKEN)


@b.message_handler(commands=['start'])
def start_message(message):
    b.send_message(message.chat.id, 'Hello', reply_markup=menu.make_main_menu())


@b.message_handler(content_types=['text'])
def main(message):
    if message.chat.type == 'private':
        # Action on "Items"
        if message.text == 'Items':
            b.send_message(message.chat.id, 'Choose category',
                           reply_markup=menu.make_category_butt(GetInfo(method)))
        elif message.text == 'Delivery address':
            pass
        elif message.text == 'Cart':
            b.send_message(message.chat.id, f'{cart.getItems()}\n')


@b.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    catlist = set([item.category for item in GetInfo(method)])
    try:
        if call.message:
            # send category of items in chat
            for cat in catlist:
                if cat == call.data:
                    b.send_message(call.message.chat.id, f"Category : {cat}",
                                   reply_markup=menu.make_item_butt(GetInfo(method), cat))
            # send item information in chat
            for item in GetInfo(method):
                if str(item.ID) == call.data:
                    b.send_message(call.message.chat.id,
                                   f"Item : {item.name} \nPrice : {item.price} USD \nAmount in stock : {item.amount}",
                                   reply_markup=menu.items_butt(item))
            # add to cart
            if 'ADD' in call.data:
                b.send_message(call.message.chat.id, 'Item added')
                cart.add(int(call.data[3:]), list)
                b.send_message(call.message.chat.id, str(list[int(call.data[3:])-1]))

    except  Exception as e:
        print(repr(e))


b.infinity_polling()
