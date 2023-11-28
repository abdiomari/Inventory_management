import json
import os.path

from django.core.management import BaseCommand

from djangoProject2 import settings
from inventory_app.models import Product


class Command(BaseCommand):
    help = "Populates Products table with 1000 records"

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, "products.json")
        self.stdout.write(
            self.style.SUCCESS("Started to import data")
        )
        with open(path) as file:  # file = open(path)
            products = json.load(file)
            for p in products:
                Product.objects.create(
                    productCode=p['productCode'],
                    productName=p['productName'],
                    productDescription=p['productDescription'],
                    productCategory=p['productCategory'],
                    productPrice=p["productPrice"],
                    productQuantity=p["productQuantity"],
                )

        self.stdout.write(
            self.style.SUCCESS("Completed importing data")
        )

        # celery tasks

        # python manage.py changepassword admin
