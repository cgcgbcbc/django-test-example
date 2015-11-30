from django.http import HttpRequest
from django.test import TestCase
# Create your tests here.
from app.models import Activity
from app.views import fetch_ticket


class TestFetchTicket(TestCase):
    # fixtures = ?
    def setUp(self):
        Activity.objects.create(remain_ticket=1)

    def test_fetch_ticket(self):
        request = HttpRequest()
        response = fetch_ticket(request)
        self.assertEqual(response.content.decode(), '成功')

        request = HttpRequest()
        response = fetch_ticket(request)
        self.assertEqual(response.content.decode(), '失败')
