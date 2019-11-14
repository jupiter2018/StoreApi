from django.core.management.base import BaseCommand, CommandError
from StoreApi.Store.models import Manufacturer, Shoe, ShoeType, ShoeColor

class Command(BaseCommand):
    def handle(self, *args, **options):
        ShoeType.objects.bulk_create(
            [
                ShoeType(style="sneaker"),
                ShoeType(style="boot"),
                ShoeType(style="sandal"),
                ShoeType(style="dress"),
                ShoeType(style="other")
            ]
        )
        ShoeColor.objects.bulk_create(
            [
                ShoeColor(color_name="red"),
                ShoeColor(color_name="orange"),
                ShoeColor(color_name="yellow"),
                ShoeColor(color_name="green"),
                ShoeColor(color_name="blue"),
                ShoeColor(color_name="indigo"),
                ShoeColor(color_name="violet"),
                ShoeColor(color_name="white"),
                ShoeColor(color_name="black")

            ]
        )
    