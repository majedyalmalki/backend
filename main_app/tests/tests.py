from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Plant, Photo, Reminder, Location
from datetime import datetime, timedelta


class ModelsTest(TestCase):
    def setUp(self):
        # User
        self.user = User.objects.create_user(username='testuser', password='12345')

        # Locations
        self.location1 = Location.objects.create(name='Garden', user=self.user)
        self.location2 = Location.objects.create(name='Balcony', user=self.user)

        # Plants (each related to user)
        self.plant1 = Plant.objects.create(
            name='Aloe Vera',
            description='Heals burns and purifies air',
            user=self.user
        )
        self.plant2 = Plant.objects.create(
            name='Peace Lily',
            description='Loves shade and humidity',
            user=self.user
        )

        # Assign locations to plants
        self.plant1.locations.set([self.location1, self.location2])

        # Photos (one per plant, OneToOne)
        self.photo1 = Photo.objects.create(
            plant=self.plant1, url='http://url1.com', title='Aloe Photo'
        )
        self.photo2 = Photo.objects.create(
            plant=self.plant2, url='http://url2.com', title='Lily Photo'
        )

        # Reminders
        self.reminder1 = Reminder.objects.create(
            plant=self.plant1,
            title="Water Aloe",
            date_time=datetime.now() + timedelta(days=3)
        )
        self.reminder2 = Reminder.objects.create(
            plant=self.plant2,
            title="Fertilize Lily",
            date_time=datetime.now() + timedelta(days=7)
        )

    # -------------------
    # String Representations
    # -------------------

    def test_user_string(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_plant_string(self):
        self.assertEqual(str(self.plant1), 'Aloe Vera')
        self.assertEqual(str(self.plant2), 'Peace Lily')

    def test_location_string(self):
        self.assertEqual(str(self.location1), 'Garden')
        self.assertEqual(str(self.location2), 'Balcony')

    def test_photo_string(self):
        self.assertEqual(str(self.photo1), 'http://url1.com')
        self.assertEqual(str(self.photo2), 'http://url2.com')

    def test_reminder_string(self):
        expected1 = f"Reminder for {self.plant1.name}: {self.reminder1.title} at {self.reminder1.date_time}"
        expected2 = f"Reminder for {self.plant2.name}: {self.reminder2.title} at {self.reminder2.date_time}"
        self.assertEqual(str(self.reminder1), expected1)
        self.assertEqual(str(self.reminder2), expected2)

    # -------------------
    # Relationships
    # -------------------

    def test_plant_user_relationship(self):
        self.assertEqual(self.plant1.user.username, 'testuser')

    def test_plant_locations_relationship(self):
        self.assertEqual(self.plant1.locations.count(), 2)
        self.assertIn(self.location1, self.plant1.locations.all())
        self.assertIn(self.location2, self.plant1.locations.all())

    def test_photo_relationship(self):
        self.assertEqual(self.photo1.plant, self.plant1)
        self.assertEqual(self.photo2.plant, self.plant2)

    def test_reminder_relationship(self):
        self.assertEqual(self.reminder1.plant, self.plant1)
        self.assertEqual(self.reminder2.plant, self.plant2)
        self.assertEqual(self.plant1.reminders.count(), 1)
        self.assertIn(self.reminder1, self.plant1.reminders.all())

    # -------------------
    # Cascade Deletions
    # -------------------

    def test_deleting_user_cascades_to_plant(self):
        self.user.delete()
        self.assertEqual(Plant.objects.count(), 0)

    def test_deleting_plant_cascades_to_photo(self):
        self.plant1.delete()
        self.assertEqual(Photo.objects.count(), 1)

    def test_deleting_plant_cascades_to_reminder(self):
        self.plant1.delete()
        self.assertFalse(Reminder.objects.filter(title="Water Aloe").exists())

    # -------------------
    # Reminder Date Logic
    # -------------------

    def test_reminder_date_is_in_future(self):
        self.assertGreater(self.reminder1.date_time, datetime.now())
        self.assertGreater(self.reminder2.date_time, datetime.now())
