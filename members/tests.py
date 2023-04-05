from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_members_page_status(self):
        response = self.client.get("/members/")
        self.assertEquals(response.status_code, 200)

