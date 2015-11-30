from django.http import HttpRequest
from django.test import TestCase


# Create your tests here.
from app.views import fetch_ticket


class TestFetchTicket(TestCase):
    def test_fetch_ticket(self):
        request = HttpRequest()
        response = fetch_ticket(request)
        self.assertEqual(response.content, '成功')
