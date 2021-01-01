import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_1.settings')

import django
django.setup()

#Fake Population Script
import random
from App_1.models import AccessRecord, Webpage, Topic
from faker import Faker

fake_gen = Faker()


# can use random topics from faker like faek_url, fake_date and fake_name but placed manually here
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics)) [0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):

        #get the topic for entry
        top = add_topic()

        # Create fake data for that entry
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()
        
        #Create new webpage entry
        webpg = Webpage.objects.get_or_create(topic = top, url=fake_url, name=fake_url)[0]

        #Create fake Access Record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date) [0]
        # name is foreign key so used webpg

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('Populate complete, check database')

