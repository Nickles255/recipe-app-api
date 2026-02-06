"""
Test custom Django management commands
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.core.management.base import CommandError
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands."""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready."""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError."""
        patched_check.side_effect = [Psycopg2Error] * 2 + \
                                    [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_gives_up_after_max_tries(self, patched_sleep, patched_check):
        """Test command stops retrying after max tries."""
        patched_check.side_effect = [OperationalError] * 10

        with self.assertRaises(CommandError):
            call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 10)
        self.assertEqual(patched_sleep.call_count, 9)
        patched_check.assert_called_with(databases=['default'])
