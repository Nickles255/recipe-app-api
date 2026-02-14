"""
Tests for the Django admin modifications.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse 
from django.test import Client

class AdminSiteTests(TestCase):
    """Tests for the Django admin modifications."""

    def setUp(self):
        """Create user and client."""
        self.client = Client() # Create a test client to simulate admin interactions
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user) # Log in the admin user
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User',
        )


    def test_users_listed(self):
        """Test that users are listed on user page."""
        url = reverse('admin:core_user_changelist') # Get the URL for the user list page in the admin
        res = self.client.get(url) # Make a GET request to the user list page

        self.assertContains(res, self.user.name) # Check that the user's name is in the response
        self.assertContains(res, self.user.email) # Check that the user's email is in the response            

    def test_edit_user_page(self):
        """Test that the edit user page works."""
        url = reverse('admin:core_user_change', args=[self.user.id]) # Get the URL for the edit user page in the admin
        res = self.client.get(url) # Make a GET request to the edit user page

        self.assertEqual(res.status_code, 200) # Check that the response status code is 200 (OK)

    def test_create_user_page(self):
        """Test that the create user page works."""
        url = reverse('admin:core_user_add') # Get the URL for the create user page in the admin
        res = self.client.get(url) # Make a GET request to the create user page

        self.assertEqual(res.status_code, 200) # Check that the response status code is 200 (OK)