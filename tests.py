"""Test suite for lemaster."""

from argparse import ArgumentParser
from unittest import main, TestCase
from unittest.mock import MagicMock, patch

from pkg_resources import load_entry_point
from telegram.ext import CommandHandler


class LeMasterHandlerTestCase(TestCase):
    """Test case with a loaded lemaster handler."""

    @patch('argparse._sys.argv', ['is7dtfbs8dfsdbuf', '--master-id', '823746'])
    def setUp(self):
        """Load the lemaster handler."""
        self.handler = load_entry_point(
            'lemaster', 'le.handlers', 'le_master_handler')


class TestLeMasterHandler(LeMasterHandlerTestCase):
    """Test a lemaster handler."""

    def test_handlers_type(self):
        """Test that the handler is an instance of CommandHandler."""
        self.assertIsInstance(
            self.handler,
            CommandHandler,
            'lemaster.handler is not an instance of CommandHandler.'
        )


class TestLeMasterHandlerCallback(LeMasterHandlerTestCase):
    """Test the behavior of the callback function.

    This callback should send a message containing the name of the bot's
    current master.
    """

    def setUp(self):
        """Set up a call to the callback."""
        super().setUp()
        self.bot = MagicMock()
        self.update = MagicMock()
        self.bot.get_chat().username = 'cris'
        self.handler.callback(self.bot, self.update)

    def test_send_message_is_called(self):
        """Test that bot.send_message() was called."""
        self.bot.send_message.assert_called_with(
            self.update.message.chat_id,
            'My master is @{name}.'.format(name='cris')
        )

    def test_get_chat_is_called(self):
        """Test that bot.get_chat() was called."""
        from lemaster import master_id

        self.bot.get_chat.assert_called_with(master_id)


class TestLeMasterArgumentParser(TestCase):
    """Test the behavior of the argument parser declared in lemaster."""

    @patch('argparse._sys.argv', ['is7dtfbs8dfsdbuf', '--master-id', '823746'])
    def setUp(self):
        """Load the lemaster argument parser."""
        self.parser = load_entry_point(
            'lemaster', 'le.parsers', 'le_master_parser')

    def test_parsers_type(self):
        """Test that the parser is an instance of ArgumentParser."""
        self.assertIsInstance(
            self.parser,
            ArgumentParser,
            'lemaster.parser is not an instance of ArgumentParser.'
        )


class TestLeMasterModule(TestCase):
    """Test lemaster module contents."""

    @patch('argparse._sys.argv', ['is7dtfbs8dfsdbuf', '--master-id', '823746'])
    def setUp(self):
        """Load lemaster module."""
        import lemaster

        self.lemaster = lemaster

    def test_master_id(self):
        """Test lemaster.master_id has the correct value."""
        self.assertEqual(self.lemaster.master_id, '823746')


if __name__ == '__main__':
    main()
