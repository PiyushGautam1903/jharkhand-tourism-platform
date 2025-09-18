from django.core.management.base import BaseCommand
from main.models import TourismPlace

class Command(BaseCommand):
    help = 'Populate the database with sample tourism places data for Jharkhand'

    def handle(self, *args, **options):
        sample_places = [
            {
                'name': 'Hundru Falls',
                'description': 'One of the most spectacular waterfalls in Jharkhand, Hundru Falls cascades from a height of 98 meters. Located near Ranchi, it is formed by the Subarnarekha River and offers breathtaking views especially during the monsoon season.',
                'place_type': 'eco',
                'district': 'Ranchi',
                'latitude': 23.4241,
                'longitude': 85.5896,
                'best_time_to_visit': 'July to November (Post Monsoon)',
                'how_to_reach': 'Located 45 km from Ranchi on the Ranchi-Purulia Road. Regular buses and taxis are available from Ranchi.',
                'nearby_attractions': 'Jonha Falls, Dasham Falls, Rock Garden',
                'entry_fee': 'Free',
                'timings': '6:00 AM to 6:00 PM'
            },
            {
                'name': 'Baidyanath Temple, Deoghar',
                'description': 'One of the twelve Jyotirlingas, Baidyanath Temple is one of the most sacred Hindu temples dedicated to Lord Shiva. The temple attracts millions of devotees during the Shravan month and is a major pilgrimage destination.',
                'place_type': 'religious',
                'district': 'Deoghar',
                'latitude': 24.4841,
                'longitude': 86.7030,
                'best_time_to_visit': 'October to March, Shravan month (July-August)',
                'how_to_reach': 'Deoghar is well connected by rail and road. Regular trains from major cities and buses are available.',
                'nearby_attractions': 'Tapovan, Naulakha Mandir, Basukinath Temple',
                'entry_fee': 'Free',
                'timings': '4:00 AM to 3:30 PM, 6:00 PM to 9:00 PM'
            },
            {
                'name': 'Netarhat',
                'description': 'Known as the "Queen of Chhota Nagpur", Netarhat is a beautiful hill station famous for its sunrise and sunset views. The serene environment and pleasant climate make it a perfect getaway from city life.',
                'place_type': 'eco',
                'district': 'Latehar',
                'latitude': 23.4667,
                'longitude': 84.2500,
                'best_time_to_visit': 'October to April',
                'how_to_reach': 'Netarhat is 154 km from Ranchi. Regular buses and private vehicles can be used to reach.',
                'nearby_attractions': 'Upper Ghaghri Falls, Lodh Falls, Magnolia Point',
                'entry_fee': 'Free',
                'timings': 'Open 24 hours'
            },
            {
                'name': 'Betla National Park',
                'description': 'One of the first national parks in India, Betla is home to tigers, elephants, leopards, and various species of deer. The park offers excellent wildlife viewing opportunities and jungle safaris.',
                'place_type': 'eco',
                'district': 'Latehar',
                'latitude': 23.8833,
                'longitude': 84.1833,
                'best_time_to_visit': 'November to June',
                'how_to_reach': 'Located 25 km from Daltonganj. Well connected by road from major cities.',
                'nearby_attractions': 'Palamau Fort, Kamaldah Lake',
                'entry_fee': 'Indian: ₹30, Foreigner: ₹500, Camera: ₹50',
                'timings': 'Summer: 6:00 AM to 6:00 PM, Winter: 6:30 AM to 5:30 PM'
            },
            {
                'name': 'Rock Garden, Ranchi',
                'description': 'A popular picnic spot in Ranchi, Rock Garden is built amidst natural rocks and offers a beautiful landscape. The garden is perfect for families and features boating facilities in the adjacent Kanke Dam.',
                'place_type': 'eco',
                'district': 'Ranchi',
                'latitude': 23.4319,
                'longitude': 85.4556,
                'best_time_to_visit': 'October to March',
                'how_to_reach': 'Located 10 km from Ranchi city center. Local buses and taxis are available.',
                'nearby_attractions': 'Kanke Dam, Birsa Zoological Park',
                'entry_fee': 'Adults: ₹10, Children: ₹5',
                'timings': '9:00 AM to 6:00 PM'
            },
            {
                'name': 'Jonha Falls (Gautamdhara)',
                'description': 'Also known as Gautamdhara, Jonha Falls is a beautiful waterfall where River Raru takes a plunge from a height of 43 meters. The place has religious significance and is surrounded by dense forests.',
                'place_type': 'eco',
                'district': 'Ranchi',
                'latitude': 23.4697,
                'longitude': 85.5761,
                'best_time_to_visit': 'July to December',
                'how_to_reach': '40 km from Ranchi on Ranchi-Purulia highway. Regular buses and private vehicles available.',
                'nearby_attractions': 'Hundru Falls, Hirni Falls',
                'entry_fee': 'Free',
                'timings': '6:00 AM to 6:00 PM'
            },
            {
                'name': 'Jagannath Temple, Ranchi',
                'description': 'Built in the architectural style of the famous Jagannath Temple of Puri, this temple is dedicated to Lord Jagannath. The annual Rath Yatra celebration attracts thousands of devotees.',
                'place_type': 'religious',
                'district': 'Ranchi',
                'latitude': 23.3569,
                'longitude': 85.3350,
                'best_time_to_visit': 'October to March, during Rath Yatra',
                'how_to_reach': 'Located in the heart of Ranchi city. Easily accessible by local transport.',
                'nearby_attractions': 'Ranchi Lake, Birsa Munda Park',
                'entry_fee': 'Free',
                'timings': '5:00 AM to 12:00 PM, 4:00 PM to 9:00 PM'
            },
            {
                'name': 'Jamshedpur (Tata Steel City)',
                'description': 'India\'s first planned industrial city, Jamshedpur is known for its well-planned infrastructure, beautiful parks, and the famous Tata Steel plant. The city offers a unique blend of industry and nature.',
                'place_type': 'cultural',
                'district': 'East Singhbhum',
                'latitude': 22.8046,
                'longitude': 86.2029,
                'best_time_to_visit': 'October to March',
                'how_to_reach': 'Well connected by rail, road, and air. Regular flights and trains from major cities.',
                'nearby_attractions': 'Jubilee Park, Tata Steel Zoological Park, Dimna Lake',
                'entry_fee': 'Varies by attraction',
                'timings': 'City is accessible 24/7'
            },
            {
                'name': 'Hazaribagh National Park',
                'description': 'A wildlife sanctuary known for its rich biodiversity, Hazaribagh National Park is home to tigers, leopards, sambars, and various bird species. The park offers excellent opportunities for wildlife photography.',
                'place_type': 'eco',
                'district': 'Hazaribagh',
                'latitude': 23.9833,
                'longitude': 85.3667,
                'best_time_to_visit': 'November to June',
                'how_to_reach': 'Located 19 km from Hazaribagh town. Well connected by road from Ranchi and other major cities.',
                'nearby_attractions': 'Hazaribagh Lake, Canary Hill',
                'entry_fee': 'Indian: ₹25, Foreigner: ₹300',
                'timings': '6:00 AM to 6:00 PM'
            },
            {
                'name': 'Ranchi Hill (Pahari Mandir)',
                'description': 'A hilltop temple dedicated to Lord Shiva, Ranchi Hill offers panoramic views of the entire city. The temple is reached by climbing 468 steps and is a popular spot for both pilgrims and tourists.',
                'place_type': 'religious',
                'district': 'Ranchi',
                'latitude': 23.3667,
                'longitude': 85.3333,
                'best_time_to_visit': 'October to March',
                'how_to_reach': 'Located in Ranchi city. Easily accessible by local transport and ropeway.',
                'nearby_attractions': 'Ranchi Lake, State Museum',
                'entry_fee': 'Free for temple, Ropeway: ₹50',
                'timings': '5:00 AM to 8:00 PM'
            },
            {
                'name': 'Dassam Falls',
                'description': 'A spectacular waterfall where River Kanchi cascades from a height of 44 meters, creating a mesmerizing curtain of water. The falls are surrounded by dense forests and offer a perfect spot for nature lovers.',
                'place_type': 'eco',
                'district': 'Ranchi',
                'latitude': 23.4833,
                'longitude': 85.5167,
                'best_time_to_visit': 'July to November',
                'how_to_reach': '40 km from Ranchi on Ranchi-Tata road. Regular buses and private vehicles available.',
                'nearby_attractions': 'Hundru Falls, Jonha Falls',
                'entry_fee': 'Free',
                'timings': '6:00 AM to 6:00 PM'
            },
            {
                'name': 'Palamu Tiger Reserve',
                'description': 'Part of the larger Betla National Park ecosystem, Palamu Tiger Reserve is known for its tiger population and diverse flora and fauna. The reserve offers jungle safaris and wildlife watching opportunities.',
                'place_type': 'eco',
                'district': 'Latehar',
                'latitude': 23.8000,
                'longitude': 84.0500,
                'best_time_to_visit': 'November to June',
                'how_to_reach': 'Well connected by road from Ranchi and Patna. Nearest railway station is Daltonganj.',
                'nearby_attractions': 'Betla National Park, Palamau Fort',
                'entry_fee': 'Indian: ₹30, Foreigner: ₹500, Vehicle: ₹100',
                'timings': '6:00 AM to 6:00 PM'
            }
        ]

        created_count = 0
        for place_data in sample_places:
            place, created = TourismPlace.objects.get_or_create(
                name=place_data['name'],
                defaults=place_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created: {place.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Already exists: {place.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'\nPopulation completed! Created {created_count} new places out of {len(sample_places)} total places.'
            )
        )