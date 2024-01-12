from django.test import TestCase
from django.utils import timezone
from .models import CustomUser, VehicleImage

class ModelTestCase(TestCase):

    def setUp(self):
        # Create a sample user
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )

        # Create a sample vehicle image
        self.vehicle_image = VehicleImage.objects.create(
            image='path/to/test/image.jpg',
            plate_number='ABC123',
            approved=True
        )

    def test_custom_user_str(self):
        self.assertEqual(str(self.user), self.user.email)

    def test_vehicle_image_str(self):
        expected_str = f"Vehicle-{self.vehicle_image.id} - {self.vehicle_image.created_at}"
        self.assertEqual(str(self.vehicle_image), expected_str)

    def test_vehicle_image_defaults(self):
        # Test default values
        self.assertFalse(self.vehicle_image.approved)
        self.assertIsNotNone(self.vehicle_image.created_at)
        self.assertIsNotNone(self.vehicle_image.updated_at)
        self.assertLessEqual(self.vehicle_image.created_at, timezone.now())
        self.assertLessEqual(self.vehicle_image.updated_at, timezone.now())

    # Add more tests as needed
