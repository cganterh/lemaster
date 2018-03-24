"""Master plugin for the Le bot.

This plugins makes it possible to configure a Le bot to recognize a user
as it's Master.
"""


from argparse import ArgumentParser as _ArgumentParser

from telegram.ext import CommandHandler as _CommandHandler


_parser = _ArgumentParser(add_help=False)
_parser.add_argument('-m', '--master-id', required=True)
_args, _ = _parser.parse_known_args()
master_id = _args.master_id


def _say_who_is_master(bot, update):
    """Respond telling the name of the master."""
    name = bot.get_chat(master_id).username

    bot.send_message(
        update.message.chat_id,
        'My master is @{name}.'.format(name=name)
    )


_handler = _CommandHandler('master', _say_who_is_master)
