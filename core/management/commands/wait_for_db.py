"""
Django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """Entry point for command"""
        self.stdout.write('Waiting for database...')
        max_tries = 10

        for attempt in range(max_tries):
            try:
                self.check(databases=['default'])
                self.stdout.write(self.style.SUCCESS('Database available!'))
                return
            except (Psycopg2OpError, OperationalError):

                if attempt == max_tries - 1:
                    raise CommandError('Unable to connect to database after 10 tries')

                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
