import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'protwo.settings')

import django
django.setup()

# import random module
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=10):

    for i in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_fname, last_name=fake_lname, email=fake_email)[0]

if __name__ == '__main__':
    print("Users are Populating...")
    populate(20)
    print("Users are populated completely")
