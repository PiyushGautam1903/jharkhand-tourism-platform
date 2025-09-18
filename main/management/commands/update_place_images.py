from django.core.management.base import BaseCommand
from main.models import TourismPlace

class Command(BaseCommand):
    help = 'Update existing tourism places with image paths'

    def handle(self, *args, **options):
        # Mapping of place names to image filenames
        place_images = {
            'Hundru Falls': 'places/hundru_falls.jpg',
            'Baidyanath Temple, Deoghar': 'places/baidyanath_temple.jpg',
            'Netarhat': 'places/netarhat.jpg',
            'Betla National Park': 'places/betla_national_park.jpg',
            'Rock Garden, Ranchi': 'places/rock_garden.jpg',
            'Jonha Falls (Gautamdhara)': 'places/jonha_falls.jpg',
            'Jagannath Temple, Ranchi': 'places/jagannath_temple.jpg',
            'Jamshedpur (Tata Steel City)': 'places/jamshedpur.jpg',
            'Hazaribagh National Park': 'places/hazaribagh_national_park.jpg',
            'Ranchi Hill (Pahari Mandir)': 'places/ranchi_hill.jpg',
            'Dassam Falls': 'places/dassam_falls.jpg',
            'Palamu Tiger Reserve': 'places/palamu_tiger_reserve.jpg',
        }

        updated_count = 0
        for place_name, image_path in place_images.items():
            try:
                place = TourismPlace.objects.get(name=place_name)
                place.image = image_path
                place.save()
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Updated image for: {place_name}')
                )
            except TourismPlace.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Place not found: {place_name}')
                )

        self.stdout.write(
            self.style.SUCCESS(
                f'\nSuccessfully updated images for {updated_count} places!'
            )
        )