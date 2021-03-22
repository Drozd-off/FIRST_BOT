
"""   Modul for functions  """

import messages as msg
import answers_dicts as ans
from spell import Spell


def start(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = msg.start_text.format(first_name)

    context.bot.send_message(chat_id=chat_id,
                             text=text)


def text_msg(update, context):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    text = update.message.text.lower()

    sp = Spell()
    array = list(ans.rus_answers.keys())
    new_text = sp.word_from_dict(text, array)[0]

    send_text = ans.global_answers['rus'][new_text]

    context.bot.send_message(chat_id=chat_id,
                            text=send_text)

