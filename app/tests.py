from django.http import HttpRequest
from django.test import TestCase, TransactionTestCase
# Create your tests here.
from app.models import Activity, Ticket
from app.views import fetch_ticket
from support.concurrent import test_concurrently


class TestFetchTicket(TransactionTestCase):
    # fixtures = ?
    def setUp(self):
        Activity.objects.create(remain_ticket=1)

    def test_fetch_ticket(self):
        response = fetch_ticket('student')
        self.assertEqual(response, '成功')

        response = fetch_ticket('student2')
        self.assertEqual(response, '失败')

        tickets = Ticket.objects.all()
        self.assertEqual(tickets.count(), 1)
        self.assertEqual(tickets.get().user, 'student')

    def test_concurrent_fetch(self):
        @test_concurrently(15)
        def fetch():
            fetch_ticket('student')

        fetch()
        tickets = Ticket.objects.all()
        self.assertEqual(tickets.count(), 1)
