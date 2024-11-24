from django.core.management.base import BaseCommand
from faker import Faker
from properties.models import Property  # Adjust the import path according to your project
import random
from django.core.files.base import ContentFile
from io import BytesIO
import requests

class Command(BaseCommand):
    help = 'Seed property data'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of properties to create')

    def handle(self, *args, **kwargs):
        fake = Faker()
        count = kwargs['count']

        property_types = ['House', 'Apartment', 'Villa', 'Condo']
        
        for _ in range(count):
            response = requests.get("https://picsum.photos/800/600", stream=True)
            if response.status_code == 200:
                property = Property(
                    title=fake.catch_phrase(),
                    description=fake.text(),
                    price=random.uniform(100000, 1000000),
                    bedrooms=random.randint(1, 6),
                    bathrooms=random.randint(1, 4),
                    area=random.uniform(500, 5000),
                    property_type=random.choice(property_types),
                    is_available=random.choice([True, False]),
                    location=f"{fake.street_address()}, {fake.city()}",
                    created_at=fake.date_time_this_year(),
                    updated_at=fake.date_time_this_year()
                )
                # Save property and attach image
                image_file = BytesIO(response.content)
                property.image.save(f"property_{random.randint(1, 1000)}.jpg", ContentFile(image_file.read()), save=True)

        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} properties'))