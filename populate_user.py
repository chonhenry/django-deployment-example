import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

##Fake pop script
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(n):
	i = 0
	while i<n:
		name = fakegen.name().split()
		if len(name)==2:
			User.objects.get_or_create(first_name=name[0], last_name=name[1], email=fakegen.email())
			i+=1

if __name__ == '__main__':
	print("populating script")
	populate(20)
	print("populating complete")