from django.test import TestCase
from django.urls import reverse

class LandingPageTests(TestCase):
    def test_landing_page_status_code(self):
        response = self.client.get(reverse('landing:index'))
        self.assertEqual(response.status_code, 200)

    def test_landing_page_template_used(self):
        response = self.client.get(reverse('landing:index'))
        self.assertTemplateUsed(response, 'landing/index.html')

    def test_landing_page_contains_correct_html(self):
        response = self.client.get(reverse('landing:index'))
        self.assertContains(response, 'Welcome to the Clinic Booking System')

    def test_landing_page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('landing:index'))
        self.assertNotContains(response, 'This text should not be on the page')