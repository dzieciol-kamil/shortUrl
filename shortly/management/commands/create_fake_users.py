#!/usr/bin/env python3
from django.core.management.base import BaseCommand, CommandError
from shortly.models import UserProfile
import urllib
import json

class Command(BaseCommand):
    help = 'Import users from randomuser.me'
    COUNT_OPTION = 'count'

    def add_arguments(self, parser):
        parser.add_argument(self.COUNT_OPTION, nargs='+', type=int)

    @staticmethod
    def import_users(object):
        count = 0
        for user in object['results']:
            try:
                new_user = UserProfile()
                new_user.email = user['email']
                new_user.first_name = user['name']['first']
                new_user.last_name = user['name']['last']
                new_user.password = user['login']['password']
                new_user.username = user['login']['username']
                new_user.date_joined = user['registered']
                new_user.save()
                count += 1
            except Exception as e:
                print (e)
        return count

    def handle(self, *args, **options):
        if self.COUNT_OPTION in options:
            count = options[self.COUNT_OPTION][0]
        else:
            raise CommandError("Number of users need to be set, and it must "
                               "be int value")

        url = "http://api.randomuser.me/?results=%s&" \
              "noinfo&" \
              "inc=name,login,email,registered" % count
        response = urllib.urlopen(url)
        raw_data = response.read()
        loaded_users = json.loads(raw_data)
        imported = self.import_users(loaded_users)
        if imported == count:
            self.stdout.write(self.style.SUCCESS(
                "Successfully created %s users" % imported))
        else:
            self.stderr.write(self.style.ERROR(
                "Could not create all users. Successfully create %s users" %
                imported))