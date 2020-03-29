import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## Fake population script

import random
from first_app.models import AccessRecord, Topic, WebPage
from faker import Faker

fakegen = Faker()

topics = ['Social', 'Gaming', 'Marketplace', 'News', 'Search']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):


        # Get the topic for the entry
        top = add_topic()

        # Generate the fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new WebPage entry
        webpage = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create fake AccessRecord for that WebPage
        access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]


if __name__ == '__main__':
    print("Poluating script")
    populate(20)
    print("Populating Completed")
