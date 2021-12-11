import sql
import settings
import menu
import telebot
from item import Cart


def get_info():
    if settings.method == 'db':
        return sql.get(settings.db)

currency = settings.currency
item_list = get_info()
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
                           reply_markup=menu.make_category_butt(item_list))
        elif message.text == 'Delivery address':
            pass
        elif message.text == 'cls':
            print(b.get_chat(message.chat.id))
            # b.delete_message(message)
        elif message.text == 'Cart':
            for item in cart.get_items():
                b.send_message(message.chat.id,
                               f'Item :{item[0]}\nAmount: {item[1]}\nFor : {item[2]} {currency}')
            b.send_message(message.chat.id, f"Total : {cart.get_total()}")


@b.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            # send category of items in chat
            for cat in set([item.category for item in item_list]):
                if cat == call.data:
                    b.send_message(call.message.chat.id, f"Category : {cat}",
                                   reply_markup=menu.make_item_butt(item_list, cat))
            # send item information in chat
            for item in item_list:
                if str(item.ID) == call.data:
                    b.send_message(call.message.chat.id,
                                   f"Item : {item.name} \nPrice : {item.price} {currency} \nAmount in stock : {item.amount}",
                                   reply_markup=menu.items_butt(item))
            # add to cart
            if 'ADD' in call.data:
                b.send_message(call.message.chat.id, f'Item added {str(item_list[int(call.data[3:]) - 1].name)} {currency}')
                cart.add(int(call.data[3:]), item_list)

    except Exception as e:
        print(repr(e))


b.infinity_polling()
